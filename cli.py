# -*- coding: utf-8 -*-
import click
from checkmysql import MySQLConn

@click.group()
def cli():
    pass

@cli.command()
@click.option('--host', default='localhost', help='ip or domain', required=True)
@click.option('--user', default='root', help='username', required=True)
@click.option('--password', help='password', required=True)
@click.option('--db', default='sys', help='database name', required=True)
@click.option('--port', default='3306', type=int, help='port', required=True)

def check(host, user, password, db, port):
    '''
    Check base de donnee
    '''
    con = MySQLConn.create(host, user, password, db, int(port))
    res = con.test()
    click.secho('+----------------------+')
    click.secho('| MySQL test connexion |')
    click.secho('+----------------------+')
    click.secho(f'| host: {host}')
    click.secho(f'| port: {port}')
    if res == 'OK':
        click.secho('| state: '+ click.style("OK", bold=True, fg="green"))
    else:
        click.secho('| state: '+ click.style("KO", bold=True, fg="red"))
        click.secho(f'| error: {res}')
    click.secho('+----------------------+')

if __name__ == '__main__':
    cli()
