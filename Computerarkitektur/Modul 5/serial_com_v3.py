import serial
import pygame
import pygame_textinput
from serial.tools import list_ports

pygame.init()
#screen
screen_width = 500
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

#external tekst
ext_text = ''

# definer hvilken port, baudrate
ports = list_ports.comports()
if ports == []:
    raise ValueError('Du skal plugge usb dimsen ind (kig LINE 34)')
ser=serial.Serial('COM3',9600,timeout=1)
# DU SKAL ÆNDRE DET ↑ TIL DEN PORT DU BRUGER PÅ DIN PC (fx COM4, COM5 osv.), ELLERS VIRKER DET IKKE

#tilfældigt pygame lort
clock = pygame.time.Clock()


pos = (10,10)
while True:
    screen.fill((black))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 160))

    #recieve text
    if ser.in_waiting:
        recieve = ser.readline()
        recieve_str = recieve.decode('utf-8').strip()
        ext_text = recieve_str  
        
    please = font.render(f'{ext_text}', True, red)
    screen.blit(please, pos)

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        #if user presses enter, send input through usb port and clear textinput
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            ser.write(f"{textinput.value}".encode("utf-8"))
            textinput.value = ''
    pygame.display.update()
    clock.tick(60)