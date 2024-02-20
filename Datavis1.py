import csv
import matplotlib.pyplot as mp

categories = []
years = []
values = []

with open('histcpi-CLEAN.csv', newline='') as file:
    reader = csv.reader(file)

    for row in reader:
        categories.append(row[0])

        year_values = []
        for value in row[1:]:
            try:
                year_values.append(float(value))

            except ValueError:
                year_values.append(None)
        years.append([int(year) for year in range(1974, 2023)])
        values.append(year_values)

mp.figure(figsize=(20, 12))

for i in range(len(categories)):
    filtered_values = [value for value in values[i] if value is not None]
    filtered_years = [str(year) for j, year in enumerate(range(1974, 2023)) if values[i][j] is not None]
    mp.bar(filtered_years, filtered_values, label=categories[i])    


mp.xlabel('Year')
mp.ylabel('CPI Values')
mp.title('CPI Values Over The Years')
mp.legend()


mp.show()

