import click
import requests

@click.group


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def helloo(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Helloo %s!' % name)

@click.command()
def view():
    url = "http://127.0.0.1:8000/view"  # 这里只有url，字符串格式
    res = requests.get(url)
    click.echo(res)


if __name__ == '__main__':
    hello()

print('111')