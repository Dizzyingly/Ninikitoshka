import pickle


class PeopleTel:
    def __init__(self, numberroom, lastName, firstName, patronymic, telephone):
        self.numberroom = numberroom
        self.firstName = firstName
        self.lastName = lastName
        self.patronymic = patronymic
        self.telephone = telephone

with open('Пробный.dat', 'rb') as f:
    Telefonists = pickle.load(f)


while True:
    print('Local Telephone Station:')
    for i in range(len(Telefonists)):
        print(str(i + 1) + ') ',
              Telefonists[i].numberroom,
              Telefonists[i].lastName,
              Telefonists[i].firstName,
              Telefonists[i].patronymic,
              Telefonists[i].telephone, end='')
    print()
    command = input('command (write help to see list of commands): ')
    if command == 'help':
        print('1 — поиск помещения по номеру телефона',
              '2 — поиск телефона по номеру помещения',
              '3 - поиск телефона и номера помещения по его фамилии',
              '4 — внести изменение',
              '5 — удалить запись',
              '6 - добавить запись',
              '(press enter)',
              sep='\n')
        print()
    elif command == '1':
        Flag = False
        telePhone = input('Введите номер телефона данного предприятия: ')
        for i in Telefonists:
            if i.telephone.strip() == telePhone:
                Flag = True
                print('Номер помещения: ', i.numberroom)
        if not Flag:
            print('Такого номера телефона нет!')


    elif command == '2':
        Fl = False
        Numberroom = input('Введите номер помещения данного предприятия: ')
        for i in Telefonists:
            if i.numberroom.strip() == Numberroom:
                if not Fl:
                    print('Номера телефонов рабочих в данном помещении: ', i.telephone.strip(), end='  ')
                    print()
                else:
                    print(i.telephone, end='  ')
                    print()
                Fl = True
        if not Fl:
            print('Такого номера помещения нет')
            print()

    elif command == '3':
        Flah = False
        lastname = input('Введите фамилию рабочего данного предприятия: ')
        for i in Telefonists:
            if i.lastName.strip() == lastname:
                Flah = True
                print('Номер и комната рабочего: ',i.telephone.strip(), i.numberroom)
        if not Flah:
            print('Такого рабочего на предприятии нет')

    elif command == '4':
        firstName = input('имя рабочего для изменения: ')
        for i in Telefonists:
            if i.firstName == firstName:
                print(i.lastName, i.firstName, i.patronymic)
                x = input('Новое имя (enter to skip): ')
                if x: i.firstName = x
                x = input('Фамилия (enter to skip): ')
                if x: i.lastName = x
                x = input('Отчество (enter to skip): ')
                if x: i.patronymic = x
                x = input('Номер помещения (enter to skip): ')
                if x: i.numberroom = x
                x = input('Номер телефона (enter to skip): ')
                if x: i.telephone = x
                print()

    elif command == '5':
        firstName = input('имя рабочего для удаления из базы: ')
        for i in range(len(Telefonists)):
            if Telefonists[i].firstName == firstName:
                if input('вы уверены, что хотите удалить' + ' '
                         + Telefonists[i].firstName + ' '
                         + Telefonists[i].lastName + '?' + ' (yes/no): ') == 'yes':
                    Telefonists.pop(i)
                    break

    elif command == '6':
        s = input("добавление записи(номер помещения фамилия имя отчество телефон): ")
        if len(s.split())>4:
            Telefonists.append(PeopleTel(*s.split(maxsplit=4)))
            print("запись добавлена")
        else: print('error')

    else:
        print('|———————————————————————Stopped———————————————————————|')
        break
    print()

with open('Пробный.dat', 'wb') as f:
    pickle.dump(Telefonists, f)