import pygame as pg
from variables import *


class Player(pg.sprite.Sprite):
    #player sprite
    def __init__(self, game, x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(CYAN)        
        #the rectangle that encloses the sprite
        self.rect = self.image.get_rect()
        #vectors
        self.vx, self.vy = 0,0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        #checks if any keys are pressed, if not then vx anf vy are set to 0,0
        self.vx, self.vy = 0,0
        keys =pg.key.get_pressed()
        #move to the left if the left arrow or a key is pressed
        if keys[pg.K_LEFT] or keys [pg.K_a]:
            self.vx = -PLAYER_SPEED
        #moves to the right is the right arrow or the d key is pressed
        if keys[pg.K_RIGHT] or keys [pg.K_d]:
            self.vx = PLAYER_SPEED
        #moves up if the up arrow or the w key is pressed
        if keys[pg.K_UP] or keys [pg.K_w]:
            self.vy = -PLAYER_SPEED
        #moves down if the down arrow or the s key is pressed
        if keys[pg.K_DOWN] or keys [pg.K_s]:
            self.vy = PLAYER_SPEED
        #so when youre moving diagonally you dont move faster than when moving <^v>
        if self.vx != 0 and self.vy !=0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        #if the direction of the player is along the x axis 
        if dir == "x":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            #then the code checks if the player sprite is hitting any wall sprites
            if hits:
                #if it is hitting any wall sprites ti checks if the player is moving in the x direction
                if self.vx >0:
                    #if it is then the x becomes the coordinate of the thing its hitting minus the width of the player
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx<0:
                    #if its not then the x becomes the coordinates of the right corner
                    self.x = hits[0].rect.right
                #x displacememnt becomes 0
                self.vx = 0
                #the rect x coordinate becomes self.x
                self.rect.x= self.x
        #if the direction of the player is along the y axis
        if dir == "y":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            #then the code checks if the player sprite is hitting any wall sprites
            if hits:
                #if it is hitting any wall sprites ti checks if the player is moving in the y direction
                if self.vy >0:
                    #if it is then the y becomes the coordinate of the thing its hitting minus the height of the player
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy<0:
                    #if its not then the y becomes the coordinates of the bottom
                    self.y = hits[0].rect.bottom
                self.vy = 0
                #y displacememnt becomes 0
                self.rect.y= self.y
                #the rect y coordinate becomes self.y


    def update(self):
        self.get_keys()
        #makes the players x-coordinate = the vx multiplied by the game
        #time step + where it already was 
        self.x += self.vx * self.game.dt
        #makes the players y-coordinate = the vx multiplied by the game
        #time step +where it already was
        self.y += self.vy * self.game.dt
        #sets the rect to the x and y coordinates
        self.rect.x = self.x
        self.collide_with_walls("x")
        self.rect.y = self.y
        self.collide_with_walls("y")
        


                
                
            
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        #make it a member of the sprites group and the walls group
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #makes the actual walls
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
