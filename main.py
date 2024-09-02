import sys
from lookup_table import LookupTable
from flowLog_Analyzer import FlowLogAnalyzer
from outputWrite import OutputWriter

def main(log_filename, lookup_filename, output_filename):

    lookup_table = LookupTable()
    lookup_table.load(lookup_filename)

    analyzer = FlowLogAnalyzer(lookup_table)
    analyzer.process_log(log_filename)

    OutputWriter.write(analyzer.tag_counts, analyzer.port_protocol_counts, output_filename)
    print(f"Analysis complete. Results written to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 4:

        print("Usage: python main.py <log_filename> <lookup_filename> <output_filename>")
        sys.exit(1)
    log_filename = sys.argv[1]
    lookup_filename = sys.argv[2]
    output_filename = sys.argv[3]

    main(log_filename, lookup_filename, output_filename)

