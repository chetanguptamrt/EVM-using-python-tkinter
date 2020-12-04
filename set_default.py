import pickle

class Pass:
    def __init__(self,current_password='12345678'):
        self.current_password=current_password
class Participant:
    def __init__(self,parti_list=[],vote_list=[]):
        self.parti_list=parti_list
        self.vote_list=vote_list

def set_pass():
    with open('Assets\\pass.dat',mode='wb') as f:
        stu=Pass()
        pickle.dump(stu,f)

    with open('Assets\\participants.dat',mode='wb') as f:
        stu=Participant()
        pickle.dump(stu,f)

if __name__ == "__main__":
    set_pass()