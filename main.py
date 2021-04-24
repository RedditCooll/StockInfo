import stockInfo as si
import chart

if __name__ == '__main__':
    print('Hi StockInfo!')

    si.stockInfo.getStockInfoFromYahoo('2330')
    chart.chart.makeChart('./csv/2330_stock_data_yahoo.csv', '2330')

    # si.stockInfo.getStockInfoFromTwStock('2330', 2021, 4)

    # si.stockInfo.getAllStockId('./csv/stock_id.csv')
    # si.stockInfo.getAllStockInfoFromYahoo('./csv/stock_id.csv')
