**Afsnit 1‑2 – Introduktion & meddelelsesformater**

- **Formål:** ICMP er en integreret del af IP og bruges til at give feedback om fejl eller kontrolinformation i netværket. Det gør IP‑kommunikationen mere håndterbar, men garanterer ikke pålidelig levering.
- **Grundlæggende struktur:** ICMP‑meddelelser kapsles ind i en almindelig IP‑pakke. Det første oktet i datadelen er _type‑feltet_; værdien bestemmer resten af formatet. Felter mærket “unused” skal sættes til nul ved afsendelse.
- **IP‑header‑felter (relevant for ICMP):** version = 4, IHL, TOS = 0, total‑længde, identifikation/flags/fragment‑offset, TTL (skal være mindst så mange hop som pakken skal gennemløbe), protokol = 1 (ICMP), header‑checksum.
- **Adressefelter:** _source address_ er adressen på den gateway/host, der genererer ICMP‑meddelelsen; _destination address_ er adressen på den host/gateway, som skal modtage den.

---

**Afsnit 3 – Echo & Echo‑relay**  
_(Selvom teksten du har givet ikke indeholder den fulde beskrivelse, er echo‑meddelelserne de eneste ICMP‑typer, der ikke rapporterer fejl, men bruges til “ping”.)_

- **Type = 8 (Echo‑request)** og **type = 0 (Echo‑reply)**.
- Formålet er at teste, om en anden host kan nås, og måle round‑trip‑tid.
- Meddelelsen indeholder et identifier‑ og sekvensnummer samt valgfri data, som skal returneres uændret.

---

**Afsnit 4‑5 – Destination Unreachable & Time Exceeded**

|Meddelelse|Type|Kode|Hovedpunkt|
|---|---|---|---|
|**Destination Unreachable**|3|0‑5|Angiver, hvorfor en pakke ikke kan leveres (netværk, host, protokol, port, fragmentering nødvendig, source‑route fejlet).|
|**Time Exceeded**|11|0‑1|Sendes når TTL‑værdien udløber (kode 0) eller når fragment‑genopbygningstid overskrides (kode 1).|

- Begge meddelelser indeholder: checksum, et _unused_‑felt, samt den oprindelige IP‑header + de første 64 bit af den oprindelige datagram‑payload (så modtageren kan matche med den korrekte proces).
- Beskrivelsen understreger, at kun gateway’er sender “Destination Unreachable” med koder 0, 1, 4, 5, mens værter også kan sende koder 2 og 3. For “Time Exceeded” kan gateway’er sende kode 0, mens værter kan sende kode 1.

---

**Afsnit 6‑7 – Parameter Problem & Source Quench**

|Meddelelse|Type|Kode|Hovedpunkt|
|---|---|---|---|
|**Parameter Problem**|12|0|Angiver, at et felt i IP‑headeren er ugyldigt. _Pointer_-feltet peger på den præcise byte, hvor fejlen blev opdaget.|
|**Source Quench**|4|0|Anmoder afsenderen om at reducere trafikhastigheden, fordi en gateway eller host mangler bufferplads eller modtager for mange pakker.|

- Begge meddelelser bruger samme grundlæggende layout: type, kode, checksum, et _unused_‑ eller _pointer_‑felt, samt den originale IP‑header + 64 bit af data.
- _Source Quench_ kan udsendes både af gateway’er og værter; den fungerer som en “back‑off”‑signal, så afsenderen gradvist kan øge hastigheden igen, når belastningen falder.

---

**Kort opsummering**

- **Intro & formater** beskriver, hvordan ICMP er bygget oven på IP, og hvilke felter der er obligatoriske.
- **Echo** er den eneste “positiv” ICMP‑type, brugt til ping‑test.
- **Destination Unreachable** og **Time Exceeded** giver detaljeret feedback om, hvorfor en pakke ikke kan leveres eller er udløbet.
- **Parameter Problem** peger på specifikke fejl i IP‑headeren, mens **Source Quench** er et flow‑kontrolsignal for at forhindre overbelastning.

Hvis du har brug for yderligere uddybning af nogen af sektionerne – f.eks. konkrete eksempler på kode‑værdier eller typisk anvendelse i netværksdiagnostik – så sig endelig til!