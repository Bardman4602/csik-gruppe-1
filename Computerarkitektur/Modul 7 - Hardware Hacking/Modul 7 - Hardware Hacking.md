#csik #computerarkitektur #opgaver 

# Opgave
Vi skal have fingrene i følgende info fra en Linksys router:
- SSID
- Wireless PW
- Admin PW
- Enhedens MAC
- Enhedsnavn

#### Fundne "Flag:"

| "Flag"            | Resultat          |
| ----------------- | ----------------- |
| SSID              | Kantine           |
| MAC               | 58:EF:68:59:0D:DB |
| Admin Password    | admin             |
| Wireless Password | peterjepsen       |
| Enhedsnavn        | E900              |

## Fremgangsmåde

 ### Step 1 - Skil lortet ad!
 - Yousef er gået i krig med at skille routeren fra hinanden. 

### Step 2 - Trial and error
- Vi forsøger at finde de rigtige forbindelser mellem min pc og routeren, via USB-UART enheden.
- ![[IMG20251208105633.jpg]]
- Vi forsøger at få liv i osciloskopet igen
- Vi har lykkedes med at få et output fra  routeren ind i RealTerm på Bastians PC
![[IMG20251208111159.jpg]]



Det giver ikke meget mening, men så ændrede vi baud-raten i RealTerm og fik dette output:
- ![[IMG20251208112529.jpg]]

- Efter mere fiflen med baud raten, fik man et prompt med "Press Enter to continue"
- Vi trykkede enter, og er nu havnet i noget der ligner en linux-terminal:
![[IMG20251208112926.jpg]]

```bash
ifconfig -a
```
Denne command har givet os enhedens mac-addresse, som er:

 `58:EF:68:59:0D:DB`

### Step 3 - /proc/kcore
Nu vil vi kigge nærmere på den mappe som er specificeret i opgaven:

```bash
cd /proc
```

Vi forsøger os først med en klassisk grep command:

```bash
grep 'password' kcore
```
- Dette gav os ikke umiddelbart et brugbart resultat. 

Vi skriver resultatet fra kcore ind i en .txt fil
```bash
cat /kcore
```

I RealTerm trykker vi "Start Overwrite" og srkvier outputtet til en fil på vores lokale maskine.

### Læsning af info fra capture.txt
Vi åbnede capture.txt i notepad og søgte rundt efter de info vi leder efter. Dette gav os svarene på alle de spørgsmål vi søgte. Så vores endelige resultat er i tabellen her, som også findes øverst i dokumentet her:

| "Flag"            | Resultat          |
| ----------------- | ----------------- |
| SSID              | Kantine           |
| MAC               | 58:EF:68:59:0D:DB |
| Admin Password    | admin             |
| Wireless Password | peterjepsen       |
| Enhedsnavn        | E900              |

*Udført af Bastian, Yousef, Nathan og Jonas*