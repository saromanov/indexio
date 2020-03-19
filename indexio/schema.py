import json
from typing import Dict, Any
from fields import Text
from consts import TEXT_TYPE, NUM_TYPE

class Schema:
    '''
    basic class for schema
    '''
    def __init__(self):
        pass

class SchemaJSON(Schema):
    '''
    definition of the schema on JSON format
    it can be defined as
    {
        "data":"text",
        "content":"text"
    }
    '''
    def __init__(self, definition:str):
        self._fields = self._create_fields(self._load(definition))
        super(SchemaJSON, self).__init__()
    
    def _load(self, definition:str) -> Dict[str, Any]:
        '''
        loading of json data
        '''
        try:
            data = json.loads(definition)
        except ValueError as e:
            raise Exception('Unable to load json data')
        return data
    
    def _create_fields(self, raw_data:Dict[str,Any]):
        fields = []
        for key, value in raw_data.items():
            if type(value) is str:
                print('True')
