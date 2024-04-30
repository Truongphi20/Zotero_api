from pyzotero import zotero


class Auth:

    def __init__(self, user_id, api_key, library_type):
        self.user_id = user_id
        self.api_key = api_key
        self.library_type = library_type

        self.zot = zotero.Zotero(user_id, library_type, api_key)
