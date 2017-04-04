import urllib.request, time, datetime





class Quote(object):
    DATE_FMT = '%Y-%m-%d'
    TIME_FMT = '%H:%M:%S'

    def __init__(self):
        self.symbol = ''
        self.date, self.time, self.open_, self.high, self.low, self.close, self.volume = ([] for _ in range(7))


    def append(self, dt, open_, high, low, close, volume):
        self.date.append(dt.date())
        self.time.append(dt.time())
        self.open_.append(float(open_))
        self.high.append(float(high))
        self.low.append(float(low))
        self.close.append(float(close))
        self.volume.append(float(volume))


    def to_csv(self):
        return ''.join(['{0},{1},{2},{3:.2f},{4:2f},{5:2f},{6:2f},{7}\n'.format(
            self.symbol, self.date[bar].strftime('%Y-%m-%d'),
            self.time[bar].strftime('%H:%M:%S'), self.open_[bar],
            self.high[bar], self.low[bar], self.close[bar],
            self.volume[bar]) for bar in range(len(self.close))])


    def write_csv(self,filename):
        with open(filename, 'w') as f:
            f.write(self.to_csv())


    def read_csv(self,filename):
        self.symbol = ''
        self.date, self.time, self.open_, self.high, self.low, self.close, self.volume = ([] for _ in range(7))
        for line in open(filename, 'r'):
            symbol, ds, ts, open_, high, low, close, volume = line.rstrip().split(',')

            self.symbol = symbol

            dt = datetime.datetime.strptime(ds + ' ' + ts, self.DATE_FMT + ' ' + self.TIME_FMT)
            self.append(dt, open_, high, low, close, volume)

        return True


    def __repr__(self):
        return self.to_csv()



class GoogleIntradayQuote(Quote):

    def __init__(self, symbol, interval_seconds=60, numdays=1):

        super(GoogleIntradayQuote, self).__init__()
        self.symbol = symbol.upper()
        url_string = 'http://www.google.com/finance/getprices?q={0}'.format(self.symbol)
        url_string += '&i={0}&p={1}d&f=d,o,h,l,c,v'.format(interval_seconds, numdays)
        # included print statement to show what exactly the url string is.
        print(url_string)

        csv = urllib.request.urlopen(url_string).readlines()


        for bar in range(7, len(csv)):
            if csv[bar].decode('utf8').count(',') != 5:
                continue

            offset, close, high, low, open_, volume = csv[bar].decode('utf8').split(',')

            if offset[0] == 'a':
                day = float(offset[1:])
                offset = 0

            else:
                offset = float(offset)

            open_, high, low, close = [float(x) for x in [open_, high, low, close]]
            dt = datetime.datetime.fromtimestamp(day + (interval_seconds * offset))
            self.append(dt, open_, high, low, close, volume)


# q = GoogleIntradayQuote('SENSEX')
#
# # This code writes the file that will appear in the directory.
# q.write_csv('Sensex_try_1')
# print(q)
