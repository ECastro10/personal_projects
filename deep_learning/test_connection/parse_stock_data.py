from stock_data import GoogleIntradayQuote


def get_percentage_change(startPoint, currentPoint):
    try:
        x = ((float(currentPoint) - startPoint) / abs(startPoint)) * 100.00

        if x == 0.0:
            return 0.000001
        else:
            return x

    except:
        return 0.000001


def apply_percentages(open_):
    percentage_list = []
    for i in range(0, len(open_)-1):
        temp_val = get_percentage_change(i, i+1)
        percentage_list.append(temp_val)

    return percentage_list


def get_one_day_data(symbol):
    one_day_data = GoogleIntradayQuote(symbol)
    return one_day_data.open_


def split_one_day_into_intervals(interval, percentage_list):
    # Finish this function, mess with intervals, try different symbols.
    interval_list = []
    for i in range(0, len(percentage_list), interval):
        interval_list.append(percentage_list[i])
    return interval_list

def main():
    test = get_one_day_data('AAPL')
    print(len(test))
    per = apply_percentages(test)
    print(len(per))
    split1 = split_one_day_into_intervals(5, per)
    print(split1)

main()

