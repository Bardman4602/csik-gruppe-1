#-----------------------------------
# eksempler
def squares_of(stream):
    for x in stream:
        yield x * x

def hosts_and_dates_of(logs):
    for log in logs:
        yield (log[0],log[1][0:10])

#-------------------------------------

# Opgave 1 - tranformer hver log-post til en ordbog med angivne nøgler
def as_dicts(logs):
    for log in logs:
        yield{
            "hostname":  log[0],
            "timestamp": log[1],
            "username":  log[2],
            "result":    log[3],
        }

# Opgave 2 - tranformerer en strøm af ordbøger og erstatter dem ned en boolean værdi
def with_boolean_results(dict_stream):
    for d in dict_stream:
        new = d.copy()                     # undgå mutation af input‑dict
        if new["result"] == "success":
            new["result"] = True
        elif new["result"] == "failure":
            new["result"] = False
        yield new

# Opgave 3 - transformerer en strøm af ordbøger og erstatter dato-delen i ISO format
def with_dates(stream):
    for d in stream:
        new = d.copy()
        new["timestamp"] = new["timestamp"].split("T")[0]
        yield new


# Opgave 4 - tilføj risk scores
def risk_score_of(log_row, employee_idx, host_idx):    
    hostname = log_row[0]
    username = log_row[2]
    status_raw = log_row[3]
    status = status_raw.strip().lower()         

    # Er brugeren en kendt medarbejder?
    if username in employee_idx:
        employee_dept = employee_idx[username][3]      # department i employee‑tabellen

        # Har vi oplysninger om hosten?
        host_entry = host_idx.get(hostname)
        if host_entry:                                 # host findes i vores ordbog
            host_dept = host_entry[2]                  # department i hosts‑tabellen

            # Samme afdeling → grønt
            if host_dept == employee_dept:
                return "green"

            # Forskellig afdeling
            if status == "failure":
                return "yellow"
            else:                                     # success
                return "red"

        # Host‑oplysninger findes ikke → “øvrige” tilfælde
        if status == "failure":
            return "red"
        else:
            return "critical"

    # Ikke en nuværende medarbejder (eller ukendt brugernavn)
    if status == "failure":
        return "red"
    else:
        return "critical"
    
# bruger ovenstående funktion til at give vores strømme en risk score   
def with_risk_scores(dict_stream, employee_idx, host_idx): 
    for d in dict_stream:
        new = d.copy()

        log_row = (
            new["hostname"],
            new["timestamp"],
            new["username"],
            new["result"] if isinstance(new["result"], str) else
            ("success" if new["result"] else "failure")
        )
        new["risk_score"] = risk_score_of(log_row, employee_idx, host_idx)
        yield new

# wrapper
if __name__ == '__main__':
    stream = iter([-3, 2, 0, 4, -1])
    stream = squares_of(stream)
    print(next(stream)) # 9
    print(next(stream)) # 4
    print(next(stream)) # 0
    print(next(stream)) # 16
    print(next(stream)) # 1
    print(next(stream)) # fails with StopIteration

    # .csv reader + filter
    import csv
    with open('auth_log.csv', 'r', newline='', encoding='utf-8') as in_file:
        with open('mapped_auth_log.csv', 'w', newline='', encoding='utf-8') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for host_and_date in hosts_and_dates_of(reader):
                writer.writerow(host_and_date)

    sample = [
        ("pluto",   "2024-01-01T00:04:34", "gefu",   "success"),
        ("pc-029",  "2024-01-01T00:10:17", "ereg",   "success"),
        ("richard", "2024-01-01T00:15:26", "nini",   "success"),
        ("niels",   "2024-01-01T00:21:09", "papa",   "failure"),
    ]

    # as_dicts
    dicts = list(as_dicts(sample))
    print("as_dicts →", dicts)

    # with_boolean_results
    bools = list(with_boolean_results(dicts))
    print("with_boolean_results →", bools)

    # with_dates
    dates = list(with_dates(bools))
    print("with_dates →", dates)