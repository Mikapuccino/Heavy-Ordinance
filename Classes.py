import pygame
import math
from pygame.math import Vector2
from pygame.transform import rotozoom
from Functions import *


UP = Vector2(0, -1)

class HeavyOrdinance:

    def __init__(self):

        self.initPygame()
        self.screen = pygame.display.set_mode((1000, 380))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.phrase = ""
        self.cannonballs = []
        self.player = Player((500, 190), self.cannonballs.append)
        self.boats = []

        self.start = False
        self.mouse_button = None
        self.mouse_pos = None
        self.cooldown = True
        self.lastShot = 0
        self.lost = False
        self.lostTime = 0
        self.score = 0
        self.show = True
        self.timeLeaderboard = 0
        self.end = True

        self.up_pressed = False
        self.down_pressed = False

    

    def get_GameObject(self):

        gameObjects = [*self.cannonballs, *self.boats]

        if self.player:
            gameObjects.append(self.player)

        return gameObjects

    def main(self):

        while True:

            if self.end == True and self.start == False:

                self.main_menu()

            if self.end == False and self.start == True:

                self.inputLogic()
                self.gameLogic()
                self.draw()

    def initPygame(self):

        pygame.init()

    def main_menu(self):

        self.start = False

        self.screen.fill((0, 0, 20))
        text_in_line(self.screen, "HEAVY ORDINANCE", self.font, 40, "white")
        text_in_line(self.screen, "START", self.font, 280)
        text_in_line(self.screen, "EXIT", self.font, 340)

        if self.up_pressed == True:

            text_in_line(self.screen, "START", self.font, 280, "tomato")

        if self.down_pressed == True:

            text_in_line(self.screen, "EXIT", self.font, 340, "tomato")

        events = pygame.event.get()

        for evt in events:
            if (evt.type == pygame.QUIT):
                quit()

        if pygame.key.get_pressed()[pygame.K_UP] == True:
            text_in_line(self.screen, "START", self.font, 280, "tomato")
            text_in_line(self.screen, "EXIT", self.font, 340)
            self.up_pressed = True
            self.down_pressed = False

        if pygame.key.get_pressed()[pygame.K_DOWN] == True:
            text_in_line(self.screen, "EXIT", self.font, 340, "tomato")
            text_in_line(self.screen, "START", self.font, 280)
            self.down_pressed = True
            self.up_pressed = False

        if pygame.key.get_pressed()[pygame.K_SPACE] == True:

            if self.down_pressed == True:
                quit()

            if self.up_pressed == True:
                self.start = True
                self.end = False
                self.restart()

        pygame.display.flip()
        self.clock.tick(60)

    def inputLogic(self):

        events = pygame.event.get()

        if self.cooldown == False:

            timePassed = pygame.time.get_ticks()

            if timePassed >= self.lastShot + 1000:

                self.cooldown = True

        for evt in events:
            if (evt.type == pygame.QUIT):
                quit()

            if self.phrase != "GAME OVER":

                if evt.type == pygame.MOUSEBUTTONUP and self.cooldown == True:

                    self.player.shoot()
                    self.cooldown = False
                    self.lastShot = pygame.time.get_ticks()
        


    def gameLogic(self):

        for gameObject in self.get_GameObject():

            gameObject.move()

        for cannonball in  self.cannonballs[:]:
            timePassed = pygame.time.get_ticks()
            cannonballTime = cannonball.timeShot
            if timePassed >= cannonballTime + 4000:
                self.cannonballs.remove(cannonball)
                break

    def draw(self):

        self.screen.fill((0, 0, 20))

        for gameObject in self.get_GameObject():
            gameObject.draw(self.screen)

        if self.phrase == "GAME OVER":
            self.gameOver()

        pygame.display.flip()
        self.clock.tick(60)

    def gameOver(self):
        self.screen.fill((0, 0, 20))

        if self.lost == False:
            self.lostTime = pygame.time.get_ticks()
            self.lost = True

        timePassed = pygame.time.get_ticks()
        
        ending = False

        text(self.screen, self.phrase, self.font)

        if timePassed >= self.diedTime + 4000:

            self.screen.fill((0, 0, 20))
            
            # Opens leaderboard file and detects the scores in it

            leaderboard = open("Leaderboard.txt", "r")

            skip = 2
            for i in range(skip):
                leaderboard.readline()
            score1 = leaderboard.readline()
            score1 = score1.split(" ")
            score2 = leaderboard.readline()
            score2 = score2.split(" ")
            score3 = leaderboard.readline()
            score3 = score3.split(" ")
            score4 = leaderboard.readline()
            score4 = score4.split(" ")
            score5 = leaderboard.readline()
            score5 = score5.split(" ")
            score6 = leaderboard.readline()
            score6 = score6.split(" ")
            score7 = leaderboard.readline()
            score7 = score7.split(" ")
            score8 = leaderboard.readline()
            score8 = score8.split(" ")
            score9 = leaderboard.readline()
            score9 = score9.split(" ")
            score10 = leaderboard.readline()
            score10 = score10.split(" ")

            leaderboard.close()

            # Detects if the player got a better score than what is on the leaderboard

            if self.score > int(score1[1]):
                self.editLeaderboard(3)
                self.score = 0
            
            if self.score > int(score2[1]):
                self.editLeaderboard(4)
                self.score = 0
            
            if self.score > int(score3[1]):
                self.editLeaderboard(5)
                self.score = 0
            
            if self.score > int(score4[1]):
                self.editLeaderboard(6)
                self.score = 0
            
            if self.score > int(score5[1]):
                self.editLeaderboard(7)
                self.score = 0
            
            if self.score > int(score6[1]):
                self.editLeaderboard(8)
                self.score = 0
            
            if self.score > int(score7[1]):
                self.editLeaderboard(9)
                self.score = 0
            
            if self.score > int(score8[1]):
                self.editLeaderboard(10)
                self.score = 0

            if self.score > int(score9[1]):
                self.editLeaderboard(11)
                self.score = 0

            if self.score > int(score10[1]):
                self.editLeaderboard(12)
                self.score = 0

            # Displays the leaderboard, with the new score if the player got a higher score
            # than one that was already on the leaderboard

            leaderboard = open("Leaderboard.txt", "r")

            text_in_line(self.screen, leaderboard.readline(), self.font, 40, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 80, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 120, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 160, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 200, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 240, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 280, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 320, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 360, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 400, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 440, "white")
            text_in_line(self.screen, leaderboard.readline(), self.font, 480, "white")

            leaderboard.close()
            
            while ending == False:
                
                ending = self.showLeaderboard(ending)

            if ending == True:
            
                self.end = True
                self.start = False

    # This function is used to edit the leaderboard when the player
    # got a higher score than one that is already on it

    def editLeaderboard(self, lineEdit):

        x = 0

        playerName = input("Input your name: ")
        leaderboard = open("Leaderboard.txt", "r")
        contents = leaderboard.readlines()

        # Edits the leaderboard to put the player initials and score on the proper
        # placement and moves every score below it, also removing the previous score in last place

        while (lineEdit + x) < len(contents):

            bottomUp = len(contents) - x - 1

            if x == 0:
                contents[bottomUp] = contents[bottomUp - 1].strip()
            if x > 0:
                contents[bottomUp] = contents[bottomUp - 1]

            x = x + 1

        contents[lineEdit - 1] = playerName[:3] + ": " + str(self.score) + "\n"
        leaderboard.close()
        leaderboard = open("Leaderboard.txt", "w")
        leaderboard.writelines(contents)
        leaderboard.close()
    
    # This function displays the leaderboard for 6 seconds

    def showLeaderboard(self, ended):

        timePassed = pygame.time.get_ticks()
        
        if self.show == True:
            
            self.timeLeaderboard = pygame.time.get_ticks()
            self.show = False
            
        if timePassed >= self.timeLeaderboard + 6000:

            self.phrase = ""
            ended = True
            return(ended)

    def restart(self):

        self.phrase = ""
        self.cannonballs = []
        self.player = Player((500, 190), self.cannonballs.append)
        self.boats = []

        self.cooldown = True
        self.lastshot = 0
        self.lost = False
        self.lostTime = 0
        self.score = 0
        self.show = True
        self.timeLeaderboard = 0

class GameObject:

    def __init__(self, pos, sprite, velocity):

        self.pos = Vector2(pos)
        self.sprite = sprite
        self.velocity = Vector2(velocity)
        self.radius = sprite.get_width() / 2

    def draw(self, surface):

        blitPos = self.pos - Vector2(self.radius)
        surface.blit(self.sprite, blitPos)

    def move(self):

        self.pos = self.pos + self.velocity

    def collision(self, otherObj):

        distance = self.pos.distance_to(otherObj.pos)
        return distance < self.radius + otherObj.radius

class Player(GameObject):

    CannonballSpeed = 2

    def __init__(self, pos, create_cannonball_callback):
        self.create_cannonball_callback = create_cannonball_callback
        self.direction = Vector2(UP)
        super().__init__(pos, load_sprite("PlayerShip"), Vector2(0))

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()
        angle = 360 - math.atan2(mouse_pos[1] - 190, mouse_pos[0] - 500) * 180 / math.pi
        rotatedSurface = rotozoom(self.sprite, angle, 1.0)
        rotatedSurfaceSize = Vector2(rotatedSurface.get_size())
        blitPos = self.pos - rotatedSurfaceSize * 0.5
        self.direction.rotate_ip(angle)
        surface.blit(rotatedSurface, blitPos)
    
    def shoot(self):

        #mouse_pos = pygame.mouse.get_pos()
        #angle = 360 - math.atan2(mouse_pos[1] - 190, mouse_pos[0] - 500) * 180 / math.pi

        cannonballVelocity = self.direction * self.CannonballSpeed
        timeShot = pygame.time.get_ticks()
        cannonball = Cannonball(self.pos, cannonballVelocity, timeShot)
        self.create_cannonball_callback(cannonball)

class Boat(GameObject):

    def __init__(self, pos, boat_callback, size=3):
        self.boat_callback = boat_callback
        self.size = size
        size_scale = { 3:1, 2:0.5, 1:0.25 }
        scale = size_scale[size]
        sprite = rotozoom(load_sprite("Boat"), 0, scale)
        super().__init__(pos, sprite)

class Cannonball(GameObject):
    def __init__(self, pos, velocity, timeShot):
        super().__init__(pos, load_sprite("Bullet"), velocity)

        self.timeShot = timeShot