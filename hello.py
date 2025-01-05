import bpy
import easybpy as ez
import random as rnd
import sys

print(sys.path)

# ez.select_all_objects()
# ez.delete_selected_objects()

ez.create_torus()
ez.create_sphere()

bpy.ops.mesh.primitive_uv_sphere_add(location=(1, 1, 1))

[
    bpy.ops.mesh.primitive_plane_add(
        location=(10 * rnd.random(), 10 * rnd.random(), 10 * rnd.random())
    )
    for _x in range(10)
    for _y in range(10)
    for _z in range(10)
]
