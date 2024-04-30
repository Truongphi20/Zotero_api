import pandas as pd
import pathlib

class Journal:
    def __init__(self, journal_name):
        current_path = str(pathlib.Path(__file__).parent.resolve())
        self.scopus_path = current_path + '/data/SCOPUS_March_2024.xlsx'
        self.scie_path = current_path + '/data/SCIE2023-December-19.xlsx'
        self.journal_name = journal_name

    def FindType(self):
        find_in_scopus = self.scopu_data[self.scopu_data['Title name'].apply(lambda x: x.upper()) == self.journal_name.upper()]
        if not find_in_scopus.empty:
            return "Scopus"
        
        find_in_scie = self.scie_data[self.scie_data['Journal title'].apply(lambda x: x.upper()) == self.journal_name.upper()]
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

    journal_name = "Food Science and Technology International"
    journal = Journal(journal_name)

    print(journal.FindType())
