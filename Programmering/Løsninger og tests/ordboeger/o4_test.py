from o4 import *

# Opgave 1
def test_count_by_currency():
    transfers = random_transfers(1000)
    res = count_by_currency(transfers)
    
    assert isinstance(res, dict), "Result should be a dictionary"
    assert count_by_currency([]) == {}

    for currency in res.keys():
        assert currency in CURRENCIES, f"Invalid currency: {currency}"

    for count in res.values():
        assert isinstance(count, int), "Count must be an integer"
        assert count > 0, "Count must be positive"

    assert sum(res.values()) == 1000, "Total counted transfers must equal generated transfers"

    for t in transfers[:10]:  # check first 10
        assert len(t) == 5, "Each transfer must be a 5-tuple"

        # Time must be in valid ISO format
        try:
            datetime.fromisoformat(t[0])
        except:
            assert False, f"Invalid timestamp format: {t[0]}"

        # Currency must be in list
        assert t[1] in CURRENCIES, f"Invalid currency: {t[1]}"

        # Amount must be in valid range
        assert 1 <= t[2] <= 10, f"Invalid amount: {t[2]}"

        # Sender & receiver must be in address list
        assert t[3] in ADDRESSES, f"Invalid sender: {t[3]}"
        assert t[4] in ADDRESSES, f"Invalid receiver: {t[4]}"

# Opgave 2
def test_count_by_date():
    transfers = random_transfers(1000)
    res = count_by_date(transfers)

    assert isinstance(res, dict), "Result should be a dictionary"

    for date in res.keys():
        assert len(date) == 10, f"Invalid date format length: {date}"
        assert date[4] == "-" and date[7] == "-", f"Invalid date format: {date}"
        try:
            datetime.fromisoformat(date)
        except:
            assert False, f"Date key is not valid ISO date: {date}"
    
    for count in res.values():
        assert isinstance(count, int), "Count should be an integer"
        assert count > 0, "Count must be positive"

    assert sum(res.values()) == 1000, "Total counted transfers must equal generated transfers"

    for t in transfers[:10]:
        assert len(t) == 5, "Each transfer must be a 5-tuple"

        try:
            datetime.fromisoformat(t[0])
        except:
            assert False, f"Invalid timestamp: {t[0]}"

        date = t[0][:10]
        try:
            datetime.fromisoformat(date)
        except:
            assert False, f"Invalid extracted date: {date}"

# Opgave 3
def test_sum_by_date_and_currency():
    transfers = random_transfers(1000)
    res = sum_by_date_and_currency(transfers)

    assert isinstance(res, dict), "Result should be a dictionary"

    for key in res.keys():
        assert isinstance(key, tuple), f"Key must be a tuple: {key}"
        assert len(key) == 2, f"Key tuple must have length 2: {key}"

        date, currency = key

        # Check date format
        assert len(date) == 10, f"Invalid date length: {date}"
        assert date[4] == "-" and date[7] == "-", f"Invalid date format: {date}"
        try:
            datetime.fromisoformat(date)
        except:
            assert False, f"Invalid ISO date: {date}"

        # Check currency validity
        assert currency in CURRENCIES, f"Invalid currency: {currency}"

    for amount_sum in res.values():
        assert isinstance(amount_sum, int), "Amount sum must be an integer"
        assert amount_sum > 0, "Amount sum must be positive"

    expected = {}
    for t in transfers:
        timestamp, currency, amount, _, _ = t
        date = timestamp[:10]
        key = (date, currency)

        if key not in expected:
            expected[key] = amount
        else:
            expected[key] += amount

    assert res == expected, "Result does not match manual recomputation"

    for t in transfers[:10]:
        assert len(t) == 5, "Each transfer must be a 5-tuple"

        # Check timestamp
        try:
            datetime.fromisoformat(t[0])
        except:
            assert False, f"Invalid timestamp: {t[0]}"

        # Check currency
        assert t[1] in CURRENCIES, f"Invalid currency: {t[1]}"

        # Check amount range
        assert 1 <= t[2] <= 10, f"Invalid amount: {t[2]}"

# Opgave 4
def test_active_timespan_by_address():
    transfers = random_transfers(1000)
    res = active_timespan_by_address(transfers)

    assert isinstance(res, dict), "Result should be a dictionary"

    for addr in res.keys():
        assert addr in ADDRESSES, f"Invalid address in result: {addr}"

    for value in res.values():
        assert isinstance(value, tuple), "Value must be a tuple"
        assert len(value) == 2, "Tuple must contain two timestamps"

        first, last = value

        # Both timestamps must be valid ISO datetime strings
        try:
            datetime.fromisoformat(first)
            datetime.fromisoformat(last)
        except:
            assert False, f"Invalid timestamp tuple: {value}"

    expected = {}

    for timestamp, _, _, sender, receiver in transfers:

        def update(addr):
            if addr not in expected:
                expected[addr] = (timestamp, timestamp)
            else:
                first, _ = expected[addr]
                expected[addr] = (first, timestamp)

        update(sender)
        update(receiver)

    assert res == expected, "Result does not match manual recomputation"

    for t in transfers[:10]:
        assert len(t) == 5, "Each transfer must be a 5-tuple"
        timestamp, currency, amount, sender, receiver = t

        try:
            datetime.fromisoformat(timestamp)
        except:
            assert False, f"Invalid timestamp: {timestamp}"

        assert currency in CURRENCIES
        assert 1 <= amount <= 10
        assert sender in ADDRESSES
        assert receiver in ADDRESSES

# Opgave 5
def test_net_inflow_by_address_and_currency():
    transfers = random_transfers(1000)
    res = net_inflow_by_address_and_currency(transfers)

    assert isinstance(res, dict), "Result should be a dictionary"

    for key in res.keys():
        assert isinstance(key, tuple), f"Key must be a tuple: {key}"
        assert len(key) == 2, f"Key must be (address, currency): {key}"

        address, currency = key

        # Address valid?
        assert address in ADDRESSES, f"Invalid address in key: {address}"

        # Currency valid?
        assert currency in CURRENCIES, f"Invalid currency in key: {currency}"
    
    for value in res.values():
        assert isinstance(value, int), f"Value must be an integer: {value}"

    expected = {}

    for _, currency, amount, sender, receiver in transfers:

        # Receiver: +amount
        recv_key = (receiver, currency)
        expected[recv_key] = expected.get(recv_key, 0) + amount

        # Sender: -amount
        send_key = (sender, currency)
        expected[send_key] = expected.get(send_key, 0) - amount

    assert res == expected, "Result does not match manual recomputation"
  
    for t in transfers[:10]:
        assert len(t) == 5, "Each transfer must be a 5-tuple"

        timestamp, currency, amount, sender, receiver = t

        # Timestamp valid?
        try:
            datetime.fromisoformat(timestamp)
        except:
            assert False, f"Invalid timestamp: {timestamp}"

        # Currency valid?
        assert currency in CURRENCIES

        # Amount valid?
        assert 1 <= amount <= 10

        # Address valid?
        assert sender in ADDRESSES
        assert receiver in ADDRESSES
