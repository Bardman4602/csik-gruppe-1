#csik #netværksarkitektur #opgaver

[RFC Intro Lab](https://it-sikkerhed.org/N-ark/M2/%C3%98velse+1+-+RFC+intro+lab)

### Opgave 1.1
1. Gå til: [https://datatracker.ietf.org/doc/html/rfc792](https://datatracker.ietf.org/doc/html/rfc792)
2. Læs abstract og introduktion (side 1-2)
3. Besvar i din noter / laboratoriejournal:
    - Hvornår blev RFC 792 offentliggjort?
	    - *september 1981*
    - Hvad står ICMP for?
	    - *Internet Control Message Protocol*
    - Hvad er ICMP's hovedformål ifølge RFC'en?
	    - *"The purpose of these control messages is to provide feedback about problems in the communication environment, not to make IP reliable."*


### Opgave 1.2: Struktur og indhold 

**Gruppearbejde**

Opdel RFC 792 mellem gruppemedlemmerne:

- **Person A:** Læs afsnit 1-2 (Introduction, Message Formats)
- **Person B:** Læs afsnit 3 (Echo or Echo Reply Message)
- **Person C:** Læs afsnit 4-5 (Destination Unreachable, Time Exceeded)
- **Person D:** Læs afsnit 6-7 (Parameter Problem, Source Quench)

**Hver person præsenterer deres afsnit for gruppen (5 min per person)**

### Fokusområder til præsentation: 

1. **Hovedpointer** i dit afsnit
2. **Tekniske detaljer** der virker vigtige
3. **Spørgsmål** der opstod under læsningen
4. **Forbindelse** til netværkssikkerhed

### [[Besvarelse  RFC opgave 1.2]]


## Del 2
### Opgave 2.1: PING i praksis
1. **Åbn din kommandolinje** (Command Prompt/Terminal)
2. **Kør følgende kommandoer** og dokumentér output:

```bash
# Windows
ping -n 4 8.8.8.8

# Mac/Linux  
ping -c 4 8.8.8.8
```

3. **Analyser output** og identificer:
    - Hvor lang tid tager hver ping?
	    - *141ms i gennemsnit*
    - Hvor mange bytes sendes?
	    - *32 pr. ping*
    - Hvilken IP-adresse svarer?
	    - *8.8.8.8 (dns.google)*

![[RFCOpg2-1.png]]

### Opgave 2.2: RFC vs. Virkelighed 

**Analyse**

Sammenlign dit ping-output med RFC 792:

|RFC 792 Element|Ping Output|Forklaring|
|---|---|---|
|Type = 8 (Echo Request)|Implicit i kommando|Ping sender Type 8|
|Type = 0 (Echo Reply)|"Reply from..."|Modtager Type 0 tilbage|
|Sequence Number|?|Find dette i output|
|Data|"bytes=32"|Standard størrelse|
|Round Trip Time|"time=Xms"|Ikke del af RFC, men nyttigt|

**Diskussion i gruppen:**

- Hvilke dele af RFC 792 ser vi direkte i ping-output?
- Hvilke informationer tilføjer ping, som ikke er i RFC'en?
- Hvorfor tror I, at ping tilføjer ekstra information?

#### AI besvarelse (fact-tjekket og godkendt)
1. **De dele af RFC 792, vi ser direkte i ping‑output**    
    - **ICMP‑type 8 (Echo Request) og type 0 (Echo Reply)** – ping sender en Echo Request og viser svaret som “reply”.
    - **Identifikator (Identifier) og sekvensnummer (Sequence Number)** – i output vises ofte “seq X” (sekvens) og nogle gange “id Y”.
    - **TTL (Time‑to‑Live)** – ping rapporterer “ttl=…”, som er feltet i IP‑headeren, men RFC 792 nævner også TTL‑værdien i den indlejrede IP‑pakke.
    
2. **Informationer ping tilføjer, som ikke er i RFC 792**    
    - **Rundrejsetid (RTT / “time=… ms”)** – beregnes lokalt ved at måle forskellen mellem afsendelse og modtagelse.
    - **Pakke‑størrelse (bytes=…)** – viser hvor mange data‑byte ping har sendt (inkl. ICMP‑header), selvom RFC’en kun beskriver selve ICMP‑payloaden.
    - **Statistikker efter afslutning** (pakker sendt/modtaget, tab % osv.) – samles af ping‑programmet, men er ikke en del af selve ICMP‑protokollen.

3. **Hvorfor ping tilføjer ekstra information**    
    - **Brugervenlighed:** Værktøjet er designet til netværksdiagnostik for mennesker, så det viser tid, TTL, tab‑procent osv., så man hurtigt kan vurdere forbindelsens kvalitet.
    - **Fejlfinding:** RTT og tab‑statistik hjælper med at identificere forsinkelse, pakketab eller routing‑problemer, som RFC 792 alene ikke giver.
    - **Kompatibilitet:** Forskellige operativsystemer og implementeringer kan variere i standard‑felter; ping udvider derfor med ekstra felter for at give en ensartet oplevelse på tværs af platforme.


*Har valgt at springe lidt over bonus-opgaverne og reflektionsspørgsmålene*
