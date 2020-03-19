from schema import Schema

class Indexio:
    def __init__(self, schema: Schema, file_store:str):
        self._schema = schema