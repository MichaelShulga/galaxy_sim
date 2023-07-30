import pymunk
import pymunk.pygame_util


space = pymunk.Space()
# space.gravity = (0, 10)


body1 = pymunk.Body(mass=1000, moment=10)
body1.position = 100, 200

circle = pymunk.Circle(body1, radius=20)

space.add(body1, circle)


body = pymunk.Body(mass=1000, moment=10)
body.position = 200, 200

circle = pymunk.Circle(body, radius=30)

space.add(body, circle)

# print((space.bodies[0].position - space.bodies[1].position).)
# print(body1.position.get_distance(body.position))

print(bool(body.position - body.position))

