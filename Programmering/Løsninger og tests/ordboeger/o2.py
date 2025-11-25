# læs .csv filer
def read_csv(filename):
    import csv
    with open(filename, 'rt', encoding='utf-8', newline='\n') as file:
        return list(csv.reader(file))

# opgave 1 - indexering af former_employees på brugernavn
def username_index_of(v):
    n = len(v)
    d = {}
    i = 0
    while i < n:
        username = v[i][2]             
        if username in d:
            raise ValueError(f"Duplikat username: {username}")
        d[username] = v[i]
        i += 1
    return d

# Opgave 2 - post termination logins
def post_termination_logins_of(v, former_idx):
    n = len(v)
    res = []
    i = 0
    while i < n:
        row = v[i]
        username = row[2]
        if username in former_idx:
            termination_date = former_idx[username][3]
            timestamp = row[1]
            if timestamp > termination_date:
                res.append(row)
        i += 1
    return res

# Opgave 3
def employee_username_index_of(employees):
    return username_index_of(employees)

# Opgave 4
def hostname_index_of(hosts):
    n = len(hosts)
    d = {}
    i = 0
    while i < n:
        hostname = hosts[i][0]
        if hostname in d:
            raise ValueError(f"Duplikat hostname: {hostname}")
        d[hostname] = hosts[i]
        i += 1
    return d

# Opgave 5
def risk_score_of(log_row, employee_idx, host_idx):
    hostname = log_row[0]
    username = log_row[2]
    status_raw = log_row[3]
    status = status_raw.strip().lower() # "success" eller "failure"
    
    if username in employee_idx:
        employee_dept = employee_idx[username][3]

        host_entry = host_idx.get(hostname)
        if host_entry:                           # host findes i vores ordbog
            host_dept = host_entry[2]            # department i hosts‑tabellen

            if host_dept == employee_dept:            # samme afdeling
                return "green"

            # Forskellig afdeling
            if status == "failure":
                return "yellow"
            else:                               # status == "success"
                return "red"

        # Host‐oplysninger findes ikke → “øvrige” tilfælde
        if status == "failure":
            return "red"
        else:
            return "critical"

    # Ikke en nuværende medarbejder (eller brugernavn findes ikke)
    if status == "failure":
        return "red"
    else:
        return "critical"
    
# tester risk scores på hele auth loggen     
def risk_scores_of(auth_log, employee_idx, host_idx):
    return [risk_score_of(row, employee_idx, host_idx) for row in auth_log] 

# Opgave 6
def risk_summary_of(auth_log, employee_idx, host_idx):
    red_count = 0
    critical_count = 0
    first_critical_ts = None
    last_critical_ts = None

    for row in auth_log:
        # Beregn scoren for denne log‑post
        score = risk_score_of(row, employee_idx, host_idx)

        if score == "red":
            red_count += 1
        elif score == "critical":
            critical_count += 1
            # Konverter tidsstemplet til streng – uanset om det oprindeligt er int eller str
            ts = str(row[1])

            if first_critical_ts is None:
                first_critical_ts = ts
            # Sidste kritiske tidsstempel opdateres hver gang vi ser en "critical"
            last_critical_ts = ts

    return red_count, critical_count, first_critical_ts, last_critical_ts

# wrapper
if __name__ == "__main__":
    # Læs data én gang
    former = read_csv("former_employees.csv")
    auth    = read_csv("auth_log.csv")
    employees = read_csv("employees.csv")
    hosts   = read_csv("hosts.csv")

    # Byg indeks‑tabeller
    former_idx   = username_index_of(former)
    employee_idx = employee_username_index_of(employees)
    host_idx     = hostname_index_of(hosts)

    # Eksempel på at bruge dem
    post_term = post_termination_logins_of(auth, former_idx)
    print(f"Logins efter fratræden: {len(post_term)}")

    scores = risk_scores_of(auth, employee_idx, host_idx, employees, hosts)
    red, crit, first, last = risk_summary_of(auth, employee_idx, host_idx, employees, hosts)