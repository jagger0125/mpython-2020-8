from mcpi.minecraft import Minecraft
x,y,z= mc=Minecraft.create()= mc.player.getTilePos()
mc.setBlock(x+1,y,z,15)
mc.setBlock(x-1,y,z,15)
mc.setBlock(x,y,z-1,15)
mc.setBlock(x,y-1,z+1,15)