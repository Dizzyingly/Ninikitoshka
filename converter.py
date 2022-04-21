import pickle


class PeopleTel:
    def __init__(self, numberroom, lastName, firstName, patronymic, telephone):
        self.numberroom = numberroom
        self.firstName = firstName
        self.lastName = lastName
        self.patronymic = patronymic
        self.telephone = telephone


with open('Пробный.txt', 'r', encoding='UTF8') as f:
    arr = f.readlines()

peopleArr = []
for i in arr:
    peopleArr.append(PeopleTel(*i.split(maxsplit=4)))

with open('Пробный.dat', 'wb') as f:
    pickle.dump(peopleArr, f)