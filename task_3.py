from pprint import pprint


DOCUMENTS = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        # {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        {"type": "insurance", "number": "10006"}
      ]

DIRECTORIES = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


def get_doc_info(number):
    for doc in DOCUMENTS:
        if doc['number'] == number:
            return doc

    return None


def command_help():
    print('p - people - по номеру документа вывести его владельца\n'
          'l - list - вывести всю доступную информацию по документам\n'
          's - shelf -  по номеру документа вывести полку, на которой он находится\n'
          'a - add - добавление нового документа в каталог и на полку\n'
          'd - delete - полное удаление документа по его номеру\n'
          'm - move - перемещение документа на новую полку\n'
          'as - add shelf - добавление нового документа\n'
          'ls - list shelf - вывод перечня полок\n'
          'n - name - вывод имен всёх владельцев\n'
          'q - quit - выход из программы')


def get_doc_owner():
    doc_number = input('\tВведите номер документа: ')
    doc_info = get_doc_info(doc_number)
    if get_doc_info(doc_number) is None:
        print('\tДокумента с таким номер в базе не найдено!')
    else:
        print(f'\t{doc_info["name"]}')


def list_all_docs():
    for doc in DOCUMENTS:
        output_str = '\t'
        for parametr in doc.values():
            output_str += parametr + ' '
        print(output_str)


def get_doc_location():
    doc_number = input('\tВведите номер документа: ')
    for shelf in DIRECTORIES:
        if doc_number in DIRECTORIES[shelf]:
            print(f'\t{shelf}')
            return

    print('\tДокумента с таким номером не найдено!')


def add_new_doc():
    print('\tДля добавления нового документа укажите следующие параметры:')
    doc_number = input('\tномер документа: ')
    while get_doc_info(doc_number) is not None:
        print('\t\tДокумент с таким номером уже существует!')
        substitute_flag = input('\t\tЗаменить на новый (y/n)? ').lower()
        if substitute_flag == 'n':
            doc_number = input('\t\tвведите другой номер документа: ')
        else:
            break

    doc_type = input('\tтип документа: ')
    owner_name = input('\tимя владельца: ')
    shelf_number = input('\tномер полки, на которую документ будет помещен: ')
    while shelf_number not in DIRECTORIES.keys():
        print('\t\tТакой полки не найдено!')
        shelf_add_flag = input('\t\tДобавить полку в учет (y/n)? ').lower()
        if shelf_add_flag == 'n':
            shelf_number = input('\t\tвведите номер полки заново: ')
        else:
            DIRECTORIES[shelf_number] = list()
            break

    DOCUMENTS.append({"type": doc_type, "number": doc_number, "name": owner_name})
    DIRECTORIES[shelf_number].append(doc_number)


def delete_doc():
    doc_number = input('\tВведите номер документа: ')
    doc_info = get_doc_info(doc_number)
    if doc_info is None:
        print('\tДокумента с указанным номером в базе не найдено!')
    else:
        DOCUMENTS.remove(doc_info)
        for shelf in DIRECTORIES:
            if doc_number in DIRECTORIES[shelf]:
                doc_shelf = shelf
                break
        DIRECTORIES[doc_shelf].remove(doc_number)


def change_doc_location():
    doc_number = input('\tВведите номер документа: ')
    for shelf in DIRECTORIES:
        if doc_number in DIRECTORIES[shelf]:
            DIRECTORIES[shelf].remove(doc_number)
            shelf_number = input('\tУкажите номер целевой полки: ')
            if shelf_number not in DIRECTORIES.keys():
                new_shelf_flag = input('\tУказанная полка не подучетна. Добавить (y/n)? ')
                if new_shelf_flag == 'y':
                    DIRECTORIES[shelf_number] = [doc_number]
                else:
                    return
            else:
                DIRECTORIES[shelf_number].append(doc_number)
            return

    print('\tУказанного документа не найдено в системе хранения!')


def add_shelf():
    shelf_number = input('\tВведите номер новой полки: ')
    if shelf_number in DIRECTORIES.keys():
        print('\tПолка с таким номером уже существует!')
    else:
        DIRECTORIES[shelf_number] = list()


def list_all_shelfs():
    pprint(DIRECTORIES)


def get_all_owners():
    owners = list()
    for doc in DOCUMENTS:
        try:
            owners.append(doc['name'])
        except KeyError:
            print(f'Документ {doc["number"]}: владелец не указан')

    print(owners)


if __name__ == '__main__':
    command = input('Введите команду (h - для вывода доступного списка команд): ')
    while not command == 'q':
        if command == 'h':
            command_help()
        elif command == 'p':
            get_doc_owner()
        elif command == 'l':
            list_all_docs()
        elif command == 's':
            get_doc_location()
        elif command == 'a':
            add_new_doc()
        elif command == 'd':
            delete_doc()
        elif command == 'm':
            change_doc_location()
        elif command == 'as':
            add_shelf()
        elif command == 'ls':
            list_all_shelfs()
        elif command == 'n':
            get_all_owners()
        elif command == 'q':
            break

        command = input('Введите команду (h - для вывода доступного списка команд): ')
