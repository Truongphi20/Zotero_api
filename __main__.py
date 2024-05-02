import zotero as ztr
import os
import concurrent.futures

if __name__ == "__main__":
    API_KEY = "UylF74ppeBKaDiURNDr7bWZc"
    USER_ID = "14213612"
    library_type = "user"

    auth = ztr.Auth(user_id=USER_ID, api_key=API_KEY, library_type=library_type)

    collection_id = "4CKD8DP3"

    pdf_items = ztr.Collection(auth, collection_id).pdf_items
    ref_items = ztr.Collection(auth, collection_id).ref_items

    def Download(pdf_key, zot, ref_items):
        # sample_pdf = pdf_items["NSCJTNG2"]
        sample_pdf = pdf_items[pdf_key]
        sample_pdf.DownloadPDF(zot, ref_items, "out")

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # Start the load operations and mark each future with its download
        future_to_download = {
            executor.submit(Download, pdf_key, auth.zot, ref_items): pdf_key
            for pdf_key in pdf_items.keys()
        }
        for future in concurrent.futures.as_completed(future_to_download):
            pdf_key = future_to_download[future]
            try:
                future.result()
            except Exception as exc:
                print("Fail: ", pdf_items[pdf_key], pdf_key, exc)
            else:
                print("Success: ", pdf_items[pdf_key])
