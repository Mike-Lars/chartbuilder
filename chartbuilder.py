import requests
import pandas
import numpy
import matplotlib.pyplot as plt
import datetime


symbols = ['BTC', 'ETH']
API_KEY = '1weKMNY8IzaBh00jQZXZrYZFseS'


class ChartBuilder:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_data(self):
        self.r = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_close', params={'a': self.symbol, 'api_key': API_KEY})
        self.df = pandas.read_json(self.r.text, convert_dates=['t'])
        self.df['v_log10'] = numpy.log10(self.df['v'])
        #print(self.df)
    
    def build_plot(self):
        self.plt = plt
        self.plt.rcParams['figure.figsize'] = (20, 12)
        self.plt.plot(self.df.t, self.df.v, color='black')
        self.plt.yscale('log')
        self.plt.xlim(datetime.date(2010, 7, 17), datetime.date(2030, 12, 31))
        self.plt.ylim(10**-2, 10**6)
        self.plt.grid(b=True, which='both', axis='both')
        self.plt.title(self.symbol)
        self.plt.ylabel('Price (log10)')
        self.fig = self.plt.gcf()
        self.plt.show()
    
    def save_plot(self):
        self.fig.savefig('./desktop/' + self.symbol + '_' + str(datetime.date.today()) + '.png')

        
# main
for symbol in symbols:
    x = ChartBuilder(symbol)
    x.get_data()
    x.build_plot()
    x.save_plot()
    print(f'{symbol} chart saved.')
print('Done.')