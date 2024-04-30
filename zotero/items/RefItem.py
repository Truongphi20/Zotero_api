from datetime import datetime
from ..Scimago import Scimago

class RefItem:
    def __init__(self, meta_dict):
        self.meta_dict = meta_dict
        self.type = 'ref'
        self.key = meta_dict['key']
        self.title = meta_dict.get('data').get('title')
        self.publication = meta_dict.get('data').get('publicationTitle')

        date = meta_dict.get('data').get('date')
        if date:
            self.year = date.split('-')[0]
        else:
            self.year = None

    def GetRank(self):
        try:
            scimago = Scimago(self.publication)
            ranking = scimago.ranking
            impact_factor = scimago.impact_factor
            return {'ranking': ranking, 'impact_factor': impact_factor}
        
        except IndexError:
            return {'ranking': None, 'impact_factor': None}
    

    def __repr__(self) -> str:
        return self.title