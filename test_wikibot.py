from wikibot import scrape


def test_scrape():
    """
    Test the scrape function.
    """
    # Test the scrape function
    result = scrape("Microsoft", 1)
    assert "Microsoft" in result
    assert type(result) == str
    assert len(result.split(".")) >= 1
