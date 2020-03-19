import json
from typing import Dict, Any
from fields import Field, Text, Number
from consts import TEXT_TYPE, NUMBER_TYPE

class UnknownTypeException(Exception):
    pass

class NotFoundTypeException(Exception):
    pass

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
            self._type_handling(value)
    
    def _type_handling(self, value:Any):
        if type(value) is str:
           field_init = self._get_type_of_field(value)
        if type(value) is dict:
            if 'type' not in value:
                raise NotFoundTypeException(f'type is not defined at {value}')
            field_init = self._get_type_of_field(value['type'])
        print(field_init)
            

    def _get_type_of_field(self, value:Any) -> Field:
        '''
        return specified type of the field
        '''
        if value == TEXT_TYPE:
            return Text
        elif value == NUMBER_TYPE:
            return Number
        else:
            raise UnknownTypeException(f'{value} is unknown')
