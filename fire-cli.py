import fire
from mylib.bot import scrape

# This script is a command line interface (CLI) for the scrape function.
# It allows users to scrape the first sentence of a Wikipedia page using command line arguments.
if __name__ == "__main__":
    fire.Fire(scrape)

# Usage in CLI:
# python fire-cli.py --name Microsoft --lenght 1
# python fire-cli.py --name Microsoft
# python fire-cli.py --name Microsoft --lenght 2
# python fire-cli.py --name Microsoft --lenght 3
