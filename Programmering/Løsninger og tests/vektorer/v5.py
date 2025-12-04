# Opgave 1 - Kumulativ sum
def cum_sum_of(v):
    result = []
    acc = 0.0
    i = 0
    n = len(v)
    while i < n:
        acc += v[i]
        result.append(acc)
        i += 1
    return result

# Opgave 2 - Kumulativ max
def cum_max_of(v):
    result = []          
    cur_max = None  
    for x in v:          
        if cur_max is None or x > cur_max:
            cur_max = x               
        result.append(cur_max)
    return result

# Opgave 3 - Kumulativ forenig af mængder
def cum_union_of(v):
    result = []
    if not v:
        return result
    
    cur_set = set(v[0])
    result.append(set(cur_set))

    i = 1
    n = len(v)
    while i < n:
        cur_set.update(v[i])
        result.append(set(cur_set))
        i += 1
    return result

# Opgave 4 - Mønstret og generisk helper
def make_cumulative(op, init):
    def cumulative(seq):
        if not seq:
            return []
        result = []
        acc = init
        i = 0
        n = len(seq)
        while i < n:
            acc = op(acc, seq[i])
            result.append(acc)
            i += 1
        return result
    return cumulative

# Opgave 5 - Kumulativt gennemsnit
def cum_avg_of(v):
    result = []
    if not v:
        return result
    
    acc = 0.0
    i = 0
    n = len(v)
    while i < n:
        acc += v[i]
        result.append(acc / (i + 1))
        i += 1
    return result

# Opgave 6 - Glidende gennemsnit med fast vindue (3)
def moving_avg_of(v, window=3):
    result = []
    n = len(v)
    i = 0
    while i < n:       
        start = max(0, i - window + 1)        
        total = 0.0
        j = start
        while j <= i:
            total += v[j]
            j += 1
        count = i - start + 1 
        result.append(total / count)
        i += 1
    return result

# Opgave 7 - ohlc
def daily_ohlc(trades):
    result = []
    if not trades:
        return result
    
    cur_date, _, cur_price = trades[0]
    open_price = cur_price
    high_price = cur_price
    low_price = cur_price
    close_price = cur_price

    i = 1
    n = len(trades)
    while i < n:
        date, _, price = trades[i]
        if date != cur_date:
            result.append((cur_date, open_price, high_price, low_price, close_price))
            cur_date = date
            open_price = price
            high_price = price
            low_price = price
            close_price = price
        else:
            if price > high_price:
                high_price = price
            if price < low_price:
                low_price = price
            close_price = price
        i += 1
    result.append((cur_date, open_price, high_price, low_price, close_price))
    return result