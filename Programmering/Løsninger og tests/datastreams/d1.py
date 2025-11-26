# --------------------------------
# Skabelon
#  def my_filter(stream):
#     for x in stream:
#         if # x satisfies some condition:
#             yield x
# ---------------------------------

# -------------------------------
# eksempler
def positives_of(stream):
    for x in stream:
        if x > 0:
            yield x

def failed_root_logins_of(logs):
    for log in logs:
        if log[2] == 'root' and log[3] == 'failure':
            yield log

# -------------------------------

# Opgave 1 - filtrer på december
def in_december(logs):
    for log in logs:
        datum = log[1]
        if datum[5:7] == "12":
            yield log

# Opgave 2 - filtrer på dato i range
def in_date_range(logs, start: str, end: str):
    for log in logs:
        datum = log[1]
        if start <= datum <= end:
            yield log

# Opgave 3 - filter på host-name
def on_host(logs, hostname: str):
    for log in logs:
        if log[0] == hostname:
            yield log

# Opgave 4 - filtrer på username
def by_user(logs, username: str):
    for log in logs:
        if log[2] == username:
            yield log

# wrapper
if __name__ == "__main__":

    stream = iter([-3, 2, 0, 4, -1])
    stream = positives_of(stream)
    print(next(stream)) # 2
    print(next(stream)) # 4
    print(next(stream)) # fails with StopIteration

    # .csv reader + filter
    import csv
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as in_file:
        with open('filtered_auth_log.csv', 'w', newline='', encoding='utf-8') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for log in failed_root_logins_of(reader):
                writer.writerow(log)