import pandas as pd
import matplotlib
import mplfinance as mpf


class chart:
    @classmethod
    def makeChart(self, read_csv_from, stock_id):
        df = pd.read_csv(read_csv_from, parse_dates=True,
                         index_col=0, infer_datetime_format=True)

        mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
        kwargs = dict(type='candle', mav=(5, 20, 60), volume=True, figratio=(10, 8),
                      figscale=0.75, title=stock_id, style=s)
        mpf.plot(df, **kwargs)
