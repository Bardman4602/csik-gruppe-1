from o2 import *

#Opgave 1
def test_username_index_of():
    employees = read_csv("former_employees.csv")    
    employee_dict = username_index_of(employees)

    assert employee_dict["peni"][0] == "Peter Nielsen"
    assert employee_dict["soni"][0] == "Sonja Nielsen"
    assert employee_dict["kiki"][0] == "Kirsten Kirr"
    assert employee_dict["moni"][0] == "Morten Nivå"
    assert employee_dict["wiys"][0] == "William Ystad"


# Opgave 2
def test_post_termination_logins_of():    
    auth = read_csv("auth_log.csv")
    former = read_csv("former_employees.csv")
    former_idx   = username_index_of(former)
    result = post_termination_logins_of(auth, former_idx)

    for row in result:
        username = row[2]
        assert username in former_idx, (
            f"Brugeren '{username}' findes ikke i former_idx, men er med i resultatet."
        )

    for row in result:
        username = row[2]
        timestamp = row[1]     
        termination_date = former_idx[username][3]
        assert timestamp > termination_date, (
            f"Tidsstempel {timestamp} er ikke efter fratrædelsesdato "
            f"{termination_date} for brugeren {username}."
        )

# Opgave 3
def test_employee_username_index_of():
    employees = read_csv("employees.csv")
    idx = employee_username_index_of(employees)

    assert isinstance(idx, dict), "employee_username_index_of skal returnere en dict"

    first_row, second_row = employees[0], employees[1]
    for row in (first_row, second_row):
        username = row[2]
        assert username in idx, f"Brugernavnet {username} mangler i indekset"

        indexed_row = idx[username]
        assert indexed_row[0] == row[0], f"Navnet for {username} er forkert i indekset"
        assert indexed_row[3] == row[3], f"Afdelingen for {username} er forkert i indekset"

# Opgave 4
def test_hostname_index_of():
    hosts = read_csv("hosts.csv")
    idx = hostname_index_of(hosts)

    assert isinstance(idx, dict), "employee_username_index_of skal returnere en dict"

    first_row, second_row = hosts[0], hosts[1]

    for row in (first_row, second_row):
        hostname = row[0]                      # kolonne 0 = hostname
        # a) hostname skal findes i indekset
        assert hostname in idx, f"Hostname {hostname} mangler i indekset"

        # b) de gemte værdier skal svare til den originale CSV‑række
        indexed_row = idx[hostname]
        assert indexed_row[0] == row[0], f"Hostname for {hostname} er forkert i indekset"
        assert indexed_row[1] == row[1], f"MAC‑address for {hostname} er forkert i indekset"
        assert indexed_row[2] == row[2], f"Department for {hostname} er forkert i indekset"

# Opgave 5
def test_risk_scores_of():
    employees = read_csv("employees.csv")
    hosts = read_csv("hosts.csv")
    auth = read_csv("auth_log.csv")
    
    employee_idx = employee_username_index_of(employees)
    host_idx = hostname_index_of(hosts)
    
    # Test 1: Result is a list
    result = risk_scores_of(auth, employee_idx, host_idx)
    assert isinstance(result, list), "risk_scores_of should return a list"
    
    # Test 2: Result length matches input length
    assert len(result) == len(auth), f"Expected {len(auth)} scores, got {len(result)}"
    
    # Test 3: All elements are valid risk scores
    valid_scores = {"green", "yellow", "red", "critical"}
    for i, score in enumerate(result):
        assert score in valid_scores, f"Row {i}: Invalid risk score '{score}'"
    
    # Test 4: Each result matches individual risk_score_of calls
    for i, row in enumerate(auth):
        expected = risk_score_of(row, employee_idx, host_idx)
        assert result[i] == expected, f"Row {i}: Expected {expected}, got {result[i]}"


def test_risk_summary_of():
    employees = read_csv("employees.csv")
    hosts     = read_csv("hosts.csv")
    auth      = read_csv("auth_log.csv")

    employee_idx = employee_username_index_of(employees)
    host_idx     = hostname_index_of(hosts)

    red, crit, first_ts, last_ts = risk_summary_of(auth, employee_idx, host_idx)

    # 1. Kontroller typer
    assert isinstance(red, int)
    assert isinstance(crit, int)
    assert (first_ts is None) or isinstance(first_ts, str)
    assert (last_ts  is None) or isinstance(last_ts,  str)

    # 2. Sammenlign med en “brute‑force” reference‑implementering
    # (her bruger vi risk_score_of direkte)
    ref_red = ref_crit = 0
    ref_first = ref_last = None
    for row in auth:
        sc = risk_score_of(row, employee_idx, host_idx)
        if sc == "red":
            ref_red += 1
        if sc == "critical":
            ref_crit += 1
            ts = row[1]
            if ref_first is None:
                ref_first = ts
            ref_last = ts

    assert red == ref_red
    assert crit == ref_crit
    assert first_ts == ref_first
    assert last_ts == ref_last
