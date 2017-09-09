from cvobjects import *
import logging

# Set the log output file, and the log level
logging.basicConfig(filename="unit_test.log", level=logging.DEBUG)

def unit_test_1(data_source):
    '''Check formatting is UTF8'''
    if data_source.getname("encoding") != "UTF8":
        logging.debug("Test Failed")
        print(data_source.name, data_source.description)
        return False
    logging.debug("Test Passed")
    return True

def _unit_test_1(data_source):
    '''Check formatting is UTF8'''
    return data_source.getname("encoding") == "UTF8"

def unit_test_2(data_source):
    '''Data Source field "Source Hosting" should be set to "INTERNAL"'''
    return data_source.getName("hosting") == "INTERNAL"

def unit_test_3(data_source):
    return data_source.fields.get("Data Structure") == "FLAT"
    
ds = DataSource('xml/xml/test_fields.xml')
result = unit_test_1(ds)
#result2 = unit_test_2(ds)
#result3 = unit_test_3(ds)
print(result)
#print(result2)
#print(result3)