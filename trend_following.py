## Moving average data exploration

import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
## quandl
import quandl
quandl.ApiConfig.api_key = "j2QGEgPyPhe-dGsNNtzE"


## load data

bbg_df = pd.read_csv("../Trend_Following/bbg_data_final.csv", header=[0,1], index_col=0)



dMA = pd.DataFrame({})

def MA(prices_dataframe):
    dMA = prices_dataframe.rolling(2).mean()
    def rename_df(df, current_index):
        for name in df.columns.values:
            df[name[0] + str(current_index)] = df[name]
        return df

    for i in range(3,200):
        MA = rename_df(prices_dataframe.rolling(i).mean(), i)
        dMA = pd.concat([dMA,MA])
    return dMA



bbgheader_list = [x for x in bbg_df.columns.values.tolist() if x[1]=='price']
bbg_df_price_only = bbg_df.filter(items= bbgheader_list)




MA_price = MA(bbg_df_price_only)




plt.plot(MA_price.filter(like='OLT'))
plt.show()
