'''
Convert cv metadata xml into Python dictionaries. Output py files, per meta file, with dicts.
'''

import xml.etree.ElementTree as ET

from os import listdir
from os.path import isfile, join

path = "./xml/meta/"
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
l = []

for file in files:
    
    tree = ET.parse(file)
    root = tree.getroot()
    output = {}
    
    object_tag = None
    for child in root.iter():
        
        if child.tag in ['object', 'objectNode']:
            object_tag = child.attrib.pop('type')
            output[object_tag] = child.attrib

        if child.tag == 'property':
            property_tag = child.attrib.pop('name')
            output[object_tag][property_tag] = child.attrib
    
    file_name = file[11:-4]
    print(file_name, '=', output)
    