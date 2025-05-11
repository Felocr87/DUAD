# Este programa lee e imprime un documento .csv

import csv


def read_csv_file(file_path):
    with open(file_path, 'r',newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)



read_csv_file('my_games_tab.csv')
