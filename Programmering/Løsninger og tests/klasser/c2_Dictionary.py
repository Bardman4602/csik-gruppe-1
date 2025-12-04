class Dictionary:
    """
    Ordbog, hvor opslagene er grupperet efter nøgle‑længde.
    Intern struktur:  _v[l]  →  liste af (key, value)-par med netop længden l.
    Der er kun én privat hjælper (_find); bucket‑valget skrives inline
    i hver offentlig metode – så der er ingen separat bucket‑funktion.
    """

   
    def __init__(self) -> None:
        """Start med en tom vektor af vektorer."""
        self._v = []          # ydre liste – hver position er en bucket
        self._count = 0       # samlet antal (key, value)-par

    
    def _find(self, bucket, key):
        """
        Returnerer indeks i ``bucket`` hvor ``key`` findes,
        eller -1 hvis den ikke er til stede.
        """
        i = 0
        n = len(bucket)
        while i < n:
            the_key, _ = bucket[i]
            if the_key == key:
                return i
            i += 1
        return -1
    

    def add_entry(self, key, value):
        """
        Tilføjer (key, value) eller erstatter den eksisterende værdi.
        Returnerer den gamle værdi, hvis der var en, ellers None.
        """
        # Find (eller opret) den bucket der svarer til nøglens længde
        length = len(key)
        while len(self._v) <= length:          # udvid ydre liste efter behov
            self._v.append([])                 # nye buckets starter tomme

        bucket = self._v[length]                # bucket for denne nøgle

        idx = self._find(bucket, key)           # <-- korrekt rækkefølge!
        if idx == -1:                           # nøgle findes ikke → append
            bucket.append((key, value))
            self._count += 1
            return None
        else:                                   # nøgle findes → erstat
            _, old_val = bucket[idx]
            bucket[idx] = (key, value)
            return old_val

    def lookup_entry(self, key):
        """
        Returnerer værdien for ``key`` eller None, hvis den ikke findes.
        """
        length = len(key)
        if length >= len(self._v):              # bucket eksisterer ikke
            return None
        bucket = self._v[length]

        idx = self._find(bucket, key)           # <-- korrekt rækkefølge!
        if idx == -1:
            return None
        _, val = bucket[idx]
        return val

    def contains_key(self, key):
        """
        Returnerer True, hvis ``key`` er i ordbogen, ellers False.
        """
        length = len(key)
        if length >= len(self._v):
            return False
        bucket = self._v[length]
        return self._find(bucket, key) != -1    # <-- korrekt rækkefølge!

    def delete_entry(self, key):
        """
        Sletter (key, value) fra ordbogen, hvis den findes.
        Returnerer den fjernede værdi eller None, hvis nøglen ikke var til stede.
        """
        length = len(key)
        if length >= len(self._v):
            return None
        bucket = self._v[length]

        idx = self._find(bucket, key)           # <-- korrekt rækkefølge!
        if idx == -1:
            return None

        # pop fjerner elementet fra bucket og returnerer (key, value)
        _, val = bucket.pop(idx)
        self._count -= 1
        return val

    def size(self):
        """Antallet af (key, value)-par i hele ordbogen."""
        return self._count

