from .Auth import Auth


class Collection:
    def __init__(self, zo_auth: Auth, colection_id: str):
        self.auth = zo_auth
        self.zot = zo_auth.zot
        self.colection_id = colection_id
        self.items = self.zot.collection_items(colection_id)
