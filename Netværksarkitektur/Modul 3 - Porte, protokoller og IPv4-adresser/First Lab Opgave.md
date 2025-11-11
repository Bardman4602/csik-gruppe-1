#csik #netværksarkitektur #opgaver 


![[01_lab_Your_first_network_DK.pdf]]

## Besvarelse
### Del 1
#### Ping:
![[PingGeneralFailure.png]]

#### ipconfig
![[IPConfig.png]]

#### Observationer
- Alle lys blinker
- Vi bruger en switch og ethernet kabel

#### ipconfig 2
![[IPConfig2.png]]

##### Subnet: 
255.255.0.0

#### IP-table

| Navn   | IPv4            | Subnet Mask | MAC               |
| ------ | --------------- | ----------- | ----------------- |
| Mads   | 169.254.55.148  | 255.255.0.0 | 00-E0-4C-68-00-28 |
| Daniel | 169.254.173.11  | 255.255.0.0 | 20-7B-D2-8F-AF-BB |
| Nathan | 169.254.138.222 | 255.255.0.0 | 20-7B-D2-CD-06-A2 |
| Jonas  | 169.254.249.4   | 255.255.0.0 | 84-BA-59-E0-BB-AF |

#### Spørgsmål
![[Spørgsmål1.png]]
- Burned-in
- Subnet er, MAC og IPv4 er forskellige

#### Ping test 2 (Nathan)
![[Ping2.png]]

![[PingNathan2.png]]

#### Spørgsmål 2 - APIPA
![[Spørgsmål2.png]]
- En automatisk service fra windows og andre OS'er, som fordeler IP-adresser til enheder på netværket, når DHCP ikke er tilgængelig.
	- Adresserne vil altid være mellem 169.254.0.1 - 169.254.255.254
	- 4-bit

#### Spørgsmål 3 - Opsamling del 1
![[OpsamlingSpørgsmål1.png]]
- En Switch - dens formål at få forbundne enheder til at snakke sammen
- Enheder på netværket
- Kablerne er twistede indeni for at undgå at opfange signaler fra andre kabler
- 169.254.0.1 - 169.254.255.254
- For at give credit, til den person som originalt har fået ideen. En citation med andre ord. 

### Del 2

| Name   | OS         | MAC               | APIPA IPv4      | Subnet mask (APIPA) | Static IPv4  | Subnet (Static) |
| ------ | ---------- | ----------------- | --------------- | ------------------- | ------------ | --------------- |
| Mads   | Windows 11 | 00-E0-4C-68-00-28 | 169.254.55.148  | 255.255.0.0         | 192.168.8.4  | 255.255.255.0   |
| Daniel | Windows 11 | 20-7B-D2-8F-AF-BB | 169.254.173.11  | 255.255.0.0         | 192.168.8.18 | 255.255.255.0   |
| Nathan | Windows 11 | 20-7B-D2-CD-06-A2 | 169.254.138.222 | 255.255.0.0         | 192.168.8.22 | 255.255.255.0   |
| Jonas  | Windows 11 | 84-BA-59-E0-BB-AF | 169.254.249.4   | 255.255.0.0         | 192.168.44   | 255.255.255.0   |

#### arp -a opgave
![[First Lab Opgave.png]]

![[arm 2.2.png]]

### Afslutningsspørgsmål:
![[Afslutningsspørgsmål.png]]

![[First Lab Opgave-1.png]]
