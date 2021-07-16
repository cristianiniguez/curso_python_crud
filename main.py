clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients
    clients += client_name
    _add_comma()


def read_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


if __name__ == '__main__':
    read_clients()
    create_client('david')
    read_clients()
