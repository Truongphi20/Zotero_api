import requests
from lxml import etree
import re

class Scimago:
    def __init__(self, journal_name):
        self.journal_name = journal_name
        self.url = 'https://www.scimagojr.com/journalsearch.php'
    
    @property
    def ranking(self):
        payload = {
            'q': self.journal_id,
            'tip': 'sid',
            'clean': 0
        }

        rs = requests.get(url=self.url, params=payload).text
        tree = etree.HTML(rs)

        journal_rank = tree.xpath('//div[@class="cellslide"]/table/tbody/tr[last()]/td[last()]/text()')[0]
        return journal_rank


    @property
    def journal_id(self):
        payload = {
            'q': journal_name 
        }

        rs = requests.get(url=self.url, params=payload).text
        tree = etree.HTML(rs)

        journal_ref = tree.xpath('//div[@class="search_results"]/a/@href')[0]
        journal_id = re.search(r'q=(\d+)&', journal_ref).group(1)
        return journal_id



if __name__ == '__main__':
    journal_name = 'Food Reviews International'

    sci = Scimago(journal_name)
    print(sci.ranking)