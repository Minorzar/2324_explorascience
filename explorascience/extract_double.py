import json

inputPath = r"Includes/tictactoe.json"
outPath = r"Includes/tttPStart.json"


def remove_duplicates(data):
    unique_tables = []
    unique_data = []
    for obj in data:
        table = obj["table"]
        if table not in unique_tables:
            unique_tables.append(table)
            unique_data.append(obj)
    return unique_data


with open(inputPath, "r") as file:
    json_data = json.load(file)

json_data_unique = remove_duplicates(json_data)

with open(outPath, "w") as file:
    json.dump(json_data_unique, file, indent=2)