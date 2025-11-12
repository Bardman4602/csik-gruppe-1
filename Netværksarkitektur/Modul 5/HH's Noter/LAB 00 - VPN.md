#csik #netværksarkitektur

> [!info] community plugin
> /* Denne note i obsidian benytter følgende community plugin:
> https://github.com/johansatge/obsidian-automatic-table-of-contents
> https://github.com/zsviczian/obsidian-excalidraw-plugin

```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

# Indledning

Som en del af undervisningen i faget Netværksarkitektur på professionsbacheloruddannelsen i Cybersikkerhed på Erhvervsakademi Aarhus er der udarbejdet en serie hands-on labs, som vil give jer indsigt i og understøtte læringen inden for netværk og Linux. 

De forskellige labs er bygget op omkring platformen Proxmox, som fungerer som hypervisor til at virtualisere de forskellige maskiner, I skal arbejde med. Adgang til Proxmox-serveren kan ske via direkte forbindelse på skolen gennem et dedikeret netværk eller via en VPN-løsning, således at I kan tilgå og arbejde på de forskellige labs hjemmefra eller remote.

Hovedadgangen sker via Proxmox WebGUI, som i skrivende stund er placeret på netværket it-sikkerhed, 10.160.0.0/24. 

## Server info – Proxmox Server PVE-super

**IP-adresse:** 10.160.0.250  
**WebGUI port:** 8006

## Adgang – bruger/password

Brugernavn og password til Proxmox-serveren udleveres i klassen eller via Canvas (LMS-system). 

**Almindelig fejlkilde:** Sørg for at vælge det korrekte `Realm` ved login. I skal altid benytte `Proxmox VE authentication server` – se figuren herunder.

![[Proxmox_login-realm.png]]
## VPN-profil

For at tilgå netværket, hvor Proxmox-serveren er placeret, skal I anvende en OpenVPN-profil, som roteres hvert semester og har samme levetid som semesteret. 

I skal downloade og installere en OpenVPN-client på jeres PC for at kunne tilgå netværket. Benyt community edition: 

https://openvpn.net/community/

I skrivende stund er version 2.6.15 den nyeste. Efter installation kan I tilgå VPN-forbindelsen via menuen `hidden icons` i taskbaren på Windows 11. I skal først importere den profil, som udleveres til jer som fil, før I kan forbinde/connect.

![[OpenVPN-icon_win11-dock.png]]

> [!warning] Vigtigt
> Det er af afgørende betydning, at denne profil kun anvendes af jer personligt. Har I mistanke om, at profilen er blevet kopieret og distribueret til personer uden relation til uddannelsen, skal I straks gøre jeres underviser opmærksom på dette, så adgangen kan nedtages.



