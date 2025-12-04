import serial
import pygame
import pygame_textinput
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
ext_font = font
ext_text = ''

# definer hvilken port, BO-rate
ser=serial.Serial('COM3',9600,timeout=1)
#tilfældigt pygame lort
clock = pygame.time.Clock()

#ser.write("tekst".encode("utf-8"))
#ser.write(bytes([0x00,0xFF]))
#ser.write(bytes([0,255]))

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