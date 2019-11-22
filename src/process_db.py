#! /usr/bin/env python

import sys
import xml.etree.ElementTree as ET



if __name__ == "__main__": 

    db_file = sys.argv[1]

    tree = ET.parse(db_file)
    len(tree.findall('entry'))
