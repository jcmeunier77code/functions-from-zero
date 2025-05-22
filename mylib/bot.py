import wikipedia

def scrape(name="Microsoft", lenght=1):
    """
    Scrape the first sentence of a Wikipedia page.
    :param name: The name of the Wikipedia page to scrape.
    :param lenght: The number of sentences to scrape.
    :return: The first sentence of the Wikipedia page.
    """
    wikipedia.set_lang("fr")
    result = wikipedia.summary(name, sentences=lenght)
    return result
    

