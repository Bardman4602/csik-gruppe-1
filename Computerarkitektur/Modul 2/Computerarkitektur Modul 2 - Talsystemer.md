#csik #computerarkitektur 

![[Binære talsystem.pdf]]
## Agenda
- Hvad er forskellen på digitale og analoge signaler.
- Hvordan bliver elektriske signaler til talværdier.
- Det binære talsystem
- Øvelse 1 – tæl binært
- Det hexa-decimale talsystem. Hvad skal vi bruge det til.
- Øvelse 2 – kodning og afkodning
- Oktale talsystem
- Opgaver i Codelabby

### Analoge og digitale signaler
#### Analoge:
- Trinløse
- Støjfølsomme
- Besværlige at skabe og læse elektronisk

**Eksempler:**
- Lyd
- Lys
- Vind

#### Digitale:
- Transistorer
	- Kan forstærke analoge signaler
	- Kan fungere som swtich (on/off)
- Er elektrisk robuste
- Er billige at fremstille

**Eksempler:**
- Stikkontakter
- Computere
- Morsekode

### Talsystemer
#### Bit - binary digit
2 tilstande
- tændt eller slukket
- 0/1
- 2 bits = 4 kombinationer
- Jo flere bits, des flere kombinationer

#### Binær til decimal

| 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |

Nederste række fortæller hvilke bits er tændt eller slukket

##### Øvelse - Kodning og afkodning
72, 69, 74   74, 85, 76, 73, 45
hej julie

64+8 = 72
64+32+4+1 = 101
64+32+8+4 = 108
64+32+8+4 = 108
63+32+8+4+2+1 = 111

H E L L O

#### Hexadecimal
- Hver pixel på en skærm har en farve
- Hver farve repræsenteres af et antal bits
- Normal farvedybde er 24 bits
- 8 bits til hver farve (Rød, grøn og blå)
- 16.777.216 mulige kombinationer
- For at gøre det mere anvendeligt, bruger ofte man HEX notation til at bestemme farver
- Hex er base 16

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | A   | B   | C   | D   | E   | F   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
- Hver halve byte udgør et hex ciffer med værdien 0-F


## Opgaver
[[C-Ark Modul 2 Opgave 1]]
[[C-Ark Modul 2 Opgave 2]]
