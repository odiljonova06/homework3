
class Boolen:
    def __get__ (self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set_name__(self, owner, name ):
        self.name = name
    
    def __set__(self, instance, value):
        print (f"Qiymati o'zgartirildi: {value}")
        if isinstance (value, bool):
            instance.__dict__[self.name] = value 
        else:
            raise ValueError ("Value must be a bool")