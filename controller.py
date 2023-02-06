import model
import view

notebook_data = None


def start():
    global notebook_data
    if notebook_data == None:
        notebook_data = model.get_data_from_file()
    main_menu()


def add_new_contact():
    global notebook_data
    contact_data = view.new_contact()
    model.add_new_contact(notebook_data, contact_data)
    view.confirmation()


def search_contacts():
    global notebook_data
    string_for_search = view.search_contacts()
    search_contacts = model.search_contacts(string_for_search, notebook_data)
    view.print_contacts(search_contacts)


def main_menu():
    global notebook_data
    choice = view.view_main_menu()

    match choice:
        case '1':
            view.print_contacts(notebook_data)
        case '2':
            add_new_contact()
        case '3':
            search_contacts()
        case '4':
            id_contact = view.update_contact()
            new_data_contact = view.new_contact()
            model.update_contact(id_contact, new_data_contact, notebook_data)
        case '5':
            model.delete_contact(view.delete_contact(), notebook_data)
            view.confirmation()
        case '6':
            model.save_notebook_file(notebook_data)
            view.confirmation()
        case '7':
            exit()

    main_menu()
