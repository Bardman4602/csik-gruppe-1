from d2 import *

# -------------
# Test eksempler 
def test_squares_of_calculates_squares():
    assert list(squares_of([-3, 3])) == [9, 9]

def test_squares_of_is_streaming():
    stream = iter([-3, 2, 0, 4, -1])

    filtered_stream = squares_of(stream)

    assert next(filtered_stream) == 9
    assert next(filtered_stream) == 4
    assert next(filtered_stream) == 0
    assert next(filtered_stream) == 16
    assert next(filtered_stream) == 1
    assert list(filtered_stream) == []

def test_hosts_and_dates_of_extracts_host_and_date():
    logs = [('pc-006', '2025-11-04T22:03:19', 'leaf', 'failure')]
    assert list(hosts_and_dates_of(logs)) == [('pc-006', '2025-11-04')]

def test_hosts_and_dates_of_is_streaming():
    log1 = ('pc-004', '2025-11-14T22:03:37', 'root', 'success')
    log2 = ('pc-005', '2025-11-15T22:03:38', 'root', 'failure')
    log3 = ('pc-006', '2025-11-16T22:03:39', 'leaf', 'failure')
    log4 = ('pc-007', '2025-11-17T22:03:40', 'root', 'failure')
    logs = iter([log1, log2, log3, log4])

    mapped_logs = hosts_and_dates_of(logs)

    assert next(mapped_logs) == ('pc-004', '2025-11-14')
    assert next(mapped_logs) == ('pc-005', '2025-11-15')
    assert next(mapped_logs) == ('pc-006', '2025-11-16')
    assert next(mapped_logs) == ('pc-007', '2025-11-17')
    assert list(mapped_logs) == []

# -----------

# Opgave 1
def test_as_dicts_transforms_to_dict():
    logs = [
        ("pluto",   "2024-01-01T00:04:34", "gefu",   "success"),
        ("pc-029",  "2024-01-01T00:10:17", "ereg",   "success"),
        ("richard", "2024-01-01T00:15:26", "nini",   "success"),
        ("niels",   "2024-01-01T00:21:09", "papa",   "failure"),
    ]

    expected = [
        {"hostname": "pluto",   "timestamp": "2024-01-01T00:04:34",
         "username": "gefu",   "result": "success"},
        {"hostname": "pc-029",  "timestamp": "2024-01-01T00:10:17",
         "username": "ereg",   "result": "success"},
        {"hostname": "richard", "timestamp": "2024-01-01T00:15:26",
         "username": "nini",   "result": "success"},
        {"hostname": "niels",   "timestamp": "2024-01-01T00:21:09",
         "username": "papa",   "result": "failure"},
    ]

    assert list(as_dicts(logs)) == expected

def test_as_dicts_is_streaming():
    log1 = ("a", "2024-01-01T00:00:00", "u1", "success")
    log2 = ("b", "2024-01-01T01:00:00", "u2", "failure")
    logs = iter([log1, log2])
    gen = as_dicts(logs)

    first = next(gen)
    assert first == {
        "hostname": "a",
        "timestamp": "2024-01-01T00:00:00",
        "username": "u1",
        "result": "success",
    }

    second = next(gen)
    assert second == {
        "hostname": "b",
        "timestamp": "2024-01-01T01:00:00",
        "username": "u2",
        "result": "failure",
    }

    assert list(gen) == []

# Opgave 2
def test_with_boolean_results_converts_success_and_failure():
    dicts = [
        {"hostname": "x", "timestamp": "2024-01-01T00:00:00",
         "username": "u", "result": "success"},
        {"hostname": "y", "timestamp": "2024-01-01T01:00:00",
         "username": "v", "result": "failure"},
        {"hostname": "z", "timestamp": "2024-01-01T02:00:00",
         "username": "w", "result": "unknown"},   # skal forblive uændret
    ]

    expected = [
        {"hostname": "x", "timestamp": "2024-01-01T00:00:00",
         "username": "u", "result": True},
        {"hostname": "y", "timestamp": "2024-01-01T01:00:00",
         "username": "v", "result": False},
        {"hostname": "z", "timestamp": "2024-01-01T02:00:00",
         "username": "w", "result": "unknown"},
    ]

    assert list(with_boolean_results(dicts)) == expected

def test_with_boolean_results_is_streaming():
    d1 = {"hostname": "a", "timestamp": "t1", "username": "u1", "result": "success"}
    d2 = {"hostname": "b", "timestamp": "t2", "username": "u2", "result": "failure"}
    stream = iter([d1, d2])
    gen = with_boolean_results(stream)

    assert next(gen)["result"] is True
    assert next(gen)["result"] is False
    assert list(gen) == []

# Opgave 3
def test_with_dates_replaces_timestamp_with_date():
    dicts = [
        {"hostname": "h1", "timestamp": "2025-11-04T22:03:19",
         "username": "root", "result": "failure"},
        {"hostname": "h2", "timestamp": "2025-12-01T00:00:00",
         "username": "leaf", "result": "success"},
    ]

    expected = [
        {"hostname": "h1", "timestamp": "2025-11-04",
         "username": "root", "result": "failure"},
        {"hostname": "h2", "timestamp": "2025-12-01",
         "username": "leaf", "result": "success"},
    ]

    assert list(with_dates(dicts)) == expected

def test_with_dates_is_streaming():
    d1 = {"hostname": "c", "timestamp": "2024-03-05T12:34:56",
          "username": "u", "result": "success"}
    d2 = {"hostname": "d", "timestamp": "2024-04-06T23:45:01",
          "username": "v", "result": "failure"}
    stream = iter([d1, d2])
    gen = with_dates(stream)

    first = next(gen)
    assert first["timestamp"] == "2024-03-05"
    second = next(gen)
    assert second["timestamp"] == "2024-04-06"
    assert list(gen) == []


# Opgave 4
def test_with_risk_scores_adds_correct_scores():
    employee_idx = {
        "gefu":   ("id", "fullname", "title", "IT"),
        "ereg":   ("id", "fullname", "title", "SALES"),
        "nini":   ("id", "fullname", "title", "HR"),
        "papa":   ("id", "fullname", "title", "FINANCE"),
    }    

    host_idx = {
        "pluto":   ("id", "location", "IT"),
        "pc-029":  ("id", "location", "SALES"),
        "richard": ("id", "location", "HR"),
        # udeladt niels
    }

    dicts = [
        {"hostname": "pluto",   "timestamp": "2024-01-01", "username": "gefu",   "result": True},   # same dept
        {"hostname": "pc-029",  "timestamp": "2024-01-01", "username": "ereg",   "result": False},  # fail, same dept
        {"hostname": "richard", "timestamp": "2024-01-01", "username": "nini",   "result": True},   # success, same dept
        {"hostname": "niels",   "timestamp": "2024-01-01", "username": "papa",   "result": False},  # fail, unknown host
    ]

    result = list(with_risk_scores(dicts, employee_idx, host_idx))

    assert result[0]["risk_score"] == "green"     # same dept
    assert result[1]["risk_score"] == "green"     # same dept (failure but still same dept = green)
    assert result[2]["risk_score"] == "green"     # same dept
    assert result[3]["risk_score"] == "red"    


def test_with_risk_scores_unknown_employee():
    employee_idx = {
        "gefu": ("id", "fullname", "title", "IT"),
    }
    host_idx = {
        "pluto": ("id", "location", "IT")
    }

    # unknown user "hacker"
    dicts = [
        {"hostname": "pluto", "timestamp": "2024-01-01", "username": "hacker", "result": True},
        {"hostname": "pluto", "timestamp": "2024-01-01", "username": "hacker", "result": False},
    ]

    scores = list(with_risk_scores(dicts, employee_idx, host_idx))

    assert scores[0]["risk_score"] == "critical"  # unknown + success
    assert scores[1]["risk_score"] == "red"       # unknown + failure

def test_with_risk_scores_is_streaming():
    employee_idx = {
        "gefu": ("id", "fullname", "title", "IT"),
    }
    host_idx = {
        "pluto": ("id", "location", "IT"),
    }

    d1 = {"hostname": "pluto", "timestamp": "t1", "username": "gefu", "result": True}
    d2 = {"hostname": "pluto", "timestamp": "t2", "username": "gefu", "result": False}
    stream = iter([d1, d2])

    gen = with_risk_scores(stream, employee_idx, host_idx)

    first = next(gen)
    assert first["risk_score"] == "green"
    second = next(gen)
    assert second["risk_score"] == "green"  # same dept still green
    assert list(gen) == []  # streaming test ends correctly