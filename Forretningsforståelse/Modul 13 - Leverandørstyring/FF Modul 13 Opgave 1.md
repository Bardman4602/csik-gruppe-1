#csik #forretningsforståelse #opgaver 

![[Pasted image 20251203090053.png]]

## SolarWinds-angrebet – Hurtige svar på spørgsmålene

## Om SolarWinds
Sikkerhedssoftware - Leverandører til
- U.S. Department of the Treasury [Wikipedia+1](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach?utm_source=chatgpt.com)    
- U.S. Department of State [CSO Online+1](https://www.csoonline.com/article/570537/the-solarwinds-hack-timeline-who-knew-what-and-when.html?utm_source=chatgpt.com)    
- Microsoft [SecurityWeek+1](https://www.securityweek.com/microsoft-energy-department-and-others-named-victims-solarwinds-attack/?utm_source=chatgpt.com)    
- FireEye [The HIPAA Journal+1](https://www.hipaajournal.com/sec-sues-solarwinds-2019-cyberattack/?utm_source=chatgpt.com)    
- U.S. Department of Homeland Security [Next7 IT+1](https://www.next7it.com/insights/what-happened-solarwinds-hack/?utm_source=chatgpt.com)

### 1. Hvad blev de ramt af (hvad gik galt)?
SolarWinds blev ramt af et **supply-chain angreb**, hvor trusselsaktører (knyttet til APT29/Cozy Bear) kompromitterede deres software‐build-miljø og indsatte en **backdoor (SUNBURST)** i Orion-opdateringerne. Kunder installerede dermed en trojaniseret version gennem helt legitime opdateringer.

Frank hævder at det var et dårligt password, som var skyld i angrebet, men det er ikke blevet bevist. Flere artikler skriver at en praktikant fik skylden for det, men det er ikke bekræftet, at faktisk var det der skete. Personligt hælder jeg til at det bare var nemt at skyde skylden på en praktikant, fremfor selv at tage ansvar. 🤷‍♂️

---

### 2. Hvilke sikkerhedsbegreber er i spil – herunder CIA?
**Confidentiality (Fortrolighed)**  
- Angriberne kunne indsamle data fra kompromitterede organisationer.

**Integrity (Integritet)**  
- SolarWinds’ officielle builds blev manipuleret.  
- Softwareopdateringer, som kunder stolede på, blev ændret uden deres viden.

**Availability (Tilgængelighed)**  
- Ikke det primære mål, men systemer måtte tages offline under undersøgelsen.

**Andre begreber:**  
- *Supply Chain Security*  
- *Zero Trust* (manglende kontrol gjorde angrebet muligt)  
- *Code Signing Misuse*  
- *Lateral Movement* hos ofrene  
- *Defense in Depth* (mange lag fejlede)

---

### 3. Hvad var konsekvensen?
- Over **18.000 organisationer** downloadede den kompromitterede opdatering.  
- Angriberne fik **persistente adgangsveje** til udvalgte højtprofilerede ofre (myndigheder, virksomheder).  
- Massive **databrud** og efterretningsmæssige konsekvenser.  
- Langvarige **omkostninger** til oprydning, genopbygning af trust og systemer.  
- SolarWinds’ omdømme og aktieværdi fik et stort slag.

---

### 4. Kunne kontroller have forhindret angrebet?
**Ja – flere typer kontroller kunne have reduceret risikoen:**

- Stram **adgangskontrol og segmentering** i build-miljøet.  
- *Zero Trust* model til både udviklings- og distributionspipeline.  
- **Hårdere overvågning** af build-systemer og code-signing processer.  
- **Reproducible builds** og *build integrity checks*.  
- Adskillelse af **signing-keys** og build-servere.  
- Avanceret **anomalidetektion** og log-analyse.  
- **SBOM (Software Bill of Materials)** for bedre indsigt i komponenter.

---

### 5. Hvad burde de forbedre?
- Sikring af hele CI/CD-pipeline (build, test, signering, deployment).  
- Implementere *Zero Trust* og strengere IAM-politikker.  
- Stærkere beskyttelse af code-signing-certifikater.  
- Kontinuerlig overvågning for ændringer i build-artefakter.  
- Bedre netværkssegmentering og MFA på alle udviklingssystemer.  
- Formelle **supply-chain-sikkerhedsrammer** (f.eks. NIST SSDF).

---

### 6. Andre sikkerhedsovervejelser?
- **Threat modeling** specifikt for supply-chain scenarier.  
- Krav om **verificering af tredjeparts-komponenter**.  
- Brug af **attestation** i build-processer.  
- Opdateret **incident response-plan** med fokus på softwarekæder.  
- Øget **transparens** og audit-muligheder i softwareproduktionsprocesser.

---

## Mere info fra MITRE
https://attack.mitre.org/campaigns/C0024/
