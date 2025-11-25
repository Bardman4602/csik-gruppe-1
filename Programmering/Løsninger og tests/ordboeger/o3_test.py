from o3 import *

# Opgave 1
def test_login_count_by_username():
    auth = read_csv("auth_log.csv")
    res = login_count_by_username(auth)

    assert isinstance(res, dict), "login_count_by_username skal returnere en dict"

    file = {}
    for row in auth:
        username = row[2]
        file[username] = file.get(username, 0) + 1
    assert res == file, "Resultat matcher ikke"
    

# Opgave 2
def test_login_dates_by_username():
    auth = read_csv("auth_log.csv")
    res = login_dates_by_username(auth)

    assert isinstance(res, dict), "login_count_by_username skal returnere en dict"

    for username, dates in res.items():
        assert isinstance(dates, list), f"værdien for {username} skal være en liste"
        for d in dates:
            assert len(d.split("-")) == 3, f"Datoen {d} er i forkert format"

# Opgave 3
def test_failed_logins_by_username():
    auth = read_csv("auth_log.csv")
    res = failed_logins_by_username(auth)

    assert isinstance(res, dict), "failed_logins_by_username skal returnere en dict"

    # Hver tuple skal have result == "failure"
    for username, rows in res.items():
        for row in rows:
            assert row[3] == "failure", f"Række {row} er ikke en fejl‑login"


# Opgave 4
def test_active_period_by_username():
    auth = read_csv("auth_log.csv")
    res = active_period_by_username(auth)

    assert isinstance(res, dict), "active_period_by_username skal returnere en dict"

    # For hver bruger skal første ≤ sidste (lexicografisk fordi timestamps er ISO‑8601)
    for username, (first, last) in res.items():
        assert first <= last, f"For {username}: first ({first}) > last ({last})"

# Opgave 5
def test_stats_by_hostname():
    auth = read_csv("auth_log.csv")
    res = stats_by_hostname(auth)

    assert isinstance(res, list), "stats_by_hostname skal returnere en liste"

    # Hver post skal have fire elementer og korrekt tælling
    for host, first, last, cnt in res:
        # Tæl manuelt for at sammenligne
        manual_cnt = sum(1 for r in auth if r[0] == host)
        assert cnt == manual_cnt, f"Tællingen for {host} er forkert ({cnt} vs {manual_cnt})"

# Opgave 6
def test_stats_by_hostname_and_username():
    auth = read_csv("auth_log.csv")
    res = stats_by_hostname_and_username(auth)

    assert isinstance(res, list), "stats_by_hostname_and_username skal returnere en liste"

    # Kontroller at hver kombination har korrekt tælling
    for host, user, first, last, cnt in res:
        manual_cnt = sum(1 for r in auth if r[0] == host and r[2] == user)
        assert cnt == manual_cnt, f"Tællingen for ({host},{user}) er forkert ({cnt} vs {manual_cnt})"
