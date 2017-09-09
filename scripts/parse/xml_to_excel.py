from __future__ import print_function
import xml.etree.ElementTree as ET

def main():
    
    tree = ET.parse('xml/test_fields.xml')
    root = tree.getroot()

    # Get Type, Name, Desc, OID, BID for Header
    obj_type = root.attrib.get('type')
    obj_name = None
    obj_desc = None
    object_id = None
    branch_id = None
    for child in root:
        if child.attrib.get('name') == 'name':
            obj_name = child.attrib.get('value')
        if child.attrib.get('name') == 'description':
            obj_desc = child.attrib.get('value')
        if child.attrib.get('name') == 'objectId':
            object_id = child.attrib.get('value')
        if child.attrib.get('name') == 'branchId':
            branch_id = child.attrib.get('value')

    # Header
    print("Type:\t{}".format(obj_type))
    print("Name:\t{}".format(obj_name))
    print("Desc:\t{}".format(obj_desc))
    print("Object ID:\t{}".format(object_id))
    print("Branch ID:\t{}\n". format(branch_id))
    
    # Body
    print("ROOT CHILDREN") 
    print("Enum\tName\tValue\tValueType\tText")
    for enum,child in enumerate(root,1):
        # remove whitespace
        if child.text is not None:
            child.text = child.text.strip()
        print("{}\t{}\t{}\t{}\t{}".format(
            enum, 
            child.attrib.get('name'), 
            child.attrib.get('value'), 
            child.attrib.get('valueType'),
            child.text)
        )
    
    # table and object Types
    print("\nTABLES")
    for child in root:
        # get tables
        if child.attrib.get('valueType') == 'table' or child.attrib.get('valueType') == 'object':
            print("Table Name\t{}".format(child.attrib.get('name')))
            # get rows, cols
            for row in child:
                for col in row:
                    print(col.attrib.get('name'), end='\t')
                print()
                for col in row:
                    print(col.attrib.get('value'), end='\t')
                print()
            print()

if __name__ == '__main__':
    main()