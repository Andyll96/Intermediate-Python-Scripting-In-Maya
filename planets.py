from maya import cmds
import random

# planet
planetRadius = random.uniform(3,8)
cmds.polySphere(name='planet', radius=planetRadius)

numMoons = random.randint(1,10)
for i in range(0,numMoons):

    # randomMoonOrbit gives the random distance away from the planet
    randomMoonOrbit = planetRadius + random.uniform(1, 10)
    # randomMoonRotation gives the random position for the moon around the planet
    randomMoonRotationX = random.uniform(0, 360)
    randomMoonRotationY = random.uniform(0, 360)
    randomMoonRotationZ = random.uniform(0, 360)
    moonRadius = random.uniform(planetRadius/10, planetRadius/5)
    
    # moons
    cmds.polySphere(name=f'moon_{str(i)}', radius=moonRadius)

    # r is relative, perform a operation relative to the object's current position
    cmds.move(randomMoonOrbit, 0, 0, r=True)
    cmds.move(-randomMoonOrbit, 0, 0, f'moon_{str(i)}.scalePivot', f'moon_{str(i)}.rotatePivot', relative=True)

    # os is object space, perform rotation about object-space axis
    cmds.rotate(randomMoonRotationX, randomMoonRotationY, randomMoonRotationZ, r=True, os=True)

    # tgl, "basically add the planet to the selection, and its gonna be the second thing in the selection, so it'll parent the moon to the planet", see documentation for tgl
    cmds.select('planet', tgl=True)
    cmds.parent()

cmds.expression(string='planet.rotateY=time*10', object='planet', ae=True, uc='all')