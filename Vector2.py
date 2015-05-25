import math

class Vector:
    """Vectors in R^n"""
    
    def __init__(self,n,m=None):
        if m is None:
            self.a=0
            self.b=0
            self.c=0
        elif type(m)==list:
            self.a=m[0]
            self.b=m[1]
            self.c=m[2]
        elif type(m)==float:
            self.a=m
            self.b=m
            self.c=m
        elif type(m)==int:
            self.a=m
            self.b=m
            self.c=m

    def __str__(self):
        return '%,%,%' % (self.a, self.b, self.c)
        
    
