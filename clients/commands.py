import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    "Manages the clients lifecycle"
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client company')
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option('-p', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    "Creates a new client"
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def read(ctx):
    "Reads all clients"
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.read_clients()

    headers = ['ID', 'Name', 'Company', 'Email', 'Position']
    table = [
        [client['uid'], client['name'], client['company'], client['email'], client['position']]
        for client in clients
    ]

    click.echo(tabulate(table, headers=headers))


@clients.command()
@click.pass_context
def update(ctx, client_id):
    "Updates a client"
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_id):
    "Deletes a client"
    pass


all = clients
