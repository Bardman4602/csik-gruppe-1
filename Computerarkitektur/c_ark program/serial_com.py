import serial
import pygame
import pygame_textinput
from serial.tools import list_ports


ports = list_ports.comports()
if ports == []:
    raise ValueError('Du skal plugge usb dimsen ind (SEE LINE 39)')

pygame.init()
#screen
screen_width = 600
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("UART comms")


#farver
white = (255,255,255)
black = (0,0,0)
green = (32, 194, 14)
red = (255,0,0)
font = pygame.font.SysFont("Cascadia code", 50)

#user text
textinput = pygame_textinput.TextInputVisualizer()
textinput.font_color = green
textinput.font_object = font

#misc. setting
ext_text = ''
password_entered = False
pis = 'Skriv password (int fra 0-36):'
counter = 0
liste = ['det skulle være en integer fra 0-36', 'kan du læse?', 'bro', 'INTEGER. 0-36.', 'jeg gir op', '']

# definer hvilken port, baudrate
ser=serial.Serial('COM4',9600,timeout=1)
# DU SKAL ÆNDRE DET ↑ TIL DEN PORT DU BRUGER PÅ DIN PC (fx COM4, COM5 osv.), ELLERS VIRKER DET IKKE

#tilfældigt pygame lort
clock = pygame.time.Clock()


#caesar settings
alph = " abcdefghijklmnopqrstuvwxyzæøå,.?1234567890 abcdefghijklmnopqrstuvwxyzæøå,.?1234567890"
key = 0


#caesar cipher scramble
def scramble(user_input):
    bla = []
    for letter in user_input:
        scrambled_key = alph.index(letter.lower()) + key
        bla.append(alph[scrambled_key])
    scrambled = ''.join(bla)
    return scrambled
#caesar cipher unscramble
def unscramble(user_input):
    blå = []
    for letter in user_input:
        unscrambled_key = alph.index(letter.lower()) - key
        blå.append(alph[unscrambled_key])
    unscrambled = ''.join(blå)
    return unscrambled


pos = (10,10)
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    screen.fill((black))

    

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 160))

    #prompt et password (hvilken key caesar cipheren bruger til at scramble) inden man kan sende beskeder
    if not password_entered:
        #password prompt
        password_prompt = font.render(pis, True, white)
        screen.blit(password_prompt, (10, 100))
        #skriv password ind
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if len(textinput.value) != 0:
                    if textinput.value.isdigit() and 0 <= int(textinput.value) <= 36:
                        key = int(textinput.value)
                        textinput.value = ''
                        password_entered = True
                    else:
                        textinput.value = ''
                        pis = liste[counter]
                        counter += 1
                        if counter == 6:
                            raise ValueError('Programmet gav op')
                        


#messaging 

    if password_entered:
    #recieve text
        if ser.in_waiting:
            recieve = ser.readline()
            recieve_str = recieve.decode('utf-8').strip()
            ext_text = unscramble(recieve_str)  
            
        please = font.render(ext_text, True, red)
        screen.blit(please, pos)

        for event in events:
            #if user presses enter, send input through usb port and clear textinput
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                caesar = scramble(textinput.value)
                ser.write(f"{caesar}".encode("utf-8"))
                textinput.value = ''
    pygame.display.update()
    clock.tick(60)