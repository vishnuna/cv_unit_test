'''
Convert cv dataset xml into Python dictionaries. Output py files, per meta file, with dicts.
'''

import xml.etree.ElementTree as ET

from os import listdir
from os.path import isfile, join

path = "./xml/dataset/"
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

for file in files:
    
    tree = ET.parse(file)
    root = tree.getroot()
    output = {}
    
    for child in root.iter('parameter'):
        
        if child.tag in ['object', 'objectNode']:
            object_tag = child.attrib.pop('type')
            output[object_tag] = child.attrib

        if child.tag == 'property':
            property_tag = child.attrib.pop('name')
            output[object_tag][property_tag] = child.attrib
    
    file_name = file[14:-4]
    print(file_name, '=', output)
    