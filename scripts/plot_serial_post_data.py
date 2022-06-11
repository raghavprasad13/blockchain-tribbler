#!/usr/bin/env python3

# Script to get statistics from measured data


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


if __name__ == "__main__":
    main()
