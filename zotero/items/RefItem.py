class RefItem:
    def __init__(self, meta_dict):
        self.meta_dict = meta_dict
        self.type = 'ref'
        self.key = meta_dict['key']
        self.title = meta_dict.get('data').get('title')
        self.date = meta_dict.get('data').get('date')

    def __repr__(self) -> str:
        return self.title