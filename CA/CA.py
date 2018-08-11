# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:20:12 2018

@author: ty020
"""

import PyCA, numpy, random
from PIL import Image

# rule for life game
def rule_lifegame(pix, neighborhood, envi):
    for r in range(3):
        for c in range(3):
            if neighborhood[r][c] == None:
                neighborhood[r][c] = 0
    
    if pix == 255:
        live = numpy.sum(neighborhood) - 255
        if live < 2 * 255:
            return 0
        elif live <= 3 * 255:
            return 255
        else:
            return 0
    else:
        live = numpy.sum(neighborhood)
        if live == 3 * 255:
            return 255
        else:
            return 0;
            
# build initial cell distributioin, randomly pick up 3000 cells as living cells
(row, col) = (100, 100)
cells= numpy.zeros((row, col)).tolist()
for i in range(3000):
    cells[random.randint(0, 99)][random.randint(0, 99)] = 255

# build trasformation rules
rulebuilder = PyCA.rulebuilder(rule_lifegame, 'von', 1)
carule = rulebuilder.build()

# create CA model
ca = PyCA.CA(cells, cells, carule)
ca.evolve(50, False, True)    

# save the array of result as bmp file
for (time, result) in ca.history.items():
    arr = numpy.array(result, dtype = numpy.uint8)
    im = Image.fromarray(arr)
    im.save('time_{0}.bmp'.format(time))