class person:
    def __init__(self,name1, age1, income1):
        self.name = name1
        self.age = age1
        self.__income = income1

    def display(self):
        print('I am', self.name,'and I am', self.age,'years old')
    
    @property
    def __return_income(self):
        return self.__income

john = person('John',20,2500)
alice = person('Alice',21,2000)

john.display()
alice.display()

#print('Attributes of the john instance of person class: \n',dir(john))

#printing the private variable from a private method
print(john.name, 'earns', john._person__return_income, '€')
