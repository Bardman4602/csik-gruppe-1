import random
from datetime import datetime, timedelta

# Hjælpefunktion
CURRENCIES = ['ETH', 'USDT', 'BNB', 'USDC', 'WBTC', 'LINK', 'BAT']
ADDRESSES   = ['a03f', 'b077', 'c0da', 'd084', 'e0fe', 'f052']

def random_transfers(n, start='2015-06-01', end=None):
    start_time = datetime.fromisoformat(start)
    end_time   = datetime.fromisoformat(end) if end else datetime.today()
    if end_time <= start_time:
        raise ValueError('start must be before end')
    seconds = int((end_time - start_time).total_seconds())

    result = []
    i = 0
    while i < n:
        time     = start_time + timedelta(seconds=random.randint(0, seconds))
        currency = random.choice(CURRENCIES)
        amount   = random.randint(1, 10)
        sender   = random.choice(ADDRESSES)
        receiver = random.choice(ADDRESSES)
        result.append((
            time.isoformat(timespec='seconds'),   # fjerner mikrosekunder for konsistens
            currency,
            amount,
            sender,
            receiver,
        ))
        i += 1
    return result

# Opgave 1 - Antal overførsler pr. currency
def count_by_currency(transfers):    
    d = {}
    i = 0
    n = len(transfers)
    while i < n:
        _, currency, _, _, _ = transfers[i]
        if currency not in d:
            d[currency] = 1
        else:
            d[currency] += 1
        i += 1
    return d


# Opgave 2 - count by date
def count_by_date(transfers):
    d = {}
    i = 0
    n = len(transfers)
    while i < n:
        timestamp, _, _, _, _ = transfers[i]
        date = timestamp[:10]
        if date not in d:
            d[date] = 1
        else:
            d[date] += 1
        i += 1
    return d

# Opgave 3 - sum by date and currency
def sum_by_date_and_currency(transfers):
    d = {}
    i = 0
    n = len(transfers)
    while i < n:
        timestamp, currency, amount, _, _ = transfers[i]
        date = timestamp[:10]
        key = (date, currency)
        if key not in d:
            d[key] = amount
        else:
            d[key] += amount
        i += 1
    return d

# Opgave 4 - active timespan by address
def active_timespan_by_address(transfers):
    d = {}
    i = 0
    n = len(transfers)
    while i < n:
        timestamp, _, _, sender, receiver = transfers[i]
       
        def update(addr):
            if addr not in d:
                d[addr] = (timestamp, timestamp)   # første og sidste er samme nu
            else:
                first, _ = d[addr]
                d[addr] = (first, timestamp)        # kun 'last' opdateres

        update(sender)
        update(receiver)
        i += 1
    return d

# Opgave 5 - tilvækst pr addresse og currency
def net_inflow_by_address_and_currency(transfers):
    d = {}
    i = 0
    n = len(transfers)
    while i < n:
        _, currency, amount, sender, receiver = transfers[i]

        # Modtager får +amount
        recv_key = (receiver, currency)
        d[recv_key] = d.get(recv_key, 0) + amount

        # Afsender mister -amount
        send_key = (sender, currency)
        d[send_key] = d.get(send_key, 0) - amount

        i += 1
    return d