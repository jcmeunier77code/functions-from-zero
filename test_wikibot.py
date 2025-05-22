from mylib.bot import scrape
from wikibot import cli_scrape
from click.testing import CliRunner

def test_scrape():
    """
    Test the scrape function.
    """
    # Test the scrape function
    result = scrape("Microsoft", 1)
    assert "Microsoft" in result
    assert type(result) == str
    assert len(result.split(".")) >= 1



def test_wikibot():
  runner = CliRunner()
  result = runner.invoke(cli_scrape, ['--name', 'Microsoft', '--lenght', '1'])
  assert result.exit_code == 0
  assert 'Microsoft' in result.output 