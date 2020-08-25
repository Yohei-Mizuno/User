class User:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def display_profile(self):
        print(f'名前(Name):{self.name}, 年齢(Age):{self.age}, 職業(Occupation):{self.occupation}')

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation



if __name__ == '__main__':
    ross = User('Ross', 30, 'paleontologist')
    ross.display_profile()

    joey = User('Joey', 31, 'actor')
    joey.display_profile()

    chandler = User('Chandler', 31, '???')
    chandler.display_profile()
    chandler.change_occupation('Statistical analysis')
    chandler.display_profile()





