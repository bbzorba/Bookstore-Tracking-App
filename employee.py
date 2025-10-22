from candidate import Candidate

class Employee:
    #global variables
    company = 'D&R'
    counter = 0

    def __init__(self,name1, age1, salary1):
        self._name = name1
        self._age = age1
        self.__salary = salary1
        Employee.counter += 1
    
    @classmethod
    def from_candidate(cls, candidate_instance, salary):
        new_employee_name = candidate_instance.name
        new_employee_age = candidate_instance.age
        print('Creating employee from candidate:', new_employee_name)
        return cls(new_employee_name, new_employee_age, salary)

    @classmethod
    def total_employees(cls):
        print('There are', cls.counter, 'employees in', cls.company)

    @classmethod
    def obj_from_str(cls, emp_str):
        name, age, salary = emp_str.split('-')
        return cls(name, int(age), float(salary))

    @classmethod
    def obj_from_dict(cls, emp_dict):
        return cls(emp_dict['name'], emp_dict['age'], emp_dict['salary'])

    def display(self):
        print('I am', self._name, ', I work at', Employee.company, ', I am', self._age, 'years old')
    
    @property
    def get_name(self):
        return self._name

    @property
    def __return_salary(self):
        if self.__salary < 0:
            raise ValueError('Salary cannot be negative')
        return self.__salary

    @__return_salary.setter
    def __return_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = new_salary
    
    @__return_salary.deleter
    def __return_salary(self):
        print('Deleting salary...')
        del self.__salary


if __name__ == '__main__':

    john = Employee.obj_from_str('John-23-2500')
    alice = Employee.obj_from_dict({'name':'Alice', 'age':28, 'salary':2800})
    dennis_candidate = Candidate('Dennis', 30, 5)

    #associated with the class, not the instance
    Employee.total_employees()

    john.display()
    alice.display()

    #print('Attributes of the john instance of employee class: \n',dir(john))

    #printing the private variable from a private method
    print(john._name, 'earns', john._Employee__return_salary, '€')

    #modifying the private variable from a private method
    john._Employee__return_salary = 3000
    print(john._name, 'now earns', john._Employee__return_salary, '€')

    #deleting the private variable from a private method
    del john._Employee__return_salary

    #creating an employee from a candidate
    dennis = Employee.from_candidate(dennis_candidate, 3200)
    dennis.display()
    print(dennis._name, 'earns', dennis._Employee__return_salary, '€')