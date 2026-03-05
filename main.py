from datetime import datetime

def odd_or_even_day(timestamp):
    # The timestamp is given in miliseconds and datetime fuctions use seconds. That's why we need to devide by 1000
    # utcfromtimestamp() function is precated, but is the one to use here because the only available
    dt = datetime.utcfromtimestamp(timestamp/1000)
    # This is the one we should use in next versions of python
    '''
    dt = datetime.fromtimestamp(timestamp/1000, tz=timezone.utc)
    '''
    return "even" if dt.day%2 == 0 else "odd"

if __name__ == '__main__':
    print(odd_or_even_day(1769472000000))
    print('==========')
    print(odd_or_even_day(1769444440000))
    print('==========')
    print(odd_or_even_day(6739456780000))
    print('==========')
    print(odd_or_even_day(1))
    print('==========')
    print(odd_or_even_day(86400000))