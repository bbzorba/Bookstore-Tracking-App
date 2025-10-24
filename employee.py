from candidate import Candidate

class Employee:
    #global variables
    company = 'D&R'
    counter = 0
    employee_list = []
    links = []

    def __init__(self,name1, age1, salary1):
        self._name = name1
        self._age = age1
        self.__salary = salary1
        # keep colleague links per instance (not shared across all employees)
        self.links = []
        Employee.counter += 1
    
    @classmethod
    def from_candidate(cls, candidate_instance, salary):
        # Ensure we received a Candidate instance and a numeric salary
        if not isinstance(candidate_instance, Candidate):
            raise TypeError("input must be an instance of Candidate.")
        if not isinstance(salary, (int, float)):
            raise TypeError("salary must be a number.")

        new_employee_name = candidate_instance._name
        new_employee_age = candidate_instance._age
        print('Creating employee from candidate:', new_employee_name)
        return cls(new_employee_name, new_employee_age, salary)

    @classmethod
    def add_employee(cls, emp_str):
        name, age, salary = emp_str.split('-')
        cls.employee_list.append(cls(name, int(age), float(salary)))
        return cls(name, int(age), float(salary))

    @classmethod
    def list_employees(cls):
        print('There are', len(cls.employee_list), 'employees in', cls.company, ":")
        for emp in cls.employee_list:
            print(emp._name, "is", emp._age, "years old, and earns", emp._Employee__return_salary, "€")

    @property
    def __return_salary(self):
        if self.__salary < 0:
            raise ValueError('Salary cannot be negative.')
        return self.__salary

    @__return_salary.setter
    def __return_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError('Salary cannot be negative.')
        self.__salary = new_salary
    
    @__return_salary.deleter
    def __return_salary(self):
        print('Deleting salary...')
        del self.__salary

    def add_mentee(self, mentee_instance):
        if not isinstance(mentee_instance, Candidate):
            raise TypeError("input to this function must be an instance of Candidate.")
        self.links.append((mentee_instance, 'mentee'))
        print(f"Added {mentee_instance._name} as a mentee to {self._name}.")
    
    def show_links(self):
        if not self.links:
            print(f"{self._name} has no linked colleagues.")
            return
        print(f"Linked colleagues for {self._name}:")
        for colleague, relation in self.links:
            # Support both Candidate (name) and Employee (_name), and fallback gracefully
            colleague_name = getattr(colleague, 'name', getattr(colleague, '_name', str(colleague)))
            print(f"{colleague_name} is the {relation} of {self._name}")

