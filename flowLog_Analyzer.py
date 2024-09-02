from collections import defaultdict

class FlowLogAnalyzer:
    """Analyzing AWS VPC flow logs: count occurrences of tags and port/protocol combinations."""

    def __init__(self, lookup_table):
        self.lookup_table = lookup_table
        self.tag_counts = defaultdict(int)
        self.port_protocol_counts = defaultdict(int)

    def process_log(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.process_line(line)

    def process_line(self, line):
        fields = line.strip().split()
        if len(fields) < 14 or not fields[0].isdigit():
            return

        version, account_id, interface_id, srcaddr, dstaddr, srcport, dstport, protocol, *_ = fields
        try:
            dstport = int(dstport)
            protocol = self._get_protocol(protocol).lower()  #protocol is lowercase

            # updating port/protocol counts
            self.port_protocol_counts[(dstport, protocol)] += 1

            # getting corresponding tag from the table
            tag = self.lookup_table.get_tag(dstport, protocol)
            if tag is None:
                tag = 'Untagged'
            self.tag_counts[tag] += 1

        except ValueError as e:
            print(f"Error processing line: {line} | Error: {str(e)}")
            return

    @staticmethod 
    def _get_protocol(protocol_number):
        return {
            '6': 'tcp',
            '17': 'udp'
        }.get(protocol_number, 'unknown')  #lowercase for consistency