class Stu: 
    __slots__= ("__name","__family",)
    def __init__(self,name:str,family:str):
        
        self.name= name
        self.family= family
    @property
    def name (self):
        return self.__name
    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self.__name=value
        else:
            raise ValueError
        
    @property
    def family (self):
        return self.__family
    @family.setter
    def family(self,value):
        if isinstance(value,str):
            self.__family=value
        else:
            raise ValueError
    def __str__(self):
        return(f"name={self.__name} family={self.__family}")
    def __call__(self, name,family):
        if name!=None:
            self.name=name

        if family!=None:
            self.family=family
    
    def __eq__(self, __value:object):
        if not isinstance(__value,Stu):
            return False
        return str(__value)==str(self)
    def __hash__(self):
        return hash(str(self))
        
if __name__=="__main__":        

    s1=Stu(name="ali",family="moradi")
    print(s1.name)
    print(s1)
    print(callable(s1))
    s2=Stu(name="saeed",family="kama")
    print(s2)
    print(s1==s2)

    s3=Stu(name="saeed",family="kama")
    print(s3)
    print(s3==s2)
    input()
    if isinstance(s1,Stu):

        print("true")
    else:
        print("false")


