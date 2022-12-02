from base_parser import BaseParser
from bs4 import BeautifulSoup

class CiligodParser(BaseParser):

    def parse(self, cont):
        soup = BeautifulSoup(cont, "html.parser")
        result = []
        for item in soup.find_all("a", class_="af"):
            result.append((item.text, item.attrs["href"]))
        return result
