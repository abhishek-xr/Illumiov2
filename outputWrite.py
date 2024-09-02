import csv 

class OutputWriter:

    @staticmethod 
    def write(tag_counts,port_protocol_counts, filename):

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['Tag Counts:'])
            writer.writerow(['Tag', 'Count'])
            for tag, count in tag_counts.items():
                writer.writerow([tag,count])

            writer.writerow([])

            writer.writerow(['Port/Protocol Combination Counts'])
            writer.writerow(['Port', 'Protocol', 'Count'])
            for(port, protocol), count in sorted(port_protocol_counts.items()):
                writer.writerow([port,protocol,count])