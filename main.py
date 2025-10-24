from employee import Employee
from candidate import Candidate

if __name__ == '__main__':

    print('\n--- Employee and Candidate Management System ---\n')

    john_employee = Employee.add_employee('John-23-2500')
    alice_employee = Employee.add_employee('Alice-28-2800')
    dennis_candidate = Candidate.add_candidate({'name':'Dennis', 'age':30, 'experience':5})
    martha_candidate = Candidate.add_candidate({'name':'Martha', 'age':35, 'experience':10})

    #associated with the class, not the instance
    Employee.list_employees()
    print("\n")
    Candidate.list_candidates()

    # Link candidates with a meaningful relation
    john_employee.add_mentee(dennis_candidate)
    alice_employee.add_mentee(martha_candidate)
    
    print("\n")

    #print('Attributes of the john instance of employee class: \n',dir(john))

    #printing the private variable from a private method
    print(john_employee._name, 'earns', john_employee._Employee__return_salary, '€')

    #modifying the private variable from a private method
    john_employee._Employee__return_salary = 3000
    print(john_employee._name, 'now earns', john_employee._Employee__return_salary, '€')

    #deleting the private variable from a private method
    del john_employee._Employee__return_salary
    
    print("\n")

    #creating an employee from a candidate
    dennis_employee = Employee.from_candidate(dennis_candidate, 3200)
    print(dennis_employee._name, 'earns', dennis_employee._Employee__return_salary, '€\n')