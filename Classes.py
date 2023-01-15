import pygame
import math
import random
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
        self.player = Player((50, 174), self.cannonballs.append)
        self.boats = []
        self.boats.append(Boat((1050, 325), (1, 0), self.boats.append, 2))
        self.multiplier = 1
        self.last_boat_shot = 0
        self.spawn_interval = random.randrange(2000, 6000, 1000)
        self.last_boat_made = 0
        self.start_boats = True

        self.start = False
        self.mouse_button = None
        self.mouse_pos = None
        self.isHolding = False
        self.timeHeld = 0
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

                if self.isHolding == True:
                    self.timeHeld = self.timeHeld + 0.05

                    if self.timeHeld >= 3:

                        self.timeHeld = 3

    def initPygame(self):

        pygame.init()

    def main_menu(self):

        self.start = False
        mouse_pos = pygame.mouse.get_pos()

        self.screen.blit(load_sprite("Background"), (0, 0))
        text_in_line(self.screen, "HEAVY ORDINANCE", self.font, 40, "white")
        text_in_line(self.screen, "START", self.font, 280)
        text_in_line(self.screen, "EXIT", self.font, 340)

        if mouse_pos[0] > 430 and mouse_pos[0] < 570 and mouse_pos[1] > 260 and mouse_pos[1] < 295:

            text_in_line(self.screen, "START", self.font, 280, "tomato")

        if mouse_pos[0] > 455 and mouse_pos[0] <= 555 and mouse_pos[1] > 320 and mouse_pos[1] < 355:

            text_in_line(self.screen, "EXIT", self.font, 340, "tomato")

        events = pygame.event.get()

        for evt in events:
            if (evt.type == pygame.QUIT):
                quit()

            if evt.type == pygame.MOUSEBUTTONUP:

                if mouse_pos[0] > 455 and mouse_pos[0] <= 555 and mouse_pos[1] > 320 and mouse_pos[1] < 355:
                    quit()

                if mouse_pos[0] > 430 and mouse_pos[0] < 570 and mouse_pos[1] > 260 and mouse_pos[1] < 295:
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

                if evt.type == pygame.MOUSEBUTTONDOWN and self.cooldown == True:

                    self.isHolding = True
                
                if evt.type == pygame.MOUSEBUTTONUP and self.cooldown == True:

                    self.isHolding = False
                    self.player.shoot(self.timeHeld)
                    self.cooldown = False
                    self.timeHeld = 0
                    self.lastShot = pygame.time.get_ticks()
        
    def gameLogic(self):

        for gameObject in self.get_GameObject():

            gameObject.move()

        for cannonball in self.cannonballs[:]:
            if cannonball.pos[0] < 0 or cannonball.pos[0] > 1000 or cannonball.pos[1] > 380:
                self.cannonballs.remove(cannonball)
                break
        
        for cannonball in self.cannonballs[:]:
            for boat in self.boats:
                if boat.collision(cannonball):
                    self.last_boat_shot = pygame.time.get_ticks()
                    self.spawn_interval = random.randrange(2000, 6000, 1000)
                    self.boats.remove(boat)
                    self.cannonballs.remove(cannonball)
                    self.addBoatScore(boat.size, self.multiplier)

        for boat in self.boats[:]:
            if boat.pos[0] <= 150:
                self.boats.remove(boat)

        if len(self.boats) < 4:

            if self.start_boats == True:
                timePassed = pygame.time.get_ticks()

                if timePassed > (self.last_boat_made + self.spawn_interval):
                    random_size = random.randint(1, 5)
                    self.boats.append(Boat((1050, 325), (-1, 0), self.boats.append, random_size))
                    self.last_boat_made = pygame.time.get_ticks()

                if len(self.boats) == 3:

                    self.start_boats = False
                    self.last_boat_shot = pygame.time.get_ticks()

            if self.start_boats == False:

                timePassed = pygame.time.get_ticks()

                if timePassed > (self.last_boat_shot + self.spawn_interval):
                    random_size = random.randint(1, 5)
                    self.boats.append(Boat((1050, 325), (-1, 0), self.boats.append, random_size))
                    self.last_boat_shot = pygame.time.get_ticks()
                    self.spawn_interval = random.randrange(2000, 6000, 1000)
                
    def draw(self):

        self.screen.blit(load_sprite("Background"), (0, 0))

        for gameObject in self.get_GameObject():
            gameObject.draw(self.screen)

        if self.phrase == "GAME OVER":
            self.gameOver()

        pygame.display.flip()
        self.clock.tick(60)

    def addBoatScore(self, size_boat, multiplier):

        boatScore = 6 - size_boat
        self.score = self.score + boatScore * multiplier

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
        self.player = Player((50, 174), self.cannonballs.append)
        self.boats = []
        self.boats.append(Boat((1050, 335), (-1, 0), self.boats.append, 2))
        self.multiplier = 1
        self.last_boat_shot = 0
        self.spawn_interval = random.randrange(2000, 6000, 1000)
        self.last_boat_made = 0
        self.start_boats = True
        
        self.isHolding = False
        self.timeHeld = 0
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

    angle = 0

    def __init__(self, pos, create_cannonball_callback):
        self.create_cannonball_callback = create_cannonball_callback
        self.direction = Vector2(UP)
        super().__init__(pos, load_sprite("PlayerCannon"), Vector2(0))

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()
        self.angle = 90 - math.atan2(mouse_pos[1] - 206, mouse_pos[0] - 50) * 180 / math.pi
        if self.angle < 100 and self.angle > -90:
            self.angle = 100
        if self.angle < 269 and self.angle > 180:
            self.angle = 180
        rotatedSurface = rotozoom(self.sprite, self.angle, 1.0)
        rotatedSurfaceSize = Vector2(rotatedSurface.get_size())
        blitPos = self.pos - rotatedSurfaceSize * 0.5
        self.direction.rotate_ip(self.angle)
        surface.blit(rotatedSurface, blitPos)

    def rotate(self):

        mouse_pos = pygame.mouse.get_pos()
        self.angle = 90 - math.atan2(mouse_pos[1] - 206, mouse_pos[0] - 50) * 180 / math.pi
        if self.angle < 100 and self.angle > -90:
            self.angle = 100
        if self.angle < 269 and self.angle > 180:
            self.angle = 180

        self.direction.rotate_ip(self.angle)
    
    def shoot(self, timeHeld):

        mouse_pos = pygame.mouse.get_pos()
        self.angle = 90 - math.atan2(mouse_pos[1] - 206, mouse_pos[0] - 50) * 180 / math.pi
        if self.angle < 100 and self.angle > -90:
            self.angle = 100
        if self.angle < 269 and self.angle > 180:
            self.angle = 180
        shotForce = timeHeld * 2
        timeShot = pygame.time.get_ticks()
        cannonball = Cannonball(self.pos, shotForce, self.angle, timeShot)
        self.create_cannonball_callback(cannonball)

class Cannonball(GameObject):

    def __init__(self, pos, velocity, angle, timeShot):
        super().__init__(pos, load_sprite("Cannonball"), velocity)

        self.timeShot = timeShot
        self.angle = angle
        self.gravity = (math.pi, 0.05)
        self.direction = Vector2(UP)
        self.drag = 0.999
        self.speed = self.velocity[0]
        self.x = self.pos[0]
        self.y = self.pos[1]

    def addVectors(self, angle1, length1, angle2, length2):

        x = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y = math.cos(angle1) * length1 + math.cos(angle2) * length2

        finalAngle = 0.5 * math.pi - math.atan2(y, x)
        finalLength = math.hypot(x, y)

        return (finalAngle, finalLength)

    def move(self):
 
        (self.angle, self.speed) = self.addVectors(self.angle, self.speed, self.gravity[0], self.gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.pos = (self.x, self.y)
        self.speed *= self.drag

class Boat(GameObject):

    def __init__(self, pos, velocity, boat_callback, size=3):
        self.velocity = velocity
        self.boat_callback = boat_callback
        self.size = size
        sprite = rotozoom(load_sprite("Boat" + str(self.size)), 0, 1)
        super().__init__(pos, sprite, velocity)