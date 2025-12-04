class Dictionary:
    """
    Hash‑baseret ordbog med dynamisk re‑hashing.

    Intern struktur:
      self._v  – en liste af buckets (hver bucket er en liste af (key, value)-tupler)
        self._count – samlet antal elementer i ordbogen

    Startkapacitet er fast sat til 7, men tabellen vokser eller krymper
    automatisk, så load‑factor (antal elementer / antal buckets) holdes
    mellem 0.25 og 1.0.
    """


   
    def __init__(self, initial_capacity: int = 7) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity skal være ≥ 1")
        # ydre tabel – hver position er en tom bucket
        self._v = [[] for _ in range(initial_capacity)]
        self._count = 0        

    
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


    def _rehash(self, new_capacity: int) -> None:
        """
        Opretter en ny tabel med ``new_capacity`` buckets og flytter
        alle eksisterende (key, value)-par ind i den nye tabel.
        """
        if new_capacity < 1:
            new_capacity = 1

        # Gem alle nuværende par
        old_items = []
        for bucket in self._v:
            old_items.extend(bucket)

        # Lav ny tabel
        self._v = [[] for _ in range(new_capacity)]
        self._count = 0                     # vil blive genopbygget i add_entry

        # Indsæt igen – bruger den offentlige add_entry, så tælleren opdateres korrekt
        for k, v in old_items:
            self.add_entry(k, v)
    

    def add_entry(self, key, value):
        """
        Tilføjer (key, value) eller erstatter den eksisterende værdi.
        Returnerer den gamle værdi, hvis der var en, ellers None.
        """
        idx = hash(key) % len(self._v)
        bucket = self._v[idx]

        pos = self._find(bucket, key)
        if pos == -1:                         # nøgle findes ikke → indsæt
            bucket.append((key, value))
            self._count += 1

            # *** dynamisk vækst ***
            if self._count > len(self._v):            # load‑factor > 1
             self._rehash(len(self._v) * 2)        # fordobling
            return None
        else:                                 # nøgle findes → erstat
            _, old_val = bucket[pos]
            bucket[pos] = (key, value)
            return old_val
            
    
    def lookup_entry(self, key):
        """
        Returnerer værdien for ``key`` eller None, hvis den ikke findes.
        """
        idx = hash(key) % len(self._v)          # inline bucket‑valg
        bucket = self._v[idx]

        pos = self._find(bucket, key)
        if pos == -1:
            return None
        _, val = bucket[pos]
        return val

    def contains_key(self, key):
        """
        Returnerer True, hvis ``key`` er i ordbogen, ellers False.
        """
        idx = hash(key) % len(self._v)          # inline bucket‑valg
        bucket = self._v[idx]
        return self._find(bucket, key) != -1
    

    def delete_entry(self, key):
        """
        Sletter (key, value) fra ordbogen, hvis den findes.
        Returnerer den fjernede værdi eller None, hvis nøglen ikke var til stede.
        """
        idx = hash(key) % len(self._v)          # inline bucket‑valg
        bucket = self._v[idx]

        pos = self._find(bucket, key)
        if pos == -1:
            return None

        _, val = bucket.pop(pos)
        self._count -= 1

        # dynamisk krympning
        if self._count < len(self._v) // 4 and len(self._v) > 1:
            new_cap = max(1, len(self._v) // 2)   # mindst 1 bucket
            self._rehash(new_cap)

        return val

    def size(self):
        """Antallet af (key, value)-par i hele ordbogen."""
        return self._count