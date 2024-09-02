import unittest
from unittest.mock import Mock, patch, mock_open
from flowLog_Analyzer import FlowLogAnalyzer

class TestFlowLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.mock_lookup_table = Mock()
        self.analyzer = FlowLogAnalyzer(self.mock_lookup_table)

    def test_process_line(self):
        log_line = "2 123456789012 eni-1234567890abcdef 172.31.16.139 172.31.16.21 20641 80 6 1 52 1418530010 1418530070 ACCEPT OK"
        self.mock_lookup_table.get_tag.return_value = "web"

        self.analyzer.process_line(log_line)

        self.assertEqual(self.analyzer.port_protocol_counts[(80, "tcp")], 1)
        self.assertEqual(self.analyzer.tag_counts["web"], 1)

    def test_process_log(self):
        mock_log_content = "2 123456789012 eni-1234567890abcdef 172.31.16.139 172.31.16.21 20641 80 6 1 52 1418530010 1418530070 ACCEPT OK\n"
        self.mock_lookup_table.get_tag.return_value = "web"

        with patch("builtins.open", mock_open(read_data=mock_log_content)):
            self.analyzer.process_log("dummy.log")

        self.assertEqual(self.analyzer.port_protocol_counts[(80, "tcp")], 1)
        self.assertEqual(self.analyzer.tag_counts["web"], 1)

    def test_get_protocol(self):
        self.assertEqual(self.analyzer._get_protocol("6"), "tcp")
        self.assertEqual(self.analyzer._get_protocol("17"), "udp")
        self.assertEqual(self.analyzer._get_protocol("1"), "unknown")

if __name__ == '__main__':
    unittest.main()