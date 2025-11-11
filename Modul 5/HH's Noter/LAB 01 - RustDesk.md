#csik #netværksarkitektur

# Lab 01: Installation og Konfiguration af Remote Desktop (RustDesk)

```table-of-contents
```

## Lab Information

**Titel:** Installation af RustDesk Remote Desktop  
**Estimeret tid:** 45-60 minutter  
**Forudsætninger:**

- Adgang til OpenVPN
- Proxmox login credentials
- Basal Linux kommandolinje kendskab

>[!warning] HUSK
LÆS alt igennem først og især [[#📝 Del 6 Dokumentation og Rapport]] inden i påbegynder lab

## Læringsmål

jrka

Efter gennemførelse af denne lab vil du kunne:

- Installere software på Linux via kommandolinjen
- Konfigurere remote desktop adgang
- Arbejde med netværksforbindelser i et virtualiseret miljø
- Dokumentere og fejlsøge installationsproblemer
- Teste og verificere netværkstjenester

---
## Teori

### Hvad er RustDesk?
https://rustdesk.com/

RustDesk er en open-source remote desktop løsning, der giver dig mulighed for at fjernstyre en computer. Det fungerer på tværs af platforme (Windows, Linux, macOS) og kan både bruges via internet og på lokale netværk.

https://rustdesk.com/docs/en/videos/
### Hvorfor RustDesk i dette lab?

- **Performance:** Bedre ydeevne end browser-baseret noVNC
- **Fleksibilitet:** Kan forbinde både via ID og direkte IP
- **Læring:** Praktisk erfaring med Linux software installation
- **Relevant:** Meget brugt værktøj i professionelle IT-miljøer
### Forbindelsesmetoder

RustDesk understøtter to primære måder at forbinde på:

1. **Via ID:** Unikt ID genereret ved installation (kræver relay server)
2. **Via IP:** Direkte forbindelse på lokalt netværk (hurtigere, ingen server nødvendig)

---
## Lab Miljø

### Netværksarkitektur

```

┌─────────────────┐
│  Din Laptop     │
│  (OpenVPN)      │
└────────┬────────┘
         │
    ┌────▼────────────────┐
    │  Proxmox Server     │
    │                     │
    │  ┌──────────────┐   │
    │  │  LAB PC      │   │
    │  │  (Xubuntu)   │   │
    │  │  vmbr0 + vX  │   │
    │  └──────────────┘   │
    └─────────────────────┘
```

### Gruppen's netværk

- **Internet interface:** vmbr0
- **Lab netværk:** vmbr100X (hvor X = dit gruppe nummer)
- **LAB PC IP:** `10.160.0.21X`
- **Standard credentials:** (får du af underviser)

---
## Forberedelse

### Tjekliste før start
- [ ] OpenVPN forbindelse etableret (se [[LAB 00 - VPN]])
- [ ] Proxmox login verificeret
- [ ] LAB PC's IP-adresse noteret: `10.160.0.21X`
- [ ] Download RustDesk til din egen laptop: https://rustdesk.com/
### Installer RustDesk på din laptop

1. Gå til https://rustdesk.com/
2. Download version til dit OS (Windows/Mac/Linux)
3. Installér programmet
4. Åbn RustDesk - du vil se dit eget ID

---
## Del 1: Start og Adgang til LAB PC

### Opgave 1.1: Forbind til Proxmox

1. Åbn browser og gå til Proxmox URL (får du af instruktør)
2. Login med dine credentials
3. Find din gruppe's LAB PC VM i listen
### Opgave 1.2: Start LAB PC

1. Højreklik på din VM
2. Vælg "Start"
3. Vent til status viser "running" (grøn pil)
### Opgave 1.3: Tilgå console

1. Klik på din VM
2. Vælg "Console" i menuen
3. noVNC console vindue åbner
4. Login med standard credentials (find disse i Notes under Summary)

> [!tip] noVNC kan være lidt langsom - det er derfor vi installerer RustDesk!

## Del 2: Installation af RustDesk på labPC

### Opgave 2.1: Download RustDesk

Åbn en terminal på LAB PC (Ctrl+Alt+T eller via menu) og kør:

```bash

# Gå til downloads folder

cd ~/Downloads

# Download seneste RustDesk version

wget https://github.com/rustdesk/rustdesk/releases/download/X.Y.Z/rustdesk-X.Y.Z-x86_64.deb
```

**Forventet output:**

```

Saving to: 'rustdesk-1.3.3-x86_64.deb'

rustdesk-1.3.3-x86_64.deb  100%[================================>]   XX.XX MB

```


> **Dokumentation:** Notér download størrelse og tid i din lab rapport

### Opgave 2.2: Installér RustDesk pakken

```bash
# Installér .deb pakken
sudo apt update

sudo apt install libxdo3
sudo apt install gstreamer1.0-pipewire

sudo dpkg -i rustdesk-1.3.3-x86_64.deb
```

**Muligt problem:** Hvis du får fejl om manglende dependencies, kør:

```bash
sudo apt install -f
```

Dette vil automatisk installere manglende pakker.

### Opgave 2.3: Verificer installation

```bash
# Check om RustDesk er installeret
which rustdesk
  
# Start RustDesk
rustdesk &

```

RustDesk vinduet skulle nu åbne!

>[!FAQ] **❓ Spørgsmål:** Hvad betyder `&` i kommandoen ovenfor? noter svar og diskussion i jeres labrapport

---

## Del 3: Konfiguration af RustDesk

### Opgave 3.1: Notér dit RustDesk ID

Når RustDesk åbner, vil du se:

- Et **unikt ID** (f.eks. `123 456 789`)
- En **password** sektion

**Dokumentér følgende:**

```
LAB PC RustDesk ID: ___________________
LAB PC IP adresse:  10.160.0.21X
Gruppe nummer:      _X_
```

### Opgave 3.2: Sæt et permanent password

1. Klik på "Settings" (⚙️ ikon)
2. Gå til "Security" tab
3. Find "Password" sektionen (set permanent password)
4. Sæt password: (brug et password I kan bruge fælles i gruppen) fx. `labpc2025`
5. Klik "Apply"

> **🔒 Sikkerhed:** I et produktionsmiljø ville du bruge et stærkere password!

### Opgave 3.3: Aktivér Direct IP Access

Dette er vigtigt for lokal netværksforbindelse!

1. I "Settings" → "Security"
2. Find "Direct IP Access"
3. Sæt flueben ved "Enable Direct IP Access"
4. Klik "Apply"
### Opgave 3.4: Verificer netværksindstillinger

1. Gå til Terminal (Ctrl+Alt+T eller via menu)
2. Verificer at du kan se begge netværksinterfaces
	```bash
	ip -c a
	```
3. Noter IP-adresserne du ser

**Forventet:**
- `eth0` eller `ens18`: Internet forbindelse (10.160.0.21X)
- `eth1` eller `ens19`: Lab netværk (ikke nogen IP adresse endnu) 

---

## Del 4: Test Remote Forbindelse

### Opgave 4.1: Forbind via RustDesk ID

Fra din egen laptop:

1. Åbn RustDesk på en laptop i gruppen som ikke er tilkoblet via OpenVPN
2. Indtast LAB PC's RustDesk ID i feltet
3. Klik "Connect"
4. Indtast password: `labpc2025` eller hvad i valgte i gruppen

**Forventet resultat:** Du ser LAB PC's desktop i et nyt vindue
  
> **⏱️ Performance test:** Notér forbindelsestid og responstid

### Opgave 4.2: Forbind via Direct IP

Test den hurtigere lokale forbindelse:

1. Disconnect fra ID-forbindelsen
2. I RustDesk på din laptop, indtast: `10.160.0.21X` (dit gruppe nummer)
3. Klik "Connect"
4. Indtast password

**Forventet resultat:** Hurtigere forbindelse end via ID

> **📊 Sammenligning:** Mærk forskellen i responstid mellem ID og IP forbindelse
### Opgave 4.3: Test funktionalitet

Når du er forbundet, test følgende:

- [ ] Flyt musen rundt - følger den med?
- [ ] Åbn en applikation (f.eks. Firefox)
- [ ] Skriv noget tekst
- [ ] Kopier tekst fra din laptop og indsæt på LAB PC
- [ ] Test filoverførsel (drag & drop en lille fil)
  
---

## Del 5: Netværksanalyse

### Opgave 5.1: Undersøg RustDesk porte

På LAB PC, åbn terminal:
  
```bash
# Se hvilke porte RustDesk lytter på
sudo netstat -tulpn | grep rustdesk
```

eller med nyere systemer:  

```bash
sudo ss -tulpn | grep rustdesk
```

**Dokumentér:**

- Hvilke porte ser du?
- TCP eller UDP?
- På hvilke IP-adresser lytter den?

### Opgave 5.2: Test netværksforbindelse

```bash
# Ping test til din laptop (find din laptop IP først)
ping -c 4 <din-laptop-ip>

# Tjek routing table
ip route show

# Se alle netværksinterfaces
ip addr show
```

**Analyser:**

- Hvilken route bruges til at nå din laptop?
- Hvor mange hop er der mellem LAB PC og din laptop?  

---

## 📝 Del 6: Dokumentation og Rapport

### Hvad skal dokumenteres?

Lav en grupperapport (kan være i Markdown) med følgende:
#### 6.1 Installation

- Problemer under installation?
- Løsninger du fandt?
- Tid brugt på installation?
#### 6.2 Konfiguration

```markdown
## Konfigurationsdetaljer
- RustDesk ID: [dit ID]
- LAB PC IP: aaa.bbb.ccc.ddd
- Direct IP Access: Enabled ✅
```

#### 6.3 Netværksanalyse

- Output fra netstat/ss kommando
- Liste over åbne porte
- Netværksdiagram over din opsætning

#### 6.4 Performance sammenligning

| Forbindelsestype  | Forbindelsestid | Responstid  | Noter |
| ----------------- | --------------- | ----------- | ----- |
| Via ID            |                 |             |       |
| Via Direct IP     |                 |             |       |
| noVNC (reference) |                 |             |       |

#### 6.5 Refleksion

- Hvad lærte I?
- Hvilken forbindelsesmetode foretrækker I og hvorfor?
- Hvad ville I gøre anderledes næste gang?

---

