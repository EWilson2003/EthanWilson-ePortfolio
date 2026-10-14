#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <memory>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

struct Bid { string id, title; double amount; };

bool valid(const Bid& b){ return !b.id.empty() && !b.title.empty() && b.amount >= 0.0; }

class BidBST {
    struct Node {
        Bid bid; unique_ptr<Node> left,right;
        explicit Node(Bid b):bid(move(b)){}
    };
    unique_ptr<Node> root;
    static void insert(unique_ptr<Node>& n,const Bid& b){
        if(!n){n=make_unique<Node>(b);return;}
        if(b.id<n->bid.id) insert(n->left,b); else if(b.id>n->bid.id) insert(n->right,b); else n->bid=b;
    }
public:
    void insert(const Bid& b){insert(root,b);}
    const Bid* find(const string& id) const{
        Node* n=root.get();
        while(n){ if(id==n->bid.id)return &n->bid; n=id<n->bid.id?n->left.get():n->right.get(); }
        return nullptr;
    }
};

const Bid* vectorFind(const vector<Bid>& v,const string& id){
    auto it=find_if(v.begin(),v.end(),[&](const Bid& b){return b.id==id;});
    return it==v.end()?nullptr:&*it;
}

template<class F>
double benchmark(F fn,int repetitions){
    volatile size_t sink=0;
    auto start=chrono::high_resolution_clock::now();
    for(int i=0;i<repetitions;++i){ const Bid* p=fn(); sink += p ? p->id.size() : 0; }
    auto stop=chrono::high_resolution_clock::now();
    return chrono::duration<double,micro>(stop-start).count()/repetitions;
}

int main(){
    vector<Bid> bids;
    for(int i=0;i<10000;++i){
        Bid b{to_string(100000+i),"Item "+to_string(i),double(i%500)+0.99};
        if(valid(b)) bids.push_back(b);
    }

    // O(n log n) introsort replaces the reconstructed original O(n^2) selection sort.
    sort(bids.begin(),bids.end(),[](const Bid& a,const Bid& b){return a.title<b.title;});

    unordered_map<string,Bid> table;
    table.reserve(bids.size()*2);
    BidBST tree;
    for(const auto& b:bids){table[b.id]=b;tree.insert(b);}

    const string target="109999";
    const int reps=5000;
    double vectorUs=benchmark([&](){return vectorFind(bids,target);},reps);
    double hashUs=benchmark([&]()->const Bid*{
        auto it=table.find(target); return it==table.end()?nullptr:&it->second;
    },reps);
    double bstUs=benchmark([&](){return tree.find(target);},reps);

    cout<<fixed<<setprecision(4);
    cout<<"Average search time ("<<reps<<" repetitions)\n";
    cout<<"Vector linear search: "<<vectorUs<<" microseconds | O(n)\n";
    cout<<"Hash table lookup:    "<<hashUs<<" microseconds | average O(1)\n";
    cout<<"BST lookup:           "<<bstUs<<" microseconds | average O(log n), worst O(n)\n";
    cout<<"Sorting: std::sort O(n log n) average/worst practical bound\n";
    return 0;
}
