import cvobjects

from os import listdir
from os.path import isfile, join, splitext
from zipfile import ZipFile

path = "xml/xml"
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

for file in files:

    filename, extension = splitext(file)
    #print("Processing {}...".format(file))
    #print(filename, extension)
    
    if extension == '.zip' and filename == 'xml/xml/BCAR_sh':
        print(filename)
        count = 0
        with ZipFile(file) as myzip:
            for myfile in myzip.namelist():
                filename2, extension2 = splitext(myfile)
                if extension2 == '.xml':
                    obj = cvobjects.CVObject(myzip.read(myfile))
                    
                    '''
                    if obj.type == 'DataSource':
                        for row in obj.getable('layout'):
                            if row.get('description') in [None, ""]:
                                print("Type:{}\tName:{}\tField:{}".format(obj.type, obj.getname('name'), row.get('name')))
                    '''
                    if obj.getname('description') is None:
                        count += 1
                        #print("Type:{}\tName:{}\tDesc:{}".format(obj.type, obj.getname('name'), obj.getname('description')))
        print(count)
                        
    elif extension == '.xml':
        pass