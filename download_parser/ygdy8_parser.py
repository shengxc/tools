from base_parser import BaseParser
from bs4 import BeautifulSoup

class Ygdy8Parser(BaseParser):

    def parse(self, cont):
        soup = BeautifulSoup(cont, "html.parser")
        result = []
        for item in soup.find_all("td", bgcolor="#fdfddf"):
            a_item = item.find("a")
            result.append((a_item.text, a_item.attrs["href"]))
        return result
