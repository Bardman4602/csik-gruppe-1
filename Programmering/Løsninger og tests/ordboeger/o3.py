# Indlæs csv filer
from o2 import read_csv

# Opgave 1 - Login count by username
def login_count_by_username(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        _, _, username, _ = auth[i]
        if username not in d:
            d[username] = 1
        else:
            d[username] += 1
        i += 1
    return d

# Opgave 2 - Login dates by username
def login_dates_by_username(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        _, timestamp, username, _ = auth[i]
        date = timestamp.split("T")[0]          # kun dato‑delen
        if username not in d:
            d[username] = []
        d[username].append(date)
        i += 1
    return d

# Opgave 3 - Failed logins by username
def failed_logins_by_username(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        entry = auth[i]
        _, _, username, result = entry
        if result != "failure":
            i += 1
            continue
        if username not in d:
            d[username] = []
        d[username].append(entry)
        i += 1
    return d

# Opgave 4 - active period by username
def active_period_by_username(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        _, ts, username, _ = auth[i]
        if username not in d:
            d[username] = (ts, ts)          # (first, last)
        else:
            first, _ = d[username]
            d[username] = (first, ts)       # kun 'last' opdateres
        i += 1
    return d

# Opgave 5 - stats by hostname
def stats_by_hostname(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        host, ts, _, _ = auth[i]
        if host not in d:
            d[host] = (ts, ts, 1)            # (first, last, count)
        else:
            first, _, cnt = d[host]
            d[host] = (first, ts, cnt + 1)
        i += 1

    result = [(host, first, last, cnt) for host, (first, last, cnt) in d.items()]
    result.sort(key=lambda x: x[0])            # sortér på hostname for stabilitet
    return result

# Opgave 6 - stats by hostname and username
def stats_by_hostname_and_username(auth):
    n = len(auth)
    d = {}
    i = 0
    while i < n:
        host, ts, user, _ = auth[i]
        key = (host, user)
        if key not in d:
            d[key] = (ts, ts, 1)              # (first, last, count)
        else:
            first, _, cnt = d[key]
            d[key] = (first, ts, cnt + 1)
        i += 1

    result = [
        (host, user, first, last, cnt)
        for (host, user), (first, last, cnt) in d.items()
    ]
    result.sort(key=lambda x: (x[0], x[1]))    # sortér på host, så user
    return result

# Wrapper
if __name__ == "__main__":
    # Læs data én gang
    former = read_csv("former_employees.csv")
    auth    = read_csv("auth_log.csv")
    employees = read_csv("employees.csv")
    hosts   = read_csv("hosts.csv")