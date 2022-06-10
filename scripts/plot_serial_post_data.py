#!/usr/bin/env python3


import csv
import os

import statistics

import numpy as np, scipy.stats as st

# import statsmodels.stats.api as sms


def main():
    pwd = os.getcwd()

    file_names = [
        "post_10.csv",
        "post_20.csv",
        "post_30.csv",
        "post_40.csv",
        "post_50.csv",
    ]

    for filename in file_names:
        gas_price = filename.split(".")[0].split("_")[1]
        data_all = []

        with open(pwd + "/data_remote/" + filename) as csvfile:
            csvdata = csv.reader(csvfile)

            for row in csvdata:
                # print(row)
                if len(row) == 0:
                    break
                elif len(row) == 1:
                    rowval = float(row[0])
                else:
                    # rowindex = int(row[0])
                    rowval = float(row[1])

                data_all.append(rowval)

                # gas_fast_dict.append((rowindex, rowval))

        # print(data_all)
        print("Gas price: {} gwei".format(gas_price))
        print("Num data points: {}".format(len(data_all)))
        print(
            "Mean: {}, stdev: {}".format(
                statistics.mean(data_all), statistics.stdev(data_all)
            )
        )

        print(
            "95% CI: {}".format(
                st.t.interval(
                    0.95,
                    len(data_all) - 1,
                    loc=np.mean(data_all),
                    scale=st.sem(data_all),
                )
            )
        )

        print()

        # print(sms.DescrStatsW(data_all).tconfint_mean())

    # fast_all = []
    # med_all = []
    # slow_all = []

    # gas_fast_dict = []
    # gas_medium_dict = []
    # gas_slow_dict = []

    # with open(pwd + "/data/serial_post_36_1654626205_.csv") as csvfile:
    #     csvdata = csv.reader(csvfile)

    #     for row in csvdata:
    #         # print(row)
    #         rowindex = int(row[0])
    #         rowval = float(row[1])

    #         fast_all.append(rowval)

    #         gas_fast_dict.append((rowindex, rowval))

    # # print(gas_fast_dict)

    # with open(pwd + "/data/serial_post_30_1654626205_.csv") as csvfile:
    #     csvdata = csv.reader(csvfile)

    #     for row in csvdata:
    #         # print(row)
    #         rowindex = int(row[0])
    #         rowval = float(row[1])

    #         med_all.append(rowval)

    #         gas_medium_dict.append((rowindex, rowval))

    # # print(gas_medium_dict)

    # with open(pwd + "/data/serial_post_27_1654626205_.csv") as csvfile:
    #     csvdata = csv.reader(csvfile)

    #     for row in csvdata:
    #         # print(row)
    #         rowindex = int(row[0])
    #         rowval = float(row[1])

    #         slow_all.append(rowval)

    #         gas_slow_dict.append((rowindex, rowval))

    # print(gas_slow_dict)

    # import statistics

    # print(statistics.mean(fast_all), statistics.stdev(fast_all))

    # print(statistics.mean(med_all), statistics.stdev(med_all))

    # print(statistics.mean(slow_all), statistics.stdev(slow_all))

    # import matplotlib.pyplot as plt

    # plt.plot(*zip(*gas_fast_dict))
    # plt.plot(*zip(*gas_medium_dict))
    # plt.plot(*zip(*gas_slow_dict))

    # plt.ylabel("some numbers")
    # plt.show()


if __name__ == "__main__":
    main()
