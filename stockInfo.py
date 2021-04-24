import pandas as pd
import time
import requests
import yfinance as yf
import twstock


class stockInfo:

    @classmethod
    def getAllStockId(self, save_csv_to):
        link = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
        r = requests.get(link)
        data = pd.DataFrame(r.json())
        data.to_csv(save_csv_to, index=False, header=True)

    @classmethod
    def getAllStockInfoFromYahoo(self, read_csv_from):
        stock_list = pd.read_csv(read_csv_from)
        stock_list.columns = ['證券代號', '證券名稱', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
        historical_data = pd.DataFrame()

        for i in stock_list.index:
            stock_id = str(stock_list.loc[i, '證券代號']) + '.TW'
            stock_data = yf.Ticker(stock_id)
            df = stock_data.history(period="max")
            df['證券代號'] = stock_list.loc[i, '證券代號']
            historical_data = pd.concat([historical_data, df])
            time.sleep(20)

        historical_data.to_csv('./csv/all_stock_data_yahoo.csv')

    @classmethod
    def getStockInfoFromYahoo(self, stockId):
        stock_id = stockId + '.TW'
        stock_data = yf.Ticker(stock_id)
        df = stock_data.history(period="max")
        df['Stock ID'] = stockId
        historical_data = pd.DataFrame()
        historical_data = pd.concat([historical_data, df])
        historical_data.to_csv(f'./csv/{stockId}_stock_data_yahoo.csv')

    @classmethod
    def getStockInfoFromTwStock(self, stockId, year, month):
        stock = twstock.Stock(stockId)
        stock_data = stock.fetch_from(year=year, month=month)
        attributes = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transaction']
        df = pd.DataFrame(columns=attributes, data=stock_data)
        df.to_csv(f'./csv/{stockId}_stock_data_twstock.csv')