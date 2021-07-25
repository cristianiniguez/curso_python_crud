import click


@click.group()
def clients():
    "Manages the clients lifecycle"
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    "Creates a new client"
    pass


@clients.command()
@click.pass_context
def read(ctx):
    "Reads all clients"
    pass


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
