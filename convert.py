import pandas as pd

def parse_brazilian_number(value):
    if pd.isna(value):
        return value
    if isinstance(value, (int, float)):
        return value

    s = str(value).strip()

    s = s.replace("R$", "").replace(" ", "")

    is_percent = "%" in s
    s = s.replace("%", "")

    s = s.replace(".", "").replace(",", ".")

    try:
        num = float(s)
    except ValueError:
        return value

    if is_percent:
        num /= 100.0

    return num

def convert_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    df = df.applymap(parse_brazilian_number)

    df.to_csv(output_file, index=False)

convert_csv("input.csv", "cleaned.csv")