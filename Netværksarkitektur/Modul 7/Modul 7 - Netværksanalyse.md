#csik #netværksarkitektur 

## Kopieret fra Canvas:
**Hvorfor?**

Netværksanalyse er fundamentet for at forstå, hvordan data bevæger sig gennem en organisations infrastruktur – og dermed også hvordan angribere kan udnytte denne bevægelse. Derfor er evnen til at analysere netværkstrafik afgørende for at kunne identificere anomalier, opdage igangværende angreb og forstå et systems normale adfærd.

Når du kan læse og fortolke netværkspakker, kan du se forskellen mellem legitim trafik og potentielle trusler som dataexfiltration, command-and-control kommunikation eller lateral movement.

Netværksanalyse giver dig desuden indsigt i, hvordan forskellige sikkerhedsløsninger fungerer på protokolniveau – fra firewalls til IDS/IPS-systemer – hvilket er essentielt for både at konfigurere, fejlfinde og optimere disse værktøjer.

_**Helt enkelt: Uden en forståelse for netværksanalyse arbejder vi i blinde, når vi skal beskytte digitale systemer.**_

# Slides
![[CSIK-network-analyse.pptx]]

## Noter til slides (ChatGPT):

### TCP/IP – Genopfriskning

#### TCP/IP Networking Model
- Historisk udvikling: proprietary modeller → åbne TCP/IP-standarder.
- To TCP/IP modeller:
  - **TCP/IP architectural model**  
  - **TCP/IP protocol model**

#### Centrale protokoller
- **HTTP** – klient/serverscenarier (GET request → reply → datatransport).  
- **TCP** – leverer:
  - Error-recovery  
  - Flow control  
  - Pålidelig datatransport  
- **IP** – routing og adressering  
- **Ethernet** – fysisk og datalink lag i LAN

#### Layer-interaktion
- **Same-layer interaction:** Protokoller på samme lag kommunikerer virtuelt.  
- **Adjacent-layer interaction:** Overordnede/underordnede lag hjælper hinanden.  

---

### Dataencapsulation – Five Steps (TCP/IP)
1. Application data  
2. Transport segment (fx TCP)  
3. Network packet (IP)  
4. Data link frame (Ethernet)  
5. Bits på det fysiske medium  

**LH** = Link Header  
**LT** = Link Trailer  
→ Tilføjes i Ethernet-rammer for at muliggøre transport på datalinklaget.

---

### OSI-modellen – Genopfriskning

#### OSI-lagene
1. Physical  
2. Data Link  
3. Network  
4. Transport  
5. Session  
6. Presentation  
7. Application  

#### Eksempler på protokoller & enheder
- **Physical:** Kabler, hubs  
- **Data Link:** Ethernet, switches  
- **Network:** IP, routere  
- **Transport:** TCP, UDP  
- **Application:** HTTP, FTP, DNS  

OSI sammenholdt med TCP/IP viser, at TCP/IP’s øverste lag dækker **Application, Presentation, Session**.

---

### Videoøvelse – refleksion
Gruppeøvelsen lægger op til at diskutere:
- Hvilke elementer fra videoen man bemærkede  
- Hvad der overraskede  
- Om videoens indhold stadig er relevant i dag  
- Hvorfor/ hvorfor ikke  

---

### SOHO LAN (Small Office/Home Office)

#### Ethernet LAN – vigtige pointer
- Ethernet kan forwarde en frame over **flere forskellige linktyper**.  
- Elektriske signaler sendes i par (twisted pair) → ét par pr. transmissionsretning.  

#### Fysiske komponenter i en Ethernet-link
- Netværkskort  
- Twisted-pair kabler  
- RJ-45 stik og porte  
- Switches  
- Routere  

---

### Ethernet-kabling

#### Kabler & pinouts
##### Straight-through kabel (1:1)
- Bruges typisk mellem:
  - PC ↔ Switch  
  - Router ↔ Switch  

##### Crossover kabel (krydset)
- Bruges typisk mellem:
  - Switch ↔ Switch (hvis auto-MDI/MDIX ikke findes)  
  - PC ↔ PC  
  - Router ↔ Router  

##### Gigabit Ethernet (1000BASE-T)
- Benytter **4 par** (alle ledere)  
- Auto-MDI/MDIX gør ofte crossover unødvendig  

---

### Ethernet rammer og adresser

#### Frame format (IEEE 802.3)
- **Destination MAC**  
- **Source MAC**  
- **Type** (identificerer fx IPv4, ARP, IPv6)  
- **Payload**  
- **FCS** (Frame Check Sequence – fejlkontrol)

#### MAC-adresser
- 48-bit adresse  
- Unicast, multicast og broadcast  
- OUI (Organizationally Unique Identifier) identificerer producent  

---

### Central Wireshark-viden (fra introen)

#### Hvad man analyserer:
- Pakker (rammer), protokoller, flows  
- MAC → IP → TCP/UDP → Data  
- Flags, checksums og fejl  
- Træstruktur med lag (frame → Ethernet → IP → TCP/UDP → data)

#### Hvorfor bruge Wireshark?
- Fejlfinding  
- Sikkerhedsanalyse  
- Trafik-inspektion  
- Identifikation af angreb og misbrug  

---

### Nøglebegreber (kort forklaret)

| Begreb                  | Forklaring                                                                |
| ----------------------- | ------------------------------------------------------------------------- |
| **Frame**               | Datastruktur på datalink-laget (Ethernet).                                |
| **Packet**              | Datastruktur på netværkslaget (IP).                                       |
| **Segment**             | Datastruktur på transportlaget (TCP/UDP).                                 |
| **Encapsulation**       | Indpakning af data fra højere lag ind i protokoller fra lavere lag.       |
| **TCP 3-way handshake** | SYN → SYN/ACK → ACK (opretter forbindelse).                               |
| **MAC-adresse**         | Fysisk adresse på netværksinterface.                                      |
| **EtherType**           | Felt i Ethernet-frame der identificerer protokollen (fx 0x0800 for IPv4). |
| **OUI**                 | Første 24 bit af MAC → producent-ID.                                      |

---

### Praktiske elementer (fra lab-delen)
Selvom opgaver ikke beskrives, fremgår fokusområderne tydeligt:

- Wireshark opsætning  
- Indfangning af trafik (capture filters)  
- Analyse af HTTP, TCP, ARP, DNS, ICMP  
- Identifikation af unormal trafik  
- Forståelse af protokol-flow  
- Basic netværksfejlfinding  
- Brug af OSI/TCP-IP-lagmodeller til analyse  

---

### Takeaways
- Netværksanalyse kræver forståelse for **modellag, protokoller og trafikkens opbygning**.  
- Ethernet, TCP/IP og OSI er fundamentet for al netværkssikkerhed.  
- Wireshark er et **kritisk værktøj** til sikkerheds- og fejlanalyse.  
- For at forstå moderne angreb, skal man kunne læse trafik *lag for lag*.  
- Korrekt kabling, rammeformat og protokolforståelse = forudsætning for fejlfinding.  

[[Opgaver]]
