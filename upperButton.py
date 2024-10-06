import bpy
import bmesh
from mathutils import Vector

def create_laptop_button_with_text():
    # Crear el botón base
    bpy.ops.mesh.primitive_cube_add(size=1)
    button = bpy.context.active_object
    
    # Ajustar dimensiones del botón
    button.scale = (0.013, 0.007, 0.001)  # 1.3cm x 0.7cm x 0.1cm
    bpy.ops.object.transform_apply(scale=True)

    # Biselar los bordes superiores
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bm = bmesh.from_edit_mesh(button.data)
    for e in bm.edges:
        if e.verts[0].co.z > 0 and e.verts[1].co.z > 0:
            e.select = True
    bpy.ops.mesh.bevel(offset=0.0002, segments=8)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Crear el texto
    bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0.0005))
    text_obj = bpy.context.active_object
    text_obj.data.body = "araintel"
    text_obj.data.extrude = 0.00015  # 0.15mm de extrusión
    
    # Ajustar propiedades del texto
    text_obj.data.align_x = 'CENTER'
    text_obj.data.align_y = 'CENTER'
    
    # Escalar el texto (ajustable desde Blender)
    text_obj.scale = (0.0025, 0.0025, 1)
    
    # Centrar el texto en el botón
    text_obj.location = button.location
    text_obj.location.z = button.location.z + button.dimensions.z / 2

    # Convertir el texto a malla
    bpy.ops.object.convert(target='MESH')
    
    # Unir el texto al botón
    bpy.ops.object.select_all(action='DESELECT')
    text_obj.select_set(True)
    button.select_set(True)
    bpy.context.view_layer.objects.active = button
    bpy.ops.object.join()

    # Configurar las unidades de la escena
    bpy.context.scene.unit_settings.system = 'METRIC'
    bpy.context.scene.unit_settings.scale_length = 1

    return button

# Crear el botón con texto
created_button = create_laptop_button_with_text()

# Seleccionar y hacer activo el botón
bpy.ops.object.select_all(action='DESELECT')
created_button.select_set(True)
bpy.context.view_layer.objects.active = created_button