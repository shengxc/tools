import re
import argparse
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from xbsee_parser import XbseeParser
from ciligod_parser import CiligodParser
from hupo_parser import HupoParser
from ygdy8_parser import Ygdy8Parser

class DownloadParser:

    def __init__(self):
        self.argparser = argparse.ArgumentParser(description='从各个种子站分析电视剧下载链接')
        self.argparser.add_argument("-o", "--output", help="输出文件，不填则输出到标准输出")
        self.argparser.add_argument("-p", "--pattern", help="正则表达式")
        self.argparser.add_argument("url", help="网页链接")
        self.site_parser = {
            "www.xbsee.com": XbseeParser(),
            "www.ciligod.com": CiligodParser(),
            "www.clgod.top": CiligodParser(),
            "www.15po.com": HupoParser(),
            "www.ygdy8.com": Ygdy8Parser(),
        }

    def run(self):
        ns = self.argparser.parse_args()
        netloc = urlparse(ns.url).netloc
        page_parser = self.site_parser.get(netloc)
        if page_parser is None:
            raise Exception(f"没有[{netloc}]的解析器")
        result = page_parser.parse(self.download(ns.url))
        result = self.filter_by_pattern(result, ns.pattern)
        result = "\n".join(result)
        if ns.output is None:
            print(result)
        else:
            with open(ns.output, "w") as f:
                f.write(result)

    def download(self, url):
        ua='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        req=Request(url,headers={'User-agent':ua})
        return urlopen(req).read()

    def filter_by_pattern(self, data, pattern):
        result = []
        for name, url in data:
            if name is None or pattern is None or re.match(pattern, name) is not None:
                result.append(url)
        return result


if __name__ == "__main__":
    download_parser = DownloadParser()
    download_parser.run()
