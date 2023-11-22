from xlsx_reader import xls_read_gen
from masterdocx_reader import read_word_document_gen
from openai_faults_cmp import faults_cmp

# yields tuples: first element is the type (string): "missing" "presented" "not_matching"
# missing will be in format (number, xlsx_name)
# presented will be in format (number, xlsx_name, master_name)
# not matching will contain 3 elements: number, xlsx_name, docx_name
def faults_parser_gen(xls_path, master_word_path):
    for xlsx_number, xlsx_name in xls_read_gen(xls_path):
        is_present = 0
        for master_number, master_name in read_word_document_gen(master_word_path):
            if xlsx_number == master_number:
                is_present = 1
                if faults_cmp(xlsx_name, master_name):
                    yield ("presented", master_number, xlsx_name, master_name)
                else:
                    yield ("not_matching", xlsx_number, xlsx_name, master_name)
        if not is_present:
            yield ("missing", xlsx_number, xlsx_name)

# usage example
if __name__ == "__main__":
    for element in faults_parser_gen("faults.xlsx", "master.docx"):
        print(element)
