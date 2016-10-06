#!/usr/bin/python
# coding: utf8

# Open:
# block.py
# Add
# LEVER               = Block(69)

import mcpi.minecraft as minecraft 
import mcpi.block as block
import sys

mc = minecraft.Minecraft.create()

[x,y,z] = mc.player.getPos()

lever1 = 0

while True:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.STONE.id:    
            mc.postToChat("Stone")
            print "STONE",
            print hitBlock.pos.x,
            print hitBlock.pos.y,
            print hitBlock.pos.z,
            print hitBlock.face,
            print hitBlock.type,
            print hitBlock.entityId

        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.LEVER.id:    
            if lever1 == 0:
                mc.postToChat("Lever On")
                lever1 = 1
            else:
                mc.postToChat("Lever Off")
                lever1 = 0

            print "LEVER",
            print hitBlock.pos.x,
            print hitBlock.pos.y,
            print hitBlock.pos.z,
            print hitBlock.face,
            print hitBlock.type,
            print hitBlock.entityId
