# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:38:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock (x,y-1,z+i,137)
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
 x,y,z = mc.player.getTilePos()     
 plant(x,y,z)    