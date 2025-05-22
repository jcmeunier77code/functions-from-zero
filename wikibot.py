import click
from mylib.bot import scrape


@click.command()
@click.option('--name', 
              help='Webpade we want to scrape.')
@click.option('--lenght', default=1,
              help='Number of sentences to scrape.')

def cli_scrape(name = 'Microsoft', lenght = 1):
    """
    Scrape the first sentence of a Wikipedia page.
    :param name: The name of the Wikipedia page to scrape.
    :param lenght: The number of sentences to scrape.
    :return: The first sentence of the Wikipedia page.
    """
    result = scrape(name, lenght=lenght)
    click.echo(click.style(f"{result}", bg='blue', fg='white', bold=True))


if __name__ == '__main__':
    cli_scrape()




print(cli_scrape("facebook"))
print(type(scrape("facebook")))
