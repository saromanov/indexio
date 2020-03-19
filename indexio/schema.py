import json

class SchemaBasic:
    '''
    basic class for schema
    '''
    def __init__(self):
        pass

class SchemaJSON(SchemaBasic):
    '''
    definition of the schema on JSON format
    it can be defined as
    {
        "data":"text",
        "content":"text"
    }
    '''
    def __init__(self, definition:str):
        self._content = self._load(definition)
    
    def _load(self, definition:str):
        '''
        loading of json data
        '''
        try:
            data = json.loads(definition)
        except ValueError as e:
            raise Exception('Unable to laod json data')
        return data
