bl_info = {
    "name": "Copy Drivers",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Copy Drivers",
    "description": "Copies drivers from one object to another",
    "category": "Object",
}

import bpy

class DeleteAllShapeKeyDriversOperator(bpy.types.Operator):
    bl_idname = "object.delete_all_shape_key_drivers"
    bl_label = "Delete All Shape Key Drivers"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.data.shape_keys and obj.data.shape_keys.animation_data:
                obj.data.shape_keys.animation_data_clear()
                self.report({'INFO'}, f"All shape key drivers deleted from {obj.name}")

        return {'FINISHED'}

class COPY_DRIVERS_OT_operator(bpy.types.Operator):
    bl_idname = "object.copy_drivers"
    bl_label = "Copy Drivers"
    bl_description = "Copy drivers from one object to another"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source_obj = context.scene.copy_drivers_source
        target_obj = context.scene.copy_drivers_target
        target_armature = context.scene.copy_drivers_target_armature

        if not source_obj or not target_obj:
            self.report({'ERROR'}, "Both source and target objects must be selected")
            return {'CANCELLED'}

        if source_obj.data.shape_keys is None:
            self.report({'ERROR'}, "Source object has no shape keys with drivers to copy")
            return {'CANCELLED'}

        source_key_blocks = source_obj.data.shape_keys.key_blocks
        source_shape_key_drivers = source_obj.data.shape_keys.animation_data.drivers if source_obj.data.shape_keys.animation_data else []

        if target_obj.data.shape_keys is None:
            target_obj.shape_key_add(name="Basis")
        target_key_blocks = target_obj.data.shape_keys.key_blocks

        for source_driver in source_shape_key_drivers:
            source_key_block_name = source_driver.data_path.split('["')[-1].split('"]')[0]
            target_key_block = target_key_blocks.get(source_key_block_name)
            if not target_key_block:
                source_key_block = source_key_blocks.get(source_key_block_name)
                target_key_block = target_obj.shape_key_add(name=source_key_block.name)

            data_path = source_driver.data_path
            driver = target_obj.data.shape_keys.driver_add(data_path)

            for var in source_driver.driver.variables:
                new_var = driver.driver.variables.new()
                new_var.name = var.name
                new_var.type = var.type
                if var.type == 'TRANSFORMS' and target_armature:
                    new_var.targets[0].id = target_armature
                    if var.targets[0].bone_target in target_armature.data.bones:
                        new_var.targets[0].bone_target = var.targets[0].bone_target
                    else:
                        print(f"Bone '{var.targets[0].bone_target}' not found in target armature '{target_armature.name}'")
                else:
                    new_var.targets[0].id = var.targets[0].id
                new_var.targets[0].data_path = var.targets[0].data_path

            driver.driver.type = source_driver.driver.type
            driver.driver.expression = source_driver.driver.expression

        return {'FINISHED'}



class COPY_DRIVERS_PT_panel(bpy.types.Panel):
    bl_label = "Copy Drivers"
    bl_idname = "COPY_DRIVERS_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Copy Drivers'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "copy_drivers_source", text="Source Mesh")
        layout.prop(context.scene, "copy_drivers_target", text="Target Mesh")
        layout.prop_search(context.scene, "copy_drivers_target_armature", context.scene, "objects", text="Target Armature")
        layout.separator()
        layout.operator("object.copy_drivers")
        layout.operator("object.delete_all_shape_key_drivers")




def register():
    bpy.utils.register_class(COPY_DRIVERS_OT_operator)
    bpy.utils.register_class(DeleteAllShapeKeyDriversOperator)
    bpy.utils.register_class(COPY_DRIVERS_PT_panel)
    bpy.types.Scene.copy_drivers_source = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.copy_drivers_target = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.copy_drivers_target_armature = bpy.props.PointerProperty(
        type=bpy.types.Object,
        poll=lambda self, obj: obj.type == 'ARMATURE',
    )

def unregister():
    bpy.utils.unregister_class(COPY_DRIVERS_OT_operator)
    bpy.utils.unregister_class(DeleteAllShapeKeyDriversOperator)
    bpy.utils.unregister_class(COPY_DRIVERS_PT_panel)
    del bpy.types.Scene.copy_drivers_source
    del bpy.types.Scene.copy_drivers_target
    del bpy.types.Scene.copy_drivers_target_armature

if __name__ == "__main__":
    register()
