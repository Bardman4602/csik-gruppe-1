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
password = b''
password_entered = False
pis = 'Skriv password (int fra 0-26):'

# definer hvilken port, baudrate
ser=serial.Serial('COM5',9600,timeout=1)
# DU SKAL ÆNDRE DET ↑ TIL DEN PORT DU BRUGER PÅ DIN PC (fx COM4, COM5 osv.), ELLERS VIRKER DET IKKE

#tilfældigt pygame lort
clock = pygame.time.Clock()


#caesar settings
alph = " abcdefghijklmnopqrstuvwxyzæøå,.? abcdefghijklmnopqrstuvwxyzæøå,.?"
key = 0
bla = []
blå = []

def scramble(user_input):
    for letter in user_input:
        scrambled_key = alph.index(letter) + key
        bla.append(alph[scrambled_key])
    scrambled = ''.join(bla)
    return scrambled

def unscramble(user_input):
    for letter in user_input:
        unscrambled_key = alph.index(letter) - key
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

    #password stuff
    if not password_entered:
        #password prompt
        password_prompt = font.render(pis, True, white)
        screen.blit(password_prompt, (10, 100))
        #skriv password ind
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if len(textinput.value) != 0:
                    password = int(textinput.value)
                    textinput.value = ''
                    password_entered = True




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
                ser.write(f"{textinput.value}".encode("utf-8"))
                textinput.value = ''
    pygame.display.update()
    clock.tick(60)