import csv
import datetime


def make_csv(put_place):
    now = datetime.datetime.now()

    filename = './csv_file/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for place in put_place:
            writer.writerow(place)

    with open(filename) as f:
        print(f.read())