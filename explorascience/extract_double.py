import json

inputPath1 = r"Includes/tictactoe.json"
outPath1 = r"Includes/tttPStart.json"
inputPath2 = r"Includes/tictactoe2.json"
outPath2 = r"Includes/tttIA.json"


def extract():
    with open(inputPath1, "r") as file:
        json_data1 = json.load(file)
    file.close()

    with open(inputPath2, "r") as file:
        json_data2 = json.load(file)
    file.close()

    json_data_unique1 = remove_duplicates(json_data1)
    json_data_unique2 = remove_duplicates(json_data2)

    with open(outPath1, "w") as file:
        json.dump(json_data_unique1, file, indent=2)
    file.close()

    with open(outPath2, "w") as file:
        json.dump(json_data_unique2, file, indent=2)
    file.close()


def remove_duplicates(data):
    unique_tables = []
    unique_data = []
    for obj in data:
        table = obj["table"]
        if table not in unique_tables:
            unique_tables.append(table)
            unique_data.append(obj)
    return unique_data