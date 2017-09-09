import xml.etree.ElementTree as ET

from os import listdir
from os.path import isfile, join

path = "../../xml/dataset/"
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
dataset_attributes = []

for file in files:
    tree = ET.parse(file)
    root = tree.getroot()
    dataset = []
    
    # assign group to child nodes
    group = None
    for parameter in root.iter('parameter'):
        if parameter.get('group') is not None:
            group = parameter.get('group')
        else:
            parameter.attrib['group'] = group
        dataset.append({parameter.get('name'):parameter.attrib})
    
    with open('../../output/dataset.txt', 'a+') as outfile:
        outfile.write(str(dataset) + '\n')
        
    if __name__ == '__main__':
        for i in dataset:
            print(i)