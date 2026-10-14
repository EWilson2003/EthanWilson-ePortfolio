import unittest
from query_builder import build_rescue_query


class QueryBuilderTests(unittest.TestCase):
    def test_reset_returns_all(self):
        self.assertEqual(build_rescue_query("Reset"), {})

    def test_water_filter(self):
        query = build_rescue_query("Water Rescue")
        self.assertEqual(query["animal_type"], "Dog")
        self.assertEqual(query["sex_upon_outcome"], "Intact Female")
        self.assertIn("$in", query["breed"])

    def test_unknown_filter_rejected(self):
        with self.assertRaises(ValueError):
            build_rescue_query("Unknown")

    def test_breed_text_is_escaped(self):
        query = build_rescue_query("Reset", "Lab.*")
        self.assertEqual(query["breed"]["$regex"], "Lab\\.\\*")


if __name__ == "__main__":
    unittest.main()
