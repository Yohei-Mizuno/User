class User:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


if __name__ == '__main__':
    ross = User('Ross', 30, 'paleontologist')
    print(ross)
    print(ross.name)
    print(ross.age)
    print(ross.occupation)

    joey = User('Joey', 31, 'actor')
    print(joey)
    print(joey.name)
    print(joey.age)
    print(joey.occupation)

    chandler = User('Chandler', 31, '???')
    print(chandler)
    print(chandler.name)
    print(chandler.age)
    print(chandler.occupation)





