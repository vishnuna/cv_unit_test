import xml.etree.ElementTree as ET

from os import listdir
from os.path import isfile, join

path = "../xml/meta/"
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]


for file in files:
    tree = ET.parse(file)
    root = tree.getroot()
    meta = []
    
    # assign group to child nodes
    for child in root.iter():
        if child.tag == 'object':
            pass
        if child.tag == 'property':
            pass

    if __name__ == '__main__':
        for i in meta:
            print(i)