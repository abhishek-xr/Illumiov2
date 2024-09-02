import unittest
from unittest.mock import mock_open, patch
from lookup_table import LookupTable

class TestLookupTable(unittest.TestCase):

    def setUp(self):
        self.lookup_table = LookupTable()

    def test_load(self):
        mock_csv_content = "dstport,protocol,tag\n80,tcp,web\n443,tcp,ssl\n"
        with patch("builtins.open", mock_open(read_data=mock_csv_content)):
            self.lookup_table.load("lookup.csv")

        self.assertEqual(self.lookup_table.get_tag(80, "tcp"), "web")
        self.assertEqual(self.lookup_table.get_tag(443, "tcp"), "ssl")

    def test_get_tag_untagged(self):
        self.assertEqual(self.lookup_table.get_tag(22, "tcp"), "Untagged")

    def test_get_tag_case_insensitive(self):
        mock_csv_content = "dstport,protocol,tag\n80,tcp,web\n"
        with patch("builtins.open", mock_open(read_data=mock_csv_content)):
            self.lookup_table.load("dummy.csv")

        self.assertEqual(self.lookup_table.get_tag(80, "TCP".lower()), "web")

if __name__ == '__main__':
    unittest.main()