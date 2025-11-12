#csik #netværksarkitektur #begreber

*side 109-165 i pdf*

|Term|Definition|
|---|---|
|**Local Area Network (LAN)**|Et netværk, der dækker et begrænset geografisk område (fx hjem, kontor eller bygning) og typisk bruger Ethernet eller Wi‑Fi.|
|**Wide Area Network (WAN)**|Et netværk, der strækker sig over store afstande (regioner, lande eller globalt) og forbinder flere LAN‑ eller MAN‑segmenter via offentlige eller private forbindelser.|
|**Campus Area Network (CAN)**|Et netværk, der dækker et universitets‑ eller virksomhedskompus (flere bygninger på et samlet område) og ofte kombinerer flere LAN‑segmenter.|
|**Metropolitan Area Network (MAN)**|Et netværk, der dækker en hel storby eller region (typisk 10–50 km) og bruges til at forbinde flere LAN‑ eller CAN‑segmenter.|
|**Personal Area Network (PAN)**|Et meget lille netværk (op til et par meter) omkring en enkelt person, f.eks. Bluetooth‑ eller Zigbee‑forbindelser mellem telefon, headset og wearables.|
|**Wireless Local Area Network (WLAN)**|En trådløs version af et LAN, typisk baseret på Wi‑Fi‑standarderne (802.11a/b/g/n/ac/ax).|
|**Storage Area Network (SAN)**|Et specialiseret høj‑hastigheds‑netværk, der giver blok‑baseret adgang til lagerenheder (diskarrays, tape libraries) for servere.|
|**Logical topology**|Den måde, data flyder gennem netværket (f.eks. bus, ring, stjerne) uafhængigt af den fysiske kabelføring.|
|**Physical topology**|Den faktiske fysiske layout af kabler, enheder og forbindelser i netværket.|
|**Bus topology**|Alle enheder er forbundet til en enkelt fælles kommunikationslinje (bus); data sendes i begge retninger langs bussen.|
|**Ring topology**|Enheder er forbundet i en lukket cirkel; data bevæger sig i én eller begge retninger rundt i ringen.|
|**Star topology**|Alle enheder er forbundet til en central hub eller switch; kommunikationen går altid gennem denne centrale enhed.|
|**Hub‑and‑spoke topology**|En variant af stjernetopologi, hvor en central “hub” (oftest et datacenter) forbinder til flere “spokes” (fjernkontorer).|
|**Full‑mesh topology**|Hver node har en direkte forbindelse til alle andre noder; giver høj redundans men er dyrt at implementere.|
|**Partial‑mesh topology**|Kun nogle noder er direkte forbundet med hinanden; balancerer mellem redundans og omkostninger.|
|**Hybrid topology**|Kombination af to eller flere topologier (fx stjerne‑plus‑ring) for at udnytte deres respektive fordele.|
|**Client/Server network**|En arkitektur, hvor klient‑enheder anmoder om tjenester fra dedikerede servere (f.eks. fil‑, printer‑ eller database‑servere).|
|**Peer‑to‑peer network (P2P)**|En decentraliseret arkitektur, hvor hver node både kan tilbyde og forbruge ressourcer uden central server.|
|**Demarcation point**|Det fysiske punkt, hvor leverandørens netværk (fx ISP) overdrages til kundens netværk; ofte en NID eller fiber‑connector.|
|**Smartjack**|En intelligent telefon‑ eller datakontakt, der kan diagnosticere linjestatus og give fjernsupport (ofte i VoIP‑miljøer).|
|**Network Function Virtualization (NFV)**|Virtualisering af netværksfunktioner (firewall, load balancer, router) som software‑baserede virtuelle maskiner i stedet for dedikeret hardware.|
|**Hypervisor**|Software‑lag, der muliggør kørsel af flere virtuelle maskiner (VM’er) på samme fysiske hardware (f.eks. VMware ESXi, KVM).|
|**Satellite**|Kommunikationslink, hvor data transmitteres via geostationære eller lav‑jordbane‑satellitter; bruges ofte i fjerntliggende områder.|
|**Digital Subscriber Line (DSL)**|En bredbåndsteknologi, der bruger eksisterende kobbertelefonlinjer til at levere internet med hastigheder fra ≈ 1 Mbit/s til > 100 Mbit/s.|
|**Cable**|Bredbåndsforbindelse, der benytter koaksial‑ eller hybrid‑fiberkabel‑infrastruktur (f.eks. DOCSIS‑standarder).|
|**Leased line**|En dedikeret, privat kommunikationslinje (ofte fiber) mellem to lokationer med fast båndbredde og lav latenstid.|
|**Metro‑optical**|Høj‑hastigheds‑optisk netværk, der dækker en by eller region (typisk 10 Gbps‑+).|
|**Software‑Defined Wide Area Network (SD‑WAN)**|En virtuel WAN‑arkitektur, der centraliseret styrer trafik over flere typer forbindelser (MPLS, broadband, LTE) via software‑defineret kontrolplan.|
|**Multiprotocol Label Switching (MPLS)**|En teknik, der bruger korte etiketter (labels) til at dirigere datapakker gennem et netværk, hvilket muliggør hurtig, QoS‑bevidst routing.|
|**Multipoint Generic Routing Encapsulation (mGRE)**|En udvidelse af GRE‑tunneling, der tillader én tunnel at forbinde flere endepunkter (multipoint) i stedet for kun to.|
|**vSwitch**|En virtuel switch, der forbinder virtuelle netværksinterface‑kort (vNIC’er) inden for en hypervisor‑host.|
|**Virtual Network Interface Card (vNIC)**|Et virtuelt netværkskort, som en VM bruger til at sende/modtage netværkstrafik via en vSwitch eller fysisk NIC.|
