# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:03:02 2020

@author: user
"""



while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,\
            hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.createExplosion(x,y,z,power=100)