import math
import pygame as pygame
from pygame import Color, Vector2
import random


width = 900
height = 900

circle_radius = (height/2) - 100

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

class Ball:
    def __init__(self):
        self.position = Vector2(width/2, height/2)
        self.color = (0, 0, 0)
        self.gravity = Vector2(0, 0.3)
        self.velocity = Vector2(random.uniform(-7, 7), -7)
        self.prevPos = Vector2(self.position.x, self.position.y)
        self.radius = 30
        self.hits = 0

    def update(self):
        self.prevPos = Vector2(self.position.x, self.position.y)
        #movimento
        self.velocity += self.gravity   
        self.position += self.velocity

        dirToCenter = Vector2(self.position.x - width/2, self.position.y - height/2)
        if self.isCollide():
            self.hits += 1
            if self.hits >= 15:
                if len(balls) == 25:
                    balls.pop(0)
                self.hits = 0
                new_ball = Ball()
                new_ball.position = Vector2(width/2, height/2)
                balls.append(new_ball)

            self.radius += 0
            self.position = Vector2(self.prevPos.x, self.prevPos.y)
            v = math.sqrt(self.velocity.x * self.velocity.x + self.velocity.y * self.velocity.y)
            angleToCollisionPoint = math.atan2(-dirToCenter.y, dirToCenter.x)
            oldAngle = math.atan2(-self.velocity.y, self.velocity.x)
            newAngle = 2 * angleToCollisionPoint - oldAngle
            self.velocity = Vector2(-v * math.cos(newAngle), v * math.sin(newAngle)) * 1.02

                
    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

    def isCollide(self):
        if self.distance(self.position.x, self.position.y, width/2, height/2) > circle_radius - self.radius:
            return True
        return False

    def draw(self):
        pygame.draw.circle(screen, self.color,(self.position.x, self.position.y), self.radius)

        
ball = Ball()

balls = [ball]

colorDir = 1
color = Color(211, 12, 211)
r = color.hsla[0]
g = color.hsla[1]
b = color.hsla[2]


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    
    screen.fill((0,0,0), (0,0, width, height))
    pygame.draw.circle(screen, (255,255,255),(width//2, height//2), (height/2) - 100, 2)

    color.hsla = (r, g, b, 1)
    r += 1 * colorDir
    if r >= 360:
        colorDir = -1
    elif r<= 0:
        colorDir = 1

    for ball in balls:
        ball.update()

        pygame.draw.circle(screen, (color.r, color.g, color.b) ,(ball.position.x, ball.position.y), ball.radius + 2)

        ball.draw()

    pygame.display.flip()
                    
