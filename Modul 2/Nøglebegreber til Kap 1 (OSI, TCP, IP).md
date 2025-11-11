#csik #begreber #netværksarkitektur

|Term|Definition|
|---|---|
|**Open Systems Interconnection (OSI) reference model**|En konceptuel ramme med 7 lag (Physical → Application) der beskriver, hvordan netværkskommunikation skal struktureres og standardiseres.|
|**Protocol Data Unit (PDU)**|Den samlede datastruktur, som et lag i OSI‑modellen sender til det næste lag; fx _frame_ i Data‑Link‑laget, _packet_ i Network‑laget og _segment_ i Transport‑laget.|
|**IP header**|Den del af en IP‑pakke, der indeholder kontrol‑ og routing‑information (version, source/destination‑adresse, TTL, checksum osv.).|
|**TCP header**|Den del af et TCP‑segment, der indeholder kontrol‑felter som kilde‑/destinations‑port, sekvens‑/acknowledgement‑nummer, vindues‑size, flag‑bits og checksum.|
|**UDP header**|Den del af en UDP‑datagram, der kun indeholder kilde‑/destinations‑port, længde og checksum – ingen pålidelighedsmekanismer.|
|**TCP flags**|En samling af enkelt‑bit‑felter i TCP‑headeren (SYN, ACK, FIN, RST, PSH, URG, ECE, CWR) der styrer forbindelse‑oprettelse, afslutning og kontrol.|
|**Payload**|De egentlige data, som transporteres i en PDU (det, der ligger “bag” header‑informationen).|
|**Maximum Transmission Unit (MTU)**|Den største størrelse (i bytes) en enkelt ramme/packet må have på et givet netværksmedie uden fragmentering.|
|**Current state**|Den aktuelle tilstand i en tilstands‑maskine (fx en TCP‑forbindelses‑state som _ESTABLISHED_ eller _CLOSED_).|
|**Modulation**|Processen hvor en digital eller analog informationssignal ændres (amplitude, frekvens eller fase) for at blive sendt over et fysisk medium.|
|**State transition**|Skiftet fra én tilstand til en anden i en tilstands‑maskine (fx fra _LISTEN_ til _SYN‑RECEIVED_ i TCP).|
|**Cyclic Redundancy Check (CRC)**|En fejldetektionsteknik, hvor en kort checksum beregnes over data‑bits; modtageren kan opdage fejl ved at sammenligne checksummen.|
|**Physical layer (OSI)**|Lag 1 – håndterer transmission af rå bits over fysiske medier (kabler, fibre, radiobølger).|
|**Data link layer (OSI)**|Lag 2 – organiserer bits i rammer, håndterer MAC‑adresser, fejlkontrol (CRC) og flow‑control på lokalt netværk.|
|**Network layer (OSI)**|Lag 3 – ansvarlig for logisk adressering og routing af pakker mellem netværk (IP).|
|**Transport layer (OSI)**|Lag 4 – leverer end‑to‑end‑kommunikation, pålidelighed (TCP) eller hurtighed (UDP).|
|**Session layer (OSI)**|Lag 5 – etablerer, vedligeholder og afslutter sessioner mellem applikationer.|
|**Presentation layer (OSI)**|Lag 6 – håndterer datakonvertering, kryptering og komprimering (f.eks. TLS, JPEG).|
|**Application layer (OSI)**|Lag 7 – grænsefladen til bruger‑applikationer; protokoller som HTTP, SMTP, DNS.|
|**Network interface layer**|Det lag i TCP/IP‑modellen, der svarer til OSI’s Physical + Data‑Link‑lag; håndterer hardware‑adresser og fysisk transmission.|
|**Internet layer (TCP/IP stack)**|Det lag i TCP/IP‑modellen, svarende til OSI’s Network‑lag; primært IP‑routing og adressering.|
|**Transport layer (TCP/IP stack)**|Samme funktion som OSI’s Transport‑lag; implementerer TCP og UDP.|
|**Application layer (TCP/IP stack)**|Øverst i TCP/IP‑stakken; omfatter protokoller som HTTP, FTP, DNS, SMTP osv.|
|**Time‑Division Multiplexing (TDM)**|En teknik, hvor flere digitale signaler deles på samme fysiske kanal ved at tildele hver sin tids‑slot.|
|**Transmission Control Protocol (TCP)**|En pålidelig, forbindelsesorienteret transportprotokol, der garanterer ordnet levering, flow‑control og retransmission.|
|**User Datagram Protocol (UDP)**|En upålidelig, forbindelsesfri transportprotokol, der sender datagrammer uden garantier for levering eller rækkefølge.|
|**TCP/IP stack**|Den samlede samling af protokoller (Application, Transport, Internet, Network Interface) der udgør internettets grundlæggende kommunikationsmodel.|

## [[Framing (data-link laget) (over-entusiastisk AI)]]
