class PDFItem:
    def __init__(self, meta_dict):
        self.meta_dict = meta_dict
        self.type = 'pdf'
        self.key = meta_dict['key']
        self.title = meta_dict.get('data').get('title')
        self.parrent_key = meta_dict.get('data').get('parentItem')

    def __repr__(self) -> str:
        return self.title