#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
struct Bid { string id, title; double amount; };
Bid searchBid(const vector<Bid>& bids,const string& id){
    for(const auto& b:bids) if(b.id==id) return b;
    return {"","",0.0};
}
void selectionSort(vector<Bid>& bids){
    for(size_t i=0;i<bids.size();++i){
        size_t min=i;
        for(size_t j=i+1;j<bids.size();++j) if(bids[j].title<bids[min].title) min=j;
        swap(bids[i],bids[min]);
    }
}
int main(){
    vector<Bid> bids={{"1001","Laptop",500},{"1002","Desk",150},{"1003","Monitor",200}};
    selectionSort(bids);
    Bid b=searchBid(bids,"1002");
    if(!b.id.empty()) cout<<b.id<<" | "<<b.title<<" | "<<b.amount<<"\n";
    return 0;
}
