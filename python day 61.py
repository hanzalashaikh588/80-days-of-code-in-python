#access modifiers in python
#access modifiers in python are not enforeced by python but is a public convention.
#1) public access modifiers(all functions in python are public access modifiers.)
class client:
    def __init__(self):
        self.name = "harry"

a = client()
print(a.name)
#2) private access modifiers do not mean they are inaccesible they just cannot be accesed directly,
#  (adding __ makes private access modifiers)
class client:
    def __init__(self):
        self.__name = "harry"

a = client()
#print(a.__name) # cannot be accessed directly.
print(a._client__name) #(name mangling)# can be accessed indirectly.
print(a.__dir__())
#3) protected access modifiers is used to describe a attribute of a class
# only to be used by its own class or subclass. (_)