path = r'./notebook.txt'


def get_data_from_file() -> list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(
            map(lambda string: string.strip().split(';'), file.readlines()))

    return data


def add_new_contact(notebook_data: list, contact_data: list):
    contact_data.insert(0, get_last_id_contact(notebook_data))
    notebook_data.append(contact_data)


def save_notebook_file(notebook_data):
    global path
    notebook_data_for_string = list(
        map(lambda data: ';'.join(data), notebook_data))
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(notebook_data_for_string))


def search_contacts(string_for_search, notebook_data) -> list:
    search_result = []
    for record in notebook_data:
        for number, value in enumerate(record):
            if number != 0 and (string_for_search in value):
                search_result.append(record)
                break
    return search_result


def delete_contact(number, notebook_data):
    for i, record in enumerate(notebook_data):
        if int(record[0]) == number:
            notebook_data.pop(i)
            break


def get_last_id_contact(notebook_data) -> str:
    last_id = 0
    if len(notebook_data) > 0:
        last_id = int(notebook_data[len(notebook_data)-1][0]) + 1

    return str(last_id)


def update_contact(id, new_data, notebook_data):
    for i, record in enumerate(notebook_data):
        if int(record[0]) == id:
            new_data.insert(0, str(id))
            notebook_data[i] = new_data
            break
