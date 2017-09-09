from collections import namedtuple
import xml.etree.ElementTree as ET
from lxml import objectify

class DataSourceFields(object):
    '''Field mapping to tab, name, description'''
    Field = namedtuple('DataSourceField', 'tab name description')
    fields = [
        Field(tab='General', name='hosting', description='Source Hosting'),
        Field(tab='General', name='dataStructure', description='Data Structure'),
        Field(tab='General', name='dbSource', description='DB Source'),
        Field(tab='General', name='loader', description='DB Source'),
        Field(tab='General', name='freezeLevel', description='Freeze level'),
        Field(tab='General', name='defaultVisibilityInModel', description='Default Visibility in Model'),
        Field(tab='Layout', name='layout', description=None),
        Field(tab='Key Fields', name='keyFields', description=None),
        Field(tab='Key Fields', name='createIndexOnKeyFields', description='Create Index On Key Fields'),
        Field(tab='Key Fields', name='indexOnKeyFieldsClustered', description='Index On Key Fields Clustered'),
        Field(tab='Indexes', name='index', description=None),
        Field(tab='Data Storage', name='storageType', description='Data Storage Type'),
        Field(tab='Data Storage', name='internalSourceTablePrefix', description='Data Table Prefix'),
        Field(tab='Data Storage', name='fourEyesCheck', description='Four Eyes Check'),
        Field(tab='Data Storage', name='readOnlyAdjustment', description='Read Only Adjustment'),
        Field(tab='Data Storage', name='computeStatistics', description='Compute Statistics'),
        Field(tab='Data Storage', name='instanceRebuildRestriction', description='Instance Rebuild Restrictions'),
        Field(tab='Data Storage', name='reapplyAdjustmentsAfterDataLoad', description='Reapply Adjustments after data load'),
        Field(tab='Adjustment Validations', name='validations', description=None),
        Field(tab='Original Data Configuration', name='loaderConfigFields', description=None),
        Field(tab='Loader Actions', name='loaderActions', description=None),
        Field(tab='Post Table Creation Statements', name='postTableCreationStatements', description='Data Table Statements'),
        Field(tab='Post Table Creation Statements', name='postAdjustmentTableCreationStatements', description='Adjustment Table Statements'),
        Field(tab='Variables', name='dataLoadVariables', description=None),
        Field(tab='Loader Parameters', name='delimiter', description='Delimiter'),
        Field(tab='Loader Parameters', name='optionallyEnclosedBy', description='Optionally Enclosed By'),
        Field(tab='Loader Parameters', name='skipRows', description='Number of rows to skip'),
        Field(tab='Loader Parameters', name='newlineConversion', description='DOS/Unix Conversion'),
        Field(tab='Loader Parameters', name='targetEncoding', description='Target File Encoding (DB-specific)'),
        Field(tab='Loader Parameters', name='convertEncoding', description='Convert Encoding'),
        Field(tab='Loader Parameters', name='loaderEnumerationField', description='Loader Enumeration Field'),
        Field(tab='Loader Parameters', name='trailingNullCols', description='Trailing null columns in file'),
        Field(tab='Loader Parameters', name='keepTableContent', description='Keep current table content on load'),
        Field(tab='Loader Parameters', name='loadSheetName', description='Sheet name used when loading from Excel file'),
        Field(tab='Loader Parameters', name='columnHeadersFromFile', description='Match columns from source file by name (use headers)'),
        Field(tab='Loader Parameters', name='maxErrors', description='Max number of errors'),
        Field(tab='Loader Parameters', name='doNotFailIfRejected', description='Allow rejected records (set WARNING)'),
        Field(tab='Loader Control/Format File', name='loaderControlFile', description=None),
        Field(tab='File Preprocess Code', name='parameterIsNotAFile', description='Loader parameter is not a file name'),
        Field(tab='File Preprocess Code', name='codeWillCreateFile', description='Output file will be CREATED by the code'),
        Field(tab='File Preprocess Code', name='loaderPreprocessCode', description='File Preprocess Code'),
        Field(tab='Archive', name='archivalProperties', description=None),
    ]

class DataSource(object):
    '''CV Data Source object.'''
    def __init__(self, xml, schema=DataSourceFields()):
        self._tree = ET.parse(xml)
        self._root = self._tree.getroot()
        self._xml = ET.tostring(self._root)
        self.name = self._tree.find(".*[@name='name']").get("value")
        self.description = self._tree.find(".*[@name='description']").get("value")
        self.object_id = self._tree.find(".*[@name='objectId']").get("value")
        self.branch_id = self._tree.find(".*[@name='branchId']").get("value")
        self.documentation = self._tree.find(".*[@name='comment']").get("value")
        self.fields = {}
        for field in schema.fields:
            self.fields[field.description] = self._tree.find(".*[@name='{}']".format(field.name)).get("value")

if __name__ == '__main__':
    ds = DataSource("../../xml/xml/test_fields.xml")
    a = ds._tree.find(".*[@name='name']")
    print(ds.name, ds.description)
    print(ds.object_id, ds.branch_id)
    print(ds.documentation)
    
    #for k,v in ds.fields.items():
    #    print(k,'=',v)
    
    dss = objectify.fromstring()






















