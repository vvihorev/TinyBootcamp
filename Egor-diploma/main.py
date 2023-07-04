import csv


def read_data(filepath):
    rows = []
    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            rows.append(row)
    names = []
    ages = []
    for row in rows[1:]:
        names.append(row[0])
        ages.append(row[1])
    return names, ages


def main():
    names, ages = read_data('test.csv')
    print(names, ages)


if __name__ == "__main__":
    main()