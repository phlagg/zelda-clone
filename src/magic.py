import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player) -> None:
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('./audio/heal.wav'),
            'flame': pygame.mixer.Sound('./audio/flame.wav')
        }
    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0,-40), groups)
      
    def flame(self, player, strength, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()            
            if 'up' in player.status: direction = pygame.math.Vector2(0,-1)
            elif 'down' in player.status: direction = pygame.math.Vector2(0, 1)
            elif 'left' in player.status: direction = pygame.math.Vector2(-1,0)
            else: direction = pygame.math.Vector2(1, 0)

            for i in range(1,6):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery+ randint(-TILESIZE//3, TILESIZE//3)
                else:           # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//3, TILESIZE//3)
                self.animation_player.create_particles('flame', (x,y), groups)

