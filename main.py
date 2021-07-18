import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@gmail.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@gmail.com',
        'position': 'Data Engineer',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already exists in the client\'s list')


def read_clients():
    global clients

    for id, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=id,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name, updated_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        _print_not_found()


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        _print_not_found()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI SALES')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]eade clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("What is the client name? ('exit' to exit) ")

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}? (exit to exit) '.format(field_name))
        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()

    return field


def _print_not_found():
    print('Client is not in client\'s list')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        read_clients()
    elif command == 'R':
        read_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        read_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        read_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
