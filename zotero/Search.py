from .Auth import Auth


class Search:
    def __init__(self, zo_auth: Auth, search_dict: dict):
        self.search_dict = search_dict
        self.auth = zo_auth
        self.zot = zo_auth.zot
        self.search = self.zot.saved_search(
            search_dict.get("name"), search_dict.get("conditions")
        )

        self.key = self.search["successful"]["0"]["key"]

    @property
    def results(self):
        rs = self.zot.searches()
        self.zot.delete_saved_search([self.key])
        return rs
