"""

O padrão singleton 

"""

class classeTest():
    
    instance = None
    
    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance