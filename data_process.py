import pandas as pd


def data_process(df, col_do):
    ans = df[col_do].copy()
    ans.rename("data")
    return ans
