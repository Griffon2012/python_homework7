def new_contact() -> list:
    contact_data = []
    contact_data.append(input('Введите имя: '))
    contact_data.append(input('Введите номер телефона: '))
    contact_data.append(input('Введите комментарий: '))
    return contact_data


def view_main_menu() -> str:
    print('1. Показать контакты: ')
    print('2. Добавить новый контакт: ')
    print('3. Поиск: ')
    print('4. Изменить: ')
    print('5. Удалить: ')
    print('6. Сохранить файл: ')
    print('7. Выход: ')

    choice = input('\nВаш выбор: ')
    return choice


def confirmation():
    print('\nДействие выполнено успешно\n')


def print_contacts(data):
    for number, contact in enumerate(data):
        print(
            f'id - {contact[0]} ФИО: {contact[1]} Телефон: {contact[2]} Примечание: {contact[3]}')


def search_contacts() -> str:
    return input('Введите критерии поиска: ')


def delete_contact():
    return int(input('Введите id контакта для удаления: '))


def update_contact():
    return int(input('Введите id контакта для изменения: '))
