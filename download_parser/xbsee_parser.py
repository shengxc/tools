from base_parser import BaseParser
from bs4 import BeautifulSoup

class XbseeParser(BaseParser):

    def parse(self, cont):
        soup = BeautifulSoup(cont, "html.parser")
        result = []
        for item in soup.find_all("li", attrs={"data-type": "magnet"}):
            result.append((None, item.find("input").attrs["value"]))
        return result
