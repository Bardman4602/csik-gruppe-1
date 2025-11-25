# Opgave 1 - string i listen v er nøgle og værdien er dens index i listem
def index_of(v):
    d = {}
    for i, key in enumerate(v):
        d[key] = i
    return d

# Opgave 2 + 3 - returnerer en dict med mac-adresser
def mac_index_of(v):
    d = {}
    for i, entry in enumerate(v):
        mac = entry[3]                    
        if mac in d:                       
            raise ValueError(f"Duplikat MAC‑adresse fundet: {mac}")
        d[mac] = i
    return d

def mac_index_of_selfcontained(v):
    d = {}
    for entry in v:
        mac = entry[3]
        if mac in d:
            raise ValueError(f"Duplikat MAC‑adresse fundet: {mac}")
        d[mac] = entry
    return d