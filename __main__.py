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
    print()
    for item in ztr.Collection(auth, collection_id).items:
        print(item["key"], item.get("data").get("title"))
    auth.zot.dump("TRQNW5S6")
