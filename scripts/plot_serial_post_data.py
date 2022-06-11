#!/usr/bin/env python3

# script to plot data

import csv
import os


def main():
    pwd = os.getcwd()

    fast_all = []
    med_all = []
    slow_all = []

    gas_fast_dict = []
    gas_medium_dict = []
    gas_slow_dict = []

    with open(pwd + "/data/serial_post_36_1654626205_.csv") as csvfile:
        csvdata = csv.reader(csvfile)

        for row in csvdata:
            # print(row)
            rowindex = int(row[0])
            rowval = float(row[1])

            fast_all.append(rowval)

            gas_fast_dict.append((rowindex, rowval))

    # print(gas_fast_dict)

    with open(pwd + "/data/serial_post_30_1654626205_.csv") as csvfile:
        csvdata = csv.reader(csvfile)

        for row in csvdata:
            # print(row)
            rowindex = int(row[0])
            rowval = float(row[1])

            med_all.append(rowval)

            gas_medium_dict.append((rowindex, rowval))

    # print(gas_medium_dict)

    with open(pwd + "/data/serial_post_27_1654626205_.csv") as csvfile:
        csvdata = csv.reader(csvfile)

        for row in csvdata:
            # print(row)
            rowindex = int(row[0])
            rowval = float(row[1])

            slow_all.append(rowval)

            gas_slow_dict.append((rowindex, rowval))

    # print(gas_slow_dict)

    import statistics

    print(statistics.mean(fast_all), statistics.stdev(fast_all))

    print(statistics.mean(med_all), statistics.stdev(med_all))

    print(statistics.mean(slow_all), statistics.stdev(slow_all))

    # import matplotlib.pyplot as plt

    # plt.plot(*zip(*gas_fast_dict))
    # plt.plot(*zip(*gas_medium_dict))
    # plt.plot(*zip(*gas_slow_dict))

    # plt.ylabel("some numbers")
    # plt.show()


if __name__ == "__main__":
    main()
