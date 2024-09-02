import csv 

class LookupTable:
    """handling loading and querying of tag lookup table"""

    def __init__(self):
        self.table = {}

    def load(self,filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                #creating a tuple key of (port, protocol)
                key = (int(row['dstport']), row['protocol'].lower())
                self.table[key] = row['tag']
    
    def get_tag(self,port,protocol):
        """ getting tag for given port/protocol or else 'untagged' """
        return self.table.get((port,protocol.lower()), 'Untagged')