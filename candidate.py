class Candidate:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def show_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Experience: {self.experience} years')