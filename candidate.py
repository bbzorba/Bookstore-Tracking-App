class Candidate:
    candidate_list = []

    def __init__(self, name_cnd, age_cnd, experience_cnd):
        self._name = name_cnd
        self._age = age_cnd
        self._experience = experience_cnd
        self.links = []
    
    @classmethod
    def add_candidate(cls, emp_dict):
        candidate = Candidate(emp_dict['name'], emp_dict['age'], emp_dict['experience'])
        cls.candidate_list.append(candidate)
        return candidate
    
    @classmethod
    def list_candidates(cls):
        print('There are', len(cls.candidate_list), 'candidates:')
        for cand in cls.candidate_list:
            print(cand._name, "is", cand._age, "years old and has", cand._experience, "years of experience.")

    # Method to check eligibility based on experience
    def is_eligible(self, min_experience):
        return self._experience >= min_experience


# polymorphic method to show links
def show_links(instance):
    if not instance.links:
        print(f"{instance._name} has no links")
        return
    print(f"Links for {instance._name}:")
    for c, relation in instance.links:
        name = getattr(c, 'name', getattr(c, '_name', str(c)))
        print(f"- {relation} -> {name}")
