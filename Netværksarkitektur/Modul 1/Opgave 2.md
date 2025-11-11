![[Opgave 2 - Netværk.png]]

#### Del 1
1. ipconfig fortæller dig om din ipadresse (IPv4 og IPv6), subnet, default gateway og DNS server adressen.
2. Denne er lidt mere detaljeret, og fortæller lidt flere oplysninger om ISP og de forskellige netværkskort og deres forbindelser
3. Mac / Fysisk adresse

#### Del 2
4. Vi får svar fra en IP inde fra google med en svartid og ttl(time to live)
5. 8.8.8.8 er googles DNS server.
6. samme type svar, men bare fra en anden ip.

#### Del 3
7. giver en oversigt om hvilke ip-adresser google ligger på og deres fysiske adresser
8. ![[nslookup 8.8.8.8.png]]
	1. Her får vi at vide at navnet er dns.google

#### Del 4
9. viser en øjebliksbillede over aktive forbindelser og overfladisk information om hvem der er på netværket.
10. Flere adresser i oversigten har ændret sig.


## Ekstra:
![[Opgave 2 - Powershell.png]]

#### Tryhard
1. Sammenligningen viser at PS er lidt mere beskrivelig og fortæller lidt mere om hardware. Den skærer også meget af det unødvendige fra, som du får med i cmd.
2. Meget det samme, bare mere detaljeret
3. Kort og simpel oversigt. Meget lettere at læse.
4. Bedre version af nslookup.
5. Bruges til at få og vise aktuelle TCP-forbindelser på en Windows PC

#### Reflektion
1. Powershell giver generelt et mere detaljeret output og er samtidig meget lættere at læse
2. cmd er nok lidt hurtigere, men til gengæld sværere at "filtrere" for brugbart info.
3. Alle ovenstående.

#csik #opgaver #netværksarkitektur