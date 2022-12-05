from base_parser import BaseParser
from bs4 import BeautifulSoup

class HupoParser(BaseParser):

    def parse(self, cont):
        soup = BeautifulSoup(cont, "html.parser")
        result = []
        for item in soup.find_all("li"):
            input_item = item.find("input", class_="down_url")
            strong_item = item.find("strong", class_="down_part_name")
            if input_item is None or strong_item is None:
                continue
            result.append((strong_item.text, input_item.attrs["value"]))
        return result
