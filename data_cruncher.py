import csv
import os

with open("./formatted_data.csv", "w") as output_file:
    file_writer = csv.writer(output_file)
    col_headers = ["sales", "date", "region"]
    file_writer.writerow(col_headers)

    for file in os.listdir("./data"):
        with open(f"./data/{file}", "r") as input_file:
            file_reader = csv.reader(input_file)
            row_index = 0
            for input_row in file_reader:
                if row_index > 0:
                    product = input_row[0]
                    if product == "pink morsel":
                        price = input_row[1]
                        quantity = input_row[2]
                        date = input_row[3]
                        region = input_row[4]
                        total_daily_price = float(price[1:]) * float(quantity)
                        output_row = [total_daily_price, date, region]
                        file_writer.writerow(output_row)
                row_index += 1