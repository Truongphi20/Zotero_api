from .Auth import Auth
from zotero import items

class Collection:
    def __init__(self, zo_auth: Auth, colection_id: str):
        self.auth = zo_auth
        self.zot = zo_auth.zot
        self.colection_id = colection_id
        self.items_dict = self.zot.collection_items(colection_id)
        self._items = {}
        self.pdf_items, self.ref_items = self.FilterType()

    def DownloadPDFs(self):
        pass

    def FilterType(self):
        pdf_items = {}
        ref_items = {}
        for key, item in self.items.items():
            if item.type == 'pdf':
                pdf_items[item.key] = item
            elif item.type == 'ref':
                ref_items[item.key] = item
        return pdf_items, ref_items

    @property
    def items(self):
        if self._items == {}:
            for item in self.items_dict:
                key_item = item.get('key')
                title = item.get('data').get('title')
                if not title:
                    continue
                if title.endswith(".pdf"):
                    self._items[key_item] = items.PDFItem(item)
                elif len(title) > 0:
                    self._items[key_item] = items.RefItem(item)
        return self._items

        
