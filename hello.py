import bpy
import easybpy as ez


# ez.select_all_objects()
# ez.delete_selected_objects()
ez.create_torus()
ez.create_sphere()
bpy.ops.mesh.primitive_uv_sphere_add(location=(1, 1, 1))
[
    bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, z))
    for x in range(10)
    for y in range(10)
    for z in range(10)
]

# [value for value in iterable]

# bpy.ops.mesh.primitive_uv_sphere_add()
# print("System path:")
# print(sys.path)
# print(__file__)
# print(cwd)
# bpy.ops.mesh.primitive_uv_sphere_add()
# cube = bpy.context.active_object
# start_frame = 1
# cube.keyframe_insert("location", frame=start_frame)
# cube.location.z = 5
# end_frame = 180
# cube.keyframe_insert("location", frame=end_frame)
# main()
