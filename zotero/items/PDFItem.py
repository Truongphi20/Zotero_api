from pyzotero import zotero


class PDFItem:
    def __init__(self, meta_dict):
        self.meta_dict = meta_dict
        self.type = "pdf"
        self.key = meta_dict["key"]
        self.title = meta_dict.get("data").get("title")
        self.parrent_key = meta_dict.get("data").get("parentItem")

    def DownloadPDF(self, zot: zotero.Zotero, ref_items: dict, outdir=".") -> None:
        parrent_key = self.parrent_key
        parrent = ref_items[parrent_key]

        rank_dict = parrent.GetRank()
        ranking = rank_dict["ranking"]
        impact_factor = str(rank_dict["impact_factor"])
        pubtype = parrent.pubtype
        year = parrent.year
        title = parrent.title.replace(" ", "_")

        file_name = f"{title}-{year}-{pubtype}-{ranking}-IF{impact_factor}.pdf"
        zot.dump(self.key, file_name, outdir)

    def __repr__(self) -> str:
        return self.title
