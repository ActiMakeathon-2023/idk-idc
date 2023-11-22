from xlsx_reader import xls_read_gen
from masterdocx_reader import read_word_document_gen
from openai_faults_cmp import faults_cmp

# returns 3 lists: missing faults and presented faults and not matching faults
# missing will be in the format as in XLSX presented in format as in DOCX
# not matching will contain 3 elements: number, xlsx_name, docx_name
def faults_parser(xls_path, master_word_path):
    missing_faults = []
    presented_faults = []
    not_matching_faults = []
    for xlsx_number, xlsx_name in xls_read_gen(xls_path):
        is_present = 0
        for master_number, master_name in read_word_document_gen(master_word_path):
            if xlsx_number == master_number:
                is_present = 1
                if faults_cmp(xlsx_name, master_name):
                    presented_faults.append((master_number, master_name))
                else:
                    not_matching_faults.append((xlsx_number, xlsx_name, master_name))
        if not is_present:
            missing_faults.append((xlsx_number, xlsx_name))
        print("Missing:", missing_faults, "Presented:", presented_faults, "Not matching:", not_matching_faults, sep='\n')
        print()
    return missing_faults, presented_faults, not_matching_faults

# usage example
if __name__ == "__main__":
    missing_faults, presented_faults, not_matching_faults = faults_parser("faults.xlsx", "master.docx")
    print("Missing:", missing_faults, "Presented:", presented_faults, "Not matching:", not_matching_faults, sep='\n')
