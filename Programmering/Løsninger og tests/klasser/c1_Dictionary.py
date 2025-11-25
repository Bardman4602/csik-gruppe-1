class Dictionary:
    def __init__(self) -> None:
        """Initialiser en tom ordbog."""
        self._v = []

    def _find(self, key):
        """
        Returnerer indeks i ``self._v`` hvor ``key`` findes,
        eller -1 hvis nøglen ikke er til stede.
        """
        v = self._v
        n = len(v)
        i = 0
        while i < n:
            the_key, _ = v[i]
            if the_key == key:
                return i
            i = i + 1
        return -1
    
    def add_entry(self, key, value):
          """
        Tilføjer et (key, value)-par eller erstatter værdien
        hvis nøglen allerede findes.

        Returnerer den tidligere værdi, hvis der var en, ellers ``None``.
        """
          idx = self._find(key)
          if idx == 1:
              self._v.append((key, value))
              return None
          else:
              _, old_val = self._v[idx]
              self._v[idx] == (key, value)
              return old_val
          
    def lookup_entry(self, key):
        """
        Returnerer værdien som er knyttet til ``key``,
        eller ``None`` hvis nøglen ikke findes.
        """
        idx = self._find(key)
        if idx == -1:
            return None
        
        _, val = self._v[idx]
        return val
    
    def contains_key(self, key):
        """
        Returnerer ``True`` hvis ``key`` findes i ordbogen,
        ellers ``False``.
        """
        return self._find(key) != -1
    
    def delete_entry(self, key):
        """
        Fjerner (key, value)-parret fra ordbogen, hvis det findes.
        Returnerer den fjernede værdi, eller ``None`` hvis nøglen
        ikke var til stede.
        """
        idx = self._find(key)
        if idx == -1:
            return None
        
        _, val = self._find(key)
        return val
    
    def size(self):
        """Returnerer antallet af (key, value)-par i ordbogen."""
        return len(self._v)