#csik #programmering 

# Slides og supplerende materiale
![[slides02.pdf]]

![[samarbejdsstrukturer02.pdf]]

## Noter til slides (AI)

## Syntaks for udtryk — hovedidéer
- Kode er i udgangspunkt **tekst**.  
- **Syntaks-regler** beskriver hvordan tekst skal opfattes som et træ (AST).  
- **Parsing / syntaksanalyse**: processen der oversætter tekst → træ.  



---

## Præcedens-regler
- Bestemmer rækkefølgen hvori operatorer binder.  
- Gør det muligt at **udelade parenteser** i mange tilfælde.  
- Brug reglerne for at tolke komplekse udtryk korrekt.

---
## Fra syntaks til semantik
- **Syntaks** = hvordan udtrykket er skrevet/struktureret.  
- **Semantik** = hvad udtrykket betyder; regler for hvordan værdien beregnes.  
- **Evaluering** = den konkrete beregningsproces (fx beregne deludtryk og operatorer i korrekt rækkefølge).

---

## Praktisk arbejdsflow (evaluering)
1. **Parse**: tekst → træ.  
2. **Evaluér subtræer**: beregn deludtryk (rekursivt).  
3. **Anvend operatorer** i henhold til præcedens/associativitet.  
4. **Resultat**: endelig værdi (tal, boolsk, dato, osv.).

![[Syntaks-træ.png]]

---

## Centrale begreber
- **Syntaks** – hvordan kode skrives og struktureres.  
- **Parsing (syntaksanalyse)** – oversættelse fra tekst til struktur.  
- **Præcedens-regler** – bestemmer rækkefølgen af evaluering.  
- **Semantik** – betydningen af udtryk, dvs. hvordan resultatet udregnes.  
- **Evaluering** – selve beregningen af værdien.  

---

## Hjemmearbejde
- Se på Canvas under **Plan for modul 02**.

---

# Opgaver
## [[Programmering M2 Opg 1]]
## [[Programmering M2 Opg 2]]
