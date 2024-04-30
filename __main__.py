import zotero as ztr
import os

if __name__ == "__main__":
    API_KEY = os.environ["ZOTERO_API_KEY"]
    USER_ID = "13591208"
    library_type = "user"

    auth = ztr.Auth(user_id=USER_ID, api_key=API_KEY, library_type=library_type)

    collection_id = "5JFGIWPG"

    pdf_items = ztr.Collection(auth, collection_id).pdf_items
    ref_items = ztr.Collection(auth, collection_id).ref_items

    print(pdf_items['NSCJTNG2'])
    parrent_key = pdf_items['NSCJTNG2'].parrent_key
    print(ref_items[parrent_key].publication)
    print(ref_items[parrent_key].GetRank())
    print(ref_items[parrent_key].pubtype)

