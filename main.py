from chartbuilder import ChartBuilder


if __name__ == '__main__':
    x = ChartBuilder('BTC')
    x.build_line('linear', sy=2019, sm=1, sd=1, ey=2022, em=1, ed=1)
    # x.build_ohlc('linear')
    print('done')