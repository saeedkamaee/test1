from test_stu import Stu

class Student(Stu):
    __slots__=("__code",)
    def __init__(self,code,**kwargs):
        super().__init__(**kwargs)
        self.code=code
    
    def __str__(self):
        return f"{super().__str__()} code={str(self.__code)}"

    def __call__(self,code,**kwargs):
       super().__call__(**kwargs)
       if code!=None:
           self.code=code

    @property 
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, value):
        if isinstance (value,int) and len(str(value))==5:
            self.__code=value
        else:
            raise ValueError("code is wrong")

print()
if __name__ == "__main__":    
    s7=Student(name="ali",family="mohamad",code=12354)
    print(s7)
    print(callable(s7)) 

    s7(name="saeed",family="kama",code=1239)
    print(s7)   


