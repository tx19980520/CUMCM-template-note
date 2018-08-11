# Version:1.1
# Last edit: 12/19/2013 by Yu
# If you have any question about the script, feel free to send me an email dz316424@126.com

import PyCA, numpy, random
from PIL import Image

# rule for life game
def rule_lifegame(pix, agent, envi):
    for r in range(3):
        for c in range(3):
            if agent[r][c] == None:
                agent[r][c] = 0
    
    if pix == 255:
        live = numpy.sum(agent) - 255
        if live < 2 * 255:
            return 0
        elif live <= 3 * 255:
            return 255
        else:
            return 0
    else:
        live = numpy.sum(agent)
        if agent == 3 * 255:
            return 255
        else:
            return 0;
            
# build environment
(row, col) = (100, 100)
grid = numpy.zeros((row, col)).tolist()
for i in range(3000):
    grid[random.randint(0, 99)][random.randint(0, 99)] = 255

# build trasformation rules
rulebuilder = PyCA.rulebuilder(rule_lifegame, 'von', 1)
rule = rulebuilder.build()

# create CA model
ca = PyCA.CA(grid, grid, rule)
ca.evolve(50, False, True)    

# save the array to bmp file
for (time, result) in ca.history.items():
    arr = numpy.array(result, dtype = numpy.uint8)
    im = Image.fromarray(arr)
    im.save('time_{0}.bmp'.format(time))
    