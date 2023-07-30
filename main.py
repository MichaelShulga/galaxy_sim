import math
import random
import pygame
import pymunk
import pymunk.pygame_util

WIDTH, HEIGHT = 1500, 800
G = 0.0009

space = pymunk.Space()

def planetGravity(body, gravity, damping, dt):
    sq_dist = body.position.get_dist_sqrd((300, 300))
    g = pymunk.Vec2d(0, 0)
    for other_body in space.bodies:
        r = other_body.position - body.position
        if r.length:
            force = G * (other_body.mass * body.mass) / (r.length ** 2) * (r / r.length)
            g += force / body.mass
    pymunk.Body.update_velocity(body, g, damping, dt)


# def add_space_body(pos, mass, radius):
#     body = pymunk.Body(mass=mass, moment=1)
#     body.position = pos
#     body.velocity_func = planetGravity
#     circle = pymunk.Circle(body, radius=radius)

#     space.add(body, circle)


# def init_bodies():
#     add_space_body(pymunk.Vec2d(300, 200), 1000_000_000, 20)
#     for _ in range(7):
#         pos = pymunk.Vec2d(random.randint(0, 600), random.randint(0, 400))
#         mass = random.randint(10, 100)
#         radius = random.randint(1, 10)
#         add_space_body(pos, mass, radius)


# def init_bodies():
#     body = pymunk.Body()
#     body.mass = 1000_000_000
#     body.position = pymunk.Vec2d(300, 200)
#     body.moment = 1
#     # body.velocity = pymunk.Vec2d(random.randint(0, 600), random.randint(0, 600))
#     body.velocity_func = planetGravity 
#     space.add(body, pymunk.Circle(body, radius=20))

#     for _ in range(7):
#         body = pymunk.Body()
#         body.moment = 1
#         body.mass = random.randint(10, 1000)
#         body.position = pymunk.Vec2d(300, 200)
#         body.velocity = pymunk.Vec2d(random.randint(0, 600), random.randint(0, 600))
#         body.velocity_func = planetGravity 
#         space.add(body, pymunk.Circle(body, radius=random.randint(1, 10)))


def init_galaxy(pos, velocity):
    main_body = pymunk.Body()
    main_body.mass = 1000_000_000
    main_body.position = pos
    main_body.moment = 1
    main_body.velocity = velocity
    main_body.velocity_func = planetGravity 
    space.add(main_body, pymunk.Circle(main_body, radius=20))

    for _ in range(7):
        body = pymunk.Body()
        body.moment = 1
        body.mass = random.randint(10, 1000)
        body.position = pymunk.Vec2d(random.randint(WIDTH // 3, WIDTH), random.randint(HEIGHT // 3, HEIGHT))

        r = main_body.position - body.position
        force = G * (main_body.mass * body.mass) / (r.length ** 2) * (r / r.length)
        a = force / body.mass
        body.velocity = math.sqrt(r.length * a.length) * r.perpendicular_normal()
        body.velocity_func = planetGravity 
        space.add(body, pymunk.Circle(body, radius=random.randint(1, 10)))


init_galaxy(pymunk.Vec2d(-WIDTH // 2, HEIGHT // 2 + HEIGHT // 5), pymunk.Vec2d(30, 0))
init_galaxy((WIDTH + WIDTH // 2, HEIGHT // 2 - HEIGHT // 5), pymunk.Vec2d(-30, 0))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
draw_options = pymunk.pygame_util.DrawOptions(screen)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('black'))
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.01)
pygame.quit()