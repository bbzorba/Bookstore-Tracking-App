from candidate import Candidate

class Employee(Candidate):
    #global variables
    company = 'D&R'
    counter = 0
    employee_list = []
    links = []

    def __init__(self,name_emp, age_emp, experience_emp, salary_emp):
        super().__init__(name_emp, age_emp, experience_emp)
        self.__salary = salary_emp
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
        new_employee_experience = candidate_instance._experience
        print('Creating employee from candidate:', new_employee_name)
        return cls(new_employee_name, new_employee_age, new_employee_experience, salary)

    @classmethod
    def add_employee(cls, emp_str):
        name, age, experience, salary = emp_str.split('-')
        cls.employee_list.append(cls(name, int(age), int(experience), float(salary)))
        return cls(name, int(age), int(experience), float(salary))

    @classmethod
    def list_employees(cls):
        print('There are', len(cls.employee_list), 'employees in', cls.company, ":")
        for emp in cls.employee_list:
            print(emp._name, "is", emp._age, "years old, has", emp._experience, "years of experience, and earns", emp._Employee__return_salary, "€")

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
        # Link mentor -> mentee on the mentor side
        self.links.append((mentee_instance, 'mentee'))
        # Link mentee -> mentor on the mentee side
        mentee_instance.links.append((self, 'mentor'))
        print(f"Added {mentee_instance._name} as a mentee to {self._name}.")
