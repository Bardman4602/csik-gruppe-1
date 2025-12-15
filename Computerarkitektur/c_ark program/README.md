Programmet her bruger pygame til at lave et vindue, hvor man kan skrive med den anden pc der er forbundet.

# Moduler
Jeg har brugt et par moduler, så de skal også lige installeres først. Du **skal** køre de her kommandoer i dit virtual environment først:

pip install PySerial

pip install pygame

python3 -m pip install pygame-textinput

# Generel info
Man *skal* bruge en usb enhed der kan sende information frem og tilbage, ligesom den som Jonas gav os.

Jeg bruger en Caesar Cipher, hvor man selv skal inputte hvilket tal programmet bruger til at scramble beskederne

Programmet prompter en efter et kodeord, som den bruger til at 'scramble' og 'unscramble' teksten.
Begge computere skal skrive det samme kodeord, ellers bliver Caesar cipheren utydelig. As intended.

På linje 8, skal man manuelt ændre hvilken usb port du har set usb-enheden ind i. Hvis det er port 3, skal du skrive 'COM3' der hvor jeg har markeret det.

Det er kun specifikke characters der virker pga måden jeg har programmeret caesar cipheren. så ingen emojies eller hashtags

Programmet virker uden en anden pc på den anden side. men det er fedest med en makker.

Setuppet er lidt bøvlet, men det er det hele værd;) 
