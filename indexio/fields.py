class Field:
    '''
    general class for the field
    '''
    def __init__(self):
        pass


class Text(Field):
    def __init__(self, name:str, *args, **kwargs):
        self._name = name
        super(Text, self).__init__()

class Number(Field):
    def __init__(self, name:str, value, *args, **kwargs):
        super(Number, self).__init__()