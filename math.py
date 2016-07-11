# Generate polarzz curve

import bpy
import bmesh
import math


def theFunction( x ):

   return math.cos(5*x) + math.cos(7*x);



me = bpy.context.object.data
bm = bmesh.new()   # create an empty BMesh


resolution = 12000
length = 400
thickness = 0.004

vertReference = []

for i in range(resolution):
    
    r = theFunction(i / (resolution / length))
    o = (i / (resolution / length))
    vert = bm.verts.new((0.3*o, r * math.cos(o), r * math.sin(o)))
    vert.index = len(bm.verts)
    
    vertReference.extend([vert])

    
    bm.verts.index_update()
    
    if (len(vertReference) > 1):
        bm.edges.new( (vertReference[i], vertReference[i-1]) )
    

# Finish up, write the bmesh back to the mesh
bm.to_mesh(me)

bpy.context.scene.objects.active = bpy.context.scene.objects.active

bpy.ops.object.convert(target='CURVE')

bpy.ops.object.convert(target='CURVE')

bpy.context.object.data.fill_mode = 'FULL'
bpy.context.object.data.bevel_depth = thickness
bpy.context.object.data.bevel_resolution = 1
bpy.ops.object.shade_smooth()
bpy.ops.object.convert(target='MESH')
