class Field:
    '''
    general class for the field
    '''
    def __init__(self):
        pass


class Text(Field):
    def __init__(self, name:str, value:str, *args, **kwargs):
        self._name = name
        self._value
        super(Text, self).__init__()

class Number(Field):
    def __init__(self, name:str, value, *args, **kwargs):
        super(Number, self).__init__()