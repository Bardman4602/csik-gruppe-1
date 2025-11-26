from d1 import *

# Tests af eksempel 1
def test_positives_of_skips_negatives():
    assert list(positives_of([-1])) == []

def test_positives_of_skips_zero():
    assert list(positives_of([0])) == []

def test_positives_of_keeps_positives():
    assert list(positives_of([1])) == [1]

def test_positives_of_is_streaming():
    stream = iter([-3, 2, 0, 4, -1])

    filtered_stream = positives_of(stream)

    assert next(filtered_stream) == 2
    assert next(filtered_stream) == 4
    assert list(filtered_stream) == []

# Tests af eksempel 2
def test_failed_root_logins_of_skips_non_root_logins():
    logs = [('pc-006', '2025-11-04T22:03:19', 'leaf', 'failure')]
    assert list(failed_root_logins_of(logs)) == []

def test_failed_root_logins_of_skips_successful_root_logins():
    logs = [('pc-004', '2025-11-04T22:03:17', 'root', 'success')]
    assert list(failed_root_logins_of(logs)) == []

def test_failed_root_logins_of_filters_keeps_failed_root_logins():
    logs = [('pc-005', '2025-11-04T22:03:18', 'root', 'failure')]
    assert list(failed_root_logins_of(logs)) == logs

def test_failed_root_logins_of_is_streaming():
    log1 = ('pc-004', '2025-11-04T22:03:17', 'root', 'success')
    log2 = ('pc-005', '2025-11-04T22:03:18', 'root', 'failure')
    log3 = ('pc-006', '2025-11-04T22:03:19', 'leaf', 'failure')
    log4 = ('pc-007', '2025-11-04T22:03:20', 'root', 'failure')
    logs = iter([log1, log2, log3, log4])

    filtered_logs = failed_root_logins_of(logs)

    assert next(filtered_logs) == log2
    assert next(filtered_logs) == log4
    assert list(filtered_logs) == []

# Opgave 1
def test_ind_december_filters_november():
    logs = [
        ('pc-001', '2025-11-30T23:59:59', 'root', 'failure'),   # november
        ('pc-002', '2025-12-01T00:00:00', 'root', 'failure'),   # december
        ('pc-003', '2025-12-15T12:34:56', 'leaf', 'success'),   # december
    ]

    result = list(in_december(logs))
    expected = [
        ('pc-002', '2025-12-01T00:00:00', 'root', 'failure'),
        ('pc-003', '2025-12-15T12:34:56', 'leaf', 'success'),
    ]

    assert result == expected

def test_in_december_is_streaming():
    log1 = ('pc-001', '2025-11-30T23:59:59', 'root', 'failure')
    log2 = ('pc-002', '2025-12-01T00:00:00', 'root', 'failure')
    log3 = ('pc-003', '2025-12-02T01:02:03', 'leaf', 'success')
    logs = iter([log1, log2, log3])
    
    filtered = in_december(logs)
    assert next(filtered) == log2
    assert next(filtered) == log3
    assert list(filtered) == []


# Opgave 2
def test_in_date_range_basic():
    logs = [
        ('pc-001', '2025-10-31T23:59:59', 'root', 'failure'),
        ('pc-002', '2025-11-01T00:00:00', 'root', 'failure'),
        ('pc-003', '2025-11-15T12:00:00', 'leaf', 'success'),
        ('pc-004', '2025-12-01T00:00:00', 'root', 'failure'),
    ]

    result = list(in_date_range(logs, start="2025-11-01", end="2025-11-30"))
    expected = [
        ('pc-002', '2025-11-01T00:00:00', 'root', 'failure'),
        ('pc-003', '2025-11-15T12:00:00', 'leaf', 'success'),
    ]

    assert result == expected

def test_in_date_range_is_streaming():
    log1 = ('pc-001', '2025-11-01T00:00:00', 'root', 'failure')
    log2 = ('pc-002', '2025-11-15T12:00:00', 'leaf', 'success')
    log3 = ('pc-003', '2025-12-01T00:00:00', 'root', 'failure')
    logs = iter([log1, log2, log3])

    filtered = in_date_range(logs, start="2025-11-01", end="2025-11-30")
    assert next(filtered) == log1
    assert next(filtered) == log2
    assert list(filtered) == []

# Opgave 3
def test_on_host_filters_correct_host():
    logs = [
        ('host-a', '2025-11-01T00:00:00', 'root', 'failure'),
        ('host-b', '2025-11-01T01:00:00', 'leaf', 'success'),
        ('host-a', '2025-11-02T02:00:00', 'root', 'success'),
    ]
    result = list(on_host(logs, hostname='host-a'))
    expected = [
        ('host-a', '2025-11-01T00:00:00', 'root', 'failure'),
        ('host-a', '2025-11-02T02:00:00', 'root', 'success'),
    ]
    assert result == expected

def test_on_host_is_streaming():
    log1 = ('host-x', '2025-11-01T00:00:00', 'root', 'failure')
    log2 = ('host-y', '2025-11-01T01:00:00', 'leaf', 'success')
    logs = iter([log1, log2])

    filtered = on_host(logs, hostname="host-x")
    assert next(filtered) == log1
    assert list(filtered) == []

# Opgave 4
def test_by_user_filters_correct_user():
    logs = [
        ('host-1', '2025-11-01T00:00:00', 'alice', 'failure'),
        ('host-2', '2025-11-01T01:00:00', 'bob',   'success'),
        ('host-3', '2025-11-02T02:00:00', 'alice', 'success'),
    ]
    result = list(by_user(logs, username="alice"))
    expected = [
        ('host-1', '2025-11-01T00:00:00', 'alice', 'failure'),
        ('host-3', '2025-11-02T02:00:00', 'alice', 'success'),
    ]

    assert result == expected

def test_by_user_is_streaming():
    log1 = ('host-1', '2025-11-01T00:00:00', 'charlie', 'failure')
    log2 = ('host-2', '2025-11-01T01:00:00', 'dave',    'success')
    logs = iter([log1, log2])

    filtered = by_user(logs, username="charlie")
    assert next(filtered) == log1
    assert list(filtered) == []