from .Auth import Auth
from zotero import items

class Collection:
    def __init__(self, zo_auth: Auth, colection_id: str):
        self.auth = zo_auth
        self.zot = zo_auth.zot
        self.colection_id = colection_id
        self.items_dict = self.zot.collection_items(colection_id)
        self.pdf_items, self.ref_items = self.FilterType()

    def FilterType(self):
        pdf_items = {}
        ref_items = {}
        
        for item in self.items_dict:
            key_item = item.get('key')
            title = item.get('data').get('title')
            if not title:
                continue
            if title.endswith(".pdf"):
                pdf_items[key_item] = items.PDFItem(item)
            elif len(title) > 0:
                ref_items[key_item] = items.RefItem(item)
        
        return pdf_items, ref_items

        
