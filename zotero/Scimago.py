import requests
from lxml import etree
import re

class Scimago:
    def __init__(self, journal_name):
        self.journal_name = journal_name
        self.url = 'https://www.scimagojr.com/journalsearch.php'
        self.ranking, self.impact_factor =  self.FindRanking()
    

    def FindRanking(self):
        payload = {
            'q': self.journal_id,
            'tip': 'sid',
            'clean': 0
        }

        rs = requests.get(url=self.url, params=payload).text
        tree = etree.HTML(rs)

        journal_rank_list = tree.xpath('//div[@class="cellslide"]/table/tbody/tr[last()]/td[last()]/text()')
        
        return journal_rank_list[0], journal_rank_list[3]


    @property
    def journal_id(self):
        payload = {
            'q': self.journal_name 
        }

        rs = requests.get(url=self.url, params=payload)
        tree = etree.HTML(rs.text)

        journal_ref = tree.xpath('//div[@class="search_results"]/a/@href')[0]
        journal_id = re.search(r'q=(\d+)&', journal_ref).group(1)
        return journal_id



if __name__ == '__main__':
    journal_name = 'Food Reviews International'

    sci = Scimago(journal_name)