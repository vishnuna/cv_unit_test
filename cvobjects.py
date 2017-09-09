import xmltodict

class CVObject(object):
    def __init__(self, xml):
        #if isfile():
        self._xml = xml
        self.fields = xmltodict.parse(self._xml).get('object')
        self.type = self.fields.get('@type')
        self.version = self.fields.get('@version')
        self.stamp = self.fields.get('@stamp')
    
    def getname(self, name, attrib='@value'):
        '''Retrieves attributes in direct children of root object.'''
        children = self.fields.get('property')
        for child in children:
            if child.get('@name') == name:
                if child.get(attrib) is not None:
                    return child.get(attrib)
                if child.get('@valueType') == 'tree':
                    return child.get('objectNode')
                # default nested objects or None
                return child.get('object')
        return
    
    def getdesc(self, desc):
        pass
    
    def getable(self, name):
        '''Retrieve table and re-format as list of dicts'''
        fmt_table = []
        table = self.getname(name)
        if isinstance(table, dict):
            table = [table]
        for obj in table:
            fmt = {}
            properties = obj.get('property')
            if isinstance(properties, dict):
                properties = [properties]
            for p in properties:
                if p.get('@valueType') in ['table','object','hierarchy']:
                    fmt[p.get('@name')] = p.get('object')
                elif p.get('@valueType') == 'url':
                    fmt[p.get('@name')] = p.get('#text')
                else:
                    fmt[p.get('@name')] = p.get('@value')
            fmt_table.append(fmt)
        return fmt_table
    
    def __str__(self):
        print(self.type)
        for p in self.fields.get('property'):
            if p.get('@valueType') in ['table','object','hierarchy']:
                 print("{}: {}".format(p.get('@name'), p.get('@valueType')))
            else:
                print("{}: {}".format(p.get('@name'), p.get('@value')))
        return ''
            
class DataSource(CVObject):
    def __init__(self, xml):
        CVObject.__init__(self, xml)
        self.layout = self.getable('layout')
        self.key_fields = self.getable('keyFields')
        self.adjustment_validations = self.getable('validations')
        self.orig_data_config = self.getable('loaderConfigFields')
        self.loader_actions = self.getable('loaderActions')
        self.post_table_creation_statement = self.getable('postTableCreationStatements')
        self.post_adj_creation_statement = self.getable('postAdjustmentTableCreationStatements')
        self.variables = self.getable('dataLoadVariables')

if __name__ == '__main__':
    path = "xml/xml/test_fields.xml"
    pathdm = "xml/xml/test_dm.xml"
    cv = CVObject(path)
    ds = DataSource(path)
    dm = CVObject(pathdm)
    a = ds.getable('keyFields')