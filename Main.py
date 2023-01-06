from Classes import *

heavyOrdinance = HeavyOrdinance()
heavyOrdinance.main()

#def main():
#
#    pygame.init()
#
#    res = (1000, 380)
#    screen = pygame.display.set_mode(res)
#
#    exit = False
#    while(not exit):
#
#        events = pygame.event.get()
#        for evt in events:
#            if (evt.type == pygame.QUIT):
#                exit = True
#
#        screen.fill((0, 0, 20))
#
#        mouse_button = pygame.mouse.get_pressed()
#        cursor_color = (0, 200, 200)
#
#        if (mouse_button[0]):
#            cursor_color = (200, 200, 0)
#        elif (mouse_button[2]):
#            cursor_color = (0, 200, 0)
#
#        mouse_pos = pygame.mouse.get_pos()
#        pygame.draw.circle(screen, cursor_color, mouse_pos, 5, 5)
#
#        pygame.display.flip()
#
#main()