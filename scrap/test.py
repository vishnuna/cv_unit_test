import meta_dict
import xmltodict

path = "./xml/xml/test_fields.xml"
        
class ObjectUI(object):
    def __init__(self, xml):
        with open(xml,'r') as file:
            self._xml = file.read()
        self.fields = xmltodict.parse(self._xml).get('object')
    
    def dictToAttrib(self, **attrib):
        self.__dict__.update(attrib)
    
    def getByName(self, name):
        for i in self.fields['property']:
            if i.get('@name') == name:
                if i.get('object') is not None:
                    return i.get('object')
                return i.get('@value')
        return
    
    # TODO:
    def getByDesc(self, desc):
        pass
    
    # TODO:
    def getSubTable(self, tablename):
        pass


class GlobalObject(ObjectUI):
    def __init__(self, xml):
        ObjectUI.__init__(self, xml)
        self.name = self.getByName('name')
        self.description = self.getByName('description')
        self.object_id = self.getByName('objectId')
        # self.is_generated = self.getByName('isGenerated')
        # self.db_id = self.getByName('dbId')

class DocData(ObjectUI):
    def __init__(self, xml):
        ObjectUI.__init__(self, xml)    
        self.branch_id = self.getByName('branchId')
        self.comment = self.getByName('comment')
        self.doc_file = self.getByName('docFile')

class DataSource(GlobalObject):
    '''CV Data Source object.'''
    def __init__(self, xml):
        GlobalObject.__init__(self, xml)
        self._layout = None
        self._key_fields = None
        self._instance_keys = None
        self._loader_actions = None
        self._variables = None
    
    @property
    def layout(self):
        rows = []
        for row in self.getByName('layout'):
            d = {}
            for col in row['property']:
                d[col.get('@name')] = col.get('@value')
            rows.append(d)
        return rows
    
    

ds = DataSource(path)

"""
class DocData(object):
    def __init__(self, comment=None, doc_file=None):
        self.comment = comment
        self.doc_file = doc_file

class GlobalObject(object):
    def __init__(self, name=None, description=None, object_id=None):
        self.name = name
        self.description = description
        self.object_id = object_id

class ObjectInBranch(GlobalObject):
    def __init__(self, branch_id=None):
        GlobalObject.__init__(self)
        self.branch_id = branch_id

class DataSource2(ObjectInBranch, DocData):
    def __init__(self, xml):
        with open(xml,'r') as file:
            self._xml = file.read()
        self.fields = xmltodict.parse(self._xml).get('object')
        ObjectInBranch.__init__(self)
        DocData.__init__(self)
        self._layout = None
        self._key_fields = None
        self._instance_keys = None
        self._loader_actions = None
        self._variables = None

go = GlobalObject()
ob = ObjectInBranch()
dd = DocData()
ds = DataSource2(path)
"""