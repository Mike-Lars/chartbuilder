import requests
import json
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import datetime

from utils import datetime_object_builder


API_KEY = ''


class ChartBuilder:
    def __init__(self, symbol):
        self.symbol = symbol
        r = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_ohlc', params={'a': self.symbol, 'api_key': API_KEY})
        json = r.json()

        self.df = pd.json_normalize(json, sep='_')
        self.df['t'] = pd.to_datetime(self.df['t'], unit='s')
        self.df = self.df.rename({'t': 'date', 'o_c': 'close', 'o_h': 'high', 'o_l': 'low', 'o_o': 'open'}, axis=1)
        self.df = self.df[['date', 'open', 'high', 'low', 'close']]
        self.df['open_log10'] = numpy.log10(self.df['open'])
        self.df['high_log10'] = numpy.log10(self.df['high'])
        self.df['low_log10'] = numpy.log10(self.df['low'])
        self.df['close_log10'] = numpy.log10(self.df['close'])
        print(self.df)
        
    def build_line(self, linearlog, sy=None, sm=None, sd=None, ey=None, em=None, ed=None, savechart=False):
        s_obj, e_obj = datetime_object_builder(self.df, sy, sm, sd, ey, em, ed)
            
        plt.rcParams['figure.figsize'] = (15, 9)
        plt.plot(self.df.date, self.df.close, color='black')
        plt.xlim(s_obj, e_obj)
        plt.grid(b=True, which='both', axis='both')
        if linearlog == 'linear':
            plt.ylim(0, self.df['close'].max() * 1.7)
            plt.grid(b=True, which='both', axis='both')
            plt.title(self.symbol)
            plt.ylabel('USD') 
        elif linearlog == 'log':
            plt.ylim(self.df['close'].min(), 10**6)
            plt.yscale('log')
            plt.title(self.symbol)
            plt.ylabel('USD (log10)')
        fig = plt.gcf()
        plt.show()
        
        #if savechart:
            #fig.savefig(self.symbol + '_' + str(datetime.date.today()) + '.png')
    
    def build_ohlc(self, linearlog, savechart=False):
        if linearlog == 'linear':
            pass
        elif linearlog == 'log':
            pass
        
        if savechart:
            pass
