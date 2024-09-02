import unittest
from unittest.mock import mock_open, patch
from outputWrite import OutputWriter

class TestOutputWriter(unittest.TestCase):

    def test_write(self):
        tag_counts = {"sv_P2": 1, "sv_P1": 2, "sv_P4": 1, "email": 3, "Untagged": 9}
        port_protocol_counts = {
            (22, "tcp"): 1, (23, "tcp"): 1, (25, "tcp"): 1,
            (110, "tcp"): 1, (143, "tcp"): 1, (443, "tcp"): 1,
            (993, "tcp"): 1, (1024, "tcp"): 1, (49158, "tcp"): 1,
            (80, "tcp"): 1
        }

        expected_output = (
            "Tag Counts:\r\n"
            "Tag,Count\r\n"
            "sv_P2,1\r\n"
            "sv_P1,2\r\n"
            "sv_P4,1\r\n"
            "email,3\r\n"
            "Untagged,9\r\n"
            "\r\n"
            "Port/Protocol Combination Counts\r\n"
            "Port,Protocol,Count\r\n"
            "22,tcp,1\r\n"
            "23,tcp,1\r\n"
            "25,tcp,1\r\n"
            "80,tcp,1\r\n"
            "110,tcp,1\r\n"
            "143,tcp,1\r\n"
            "443,tcp,1\r\n"
            "993,tcp,1\r\n"
            "1024,tcp,1\r\n"
            "49158,tcp,1\r\n"
        )

        with patch("builtins.open", mock_open()) as mock_file:
            OutputWriter.write(tag_counts, port_protocol_counts, "dummy_output.csv")

            # Combine all calls to write into a single string
            actual_output = "".join(call.args[0] for call in mock_file().write.call_args_list)

            # Verify the actual output matches the expected output
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()