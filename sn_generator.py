import pandas as pd
import os


def open_file(path):
    try:
        df = pd.read_excel(path, header=None)
        return df
    except FileNotFoundError:
        print("File not found.")
        


def tail_12(text):  # simulates =RIGHT() function from Excel
    text = (str(text)).upper()
    if len(text) > 12:
        text = text[-12:]
    return text


def generate(path):
    df = open_file(path).sort_values(by=1)  # ordeno la tabla por codigo
    if(not os.path.exists('serialNumbers')):
        os.mkdir('serialNumbers')

    previous_row = next_row = df.iloc[0]
    previous_row[0] = tail_12(previous_row[0])
    total_rows = [previous_row]
    i = 1
    while i < df.shape[0]:
        while previous_row[1] == next_row[1] and i < df.shape[0]:
            next_row = df.iloc[i]
            if previous_row[1] == next_row[1]:
                if len(next_row[0]) > 12:
                    previous_row[0] = tail_12(previous_row[0])
                    next_row[0] = tail_12(next_row[0])
                total_rows.append(next_row)
            i += 1
        serial_number_path = f"Serial Numbers/{total_rows[0][1]}.csv"
        pd.DataFrame(total_rows).iloc[:][0].to_csv(serial_number_path, index=False, header=False)
        total_rows.clear()
        previous_row = next_row
        total_rows.append(previous_row)

