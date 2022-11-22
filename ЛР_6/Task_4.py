import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(f, new_line="\n") -> list[dict]:
    spisok = []
    with open(INPUT_FILE, "r") as f:
        name = f.readline().strip(new_line).split(",")
        for line in f:
            line = line.strip(new_line).split(",")
            spisok.append(dict(zip(name, line)))
    return spisok

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
