import pandas as pd

class Journal:
    def __init__(self, scopus_path, scie_path):
        self.scopus_path = scopus_path
        self.scie_path = scie_path

    def FindType(self, journal_name):
        find_in_scopus = self.scopu_data[self.scopu_data['Title name'].apply(lambda x: x.upper()) == journal_name.upper()]
        if not find_in_scopus.empty:
            return "Scopus"
        
        find_in_scie = self.scie_data[self.scie_data['Journal title'].apply(lambda x: x.upper()) == journal_name.upper()]
        if not find_in_scie.empty:
            return "SCIE"
        
        return None
        
    @property
    def scopu_data(self):
        return pd.read_excel(self.scopus_path, sheet_name='Accepted titles Feb. 2024', skiprows=2)
    
    @property
    def scie_data(self):
        return pd.read_excel(self.scie_path, skiprows=1)
    
if __name__ == "__main__":
    scopus_path = '/home/truongphi/Desktop/Zotero_api/data/SCOPUS_March_2024.xlsx'
    scie_path = '/home/truongphi/Desktop/Zotero_api/data/SCIE2023-December-19.xlsx'

    journal = Journal(scopus_path, scie_path)

    journal_name = "ACM TRANSACTIONS ON COMPUTATIONAL LOGIC"
    print(journal.FindType(journal_name))
