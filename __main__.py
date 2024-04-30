import zotero as ztr
import os

if __name__ == "__main__":
    API_KEY = os.environ["API_KEY"]
    USER_ID = "13591208"
    library_type = "user"

    auth = ztr.Auth(user_id=USER_ID, api_key=API_KEY, library_type=library_type)

    # search = {
    #     "name": "title",
    #     "conditions": [
    #         {
    #             "condition": "title",
    #             "operator": "contains",
    #             "value": "Bioactive compounds and strategy processing for acerola: A review",
    #         },
    #     ],
    # }

    # print(ztr.Search(auth, search).results[1])

    collection_id = "5JFGIWPG"
    data_key = "TRQNW5S6"

    # print([a.get("key") for a in ztr.Collection(auth, collection_id).items])
    # for item in ztr.Collection(auth, collection_id).items:
    #     print(item.get('key'), item.get('data').get('contentType') ,item.get('data').get('title'))
        # if item["key"] == data_key:
        #     print(item)
    # auth.zot.dump("TRQNW5S6")

    pdf_items = ztr.Collection(auth, collection_id).pdf_items
    ref_items = ztr.Collection(auth, collection_id).ref_items

    print(pdf_items['NSCJTNG2'])
    parrent_key = pdf_items['NSCJTNG2'].parrent_key
    print(ref_items[parrent_key].publication)
    print(ref_items[parrent_key].GetRank())

