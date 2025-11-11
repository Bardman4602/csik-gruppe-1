#csik #netværksarkitektur #begreber 

På **Data‑Link‑laget** (OSI‑lag 2) er _framing_ processen, hvor de rå bits fra det fysiske lag pakkes ind i strukturerede **rammer** (frames). En ramme fungerer som en selv‑beskrivende “pakke”, så modtageren kan genkende, adskille og behandle de enkelte datapakker korrekt.

### Hvorfor er framing nødvendigt?

1. **Afgrænsning** – Angiver start‑ og slut‑punktet for hver datapakke, så modtageren ved, hvornår en ny ramme begynder.
2. **Fejlkontrol** – Indeholder feltdetektion (typisk en CRC‑checksum) så beskadigede rammer kan forkastes eller anmode om retransmission.
3. **Adressere** – Medfører kilde‑ og destinations‑MAC‑adresser, så kun den tiltænkte modtager accepterer rammen.
4. **Flow‑control** – Giver mulighed for at styre, hvor hurtigt data kan sendes (fx ved brug af pause‑frames i Ethernet).

### Typisk rammestruktur (eksempel: Ethernet)

```
+-----------+----------+----------+----------+-----------+
| Preamble  |  MAC‑src |  MAC‑dst |  Type/Len|  Payload  |
+-----------+----------+----------+----------+-----------+
| 7 bytes   | 6 bytes  | 6 bytes  | 2 bytes  | 46‑1500 B |
+-----------+----------+----------+----------+-----------+
|                     CRC (4 bytes)                      |
+--------------------------------------------------------+
```


- **Preamble** (og Start‑of‑Frame‑Delimiter) hjælper med synkronisering.
- **MAC‑adresser** identificerer afsender og modtager på link‑niveau.
- **Type/Length** angiver enten hvilken protokol der er indkapslet (f.eks. IPv4) eller længden af payload.
- **Payload** er den faktiske data (oftest et IP‑pakke‑segment).
- **CRC** (Cyclic Redundancy Check) giver fejldetektion.

### Andre framing‑metoder

- **HDLC / PPP** – Bruger flag‑bits (`01111110`) til at markere rammegrænser og bit‑stuffing for at undgå falske flag‑forekomster.
- **Token Ring** – Indkapsler data i en ramme med start‑/slut‑markører og en token‑kontrolmekanisme.
- **Wi‑Fi (IEEE 802.11)** – Har en MAC‑header, en frame‑body (payload) og en FCS (Frame Check Sequence) for CRC‑kontrol.

### Sammenfatning

Framing på datalink‑laget er den mekanisme, der **pakker**, **identificerer**, **kontrollerer** og **afgrænser** data, så de kan overføres på et fysisk medium på en pålidelig og struktureret måde. Uden korrekt framing ville modtageren ikke kunne skelne mellem individuelle datapakker, og netværkstrafikken ville hurtigt blive kaotisk.