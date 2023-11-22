import pandas as pd

# generator that yelds pairs of Number (int) and FaultName (str)
def xls_read_gen(file_path):
    data = pd.read_excel(file_path, skiprows=3)
    data = data.iloc[:, :2]
    for _, row in data.iterrows():
        yield row['No.'], row['Faults']

# usage example
if __name__ == "__main__":
    file_path = "faults.xlsx"
    for number, fault in xls_read_gen(file_path):
        print(f"Number: {number}, Fault: {fault}")
