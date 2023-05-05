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

class COPY_DRIVERS_OT_operator(bpy.types.Operator):
    bl_idname = "object.copy_drivers"
    bl_label = "Copy Drivers"
    bl_description = "Copy drivers from one object to another"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source_obj = context.scene.copy_drivers_source
        target_obj = context.scene.copy_drivers_target

        if not source_obj or not target_obj:
            self.report({'ERROR'}, "Both source and target objects must be selected")
            return {'CANCELLED'}

        for i, source_prop in enumerate(source_obj.animation_data.drivers):
            data_path = source_prop.data_path
            driver = target_obj.driver_add(data_path)

            for var in source_prop.driver.variables:
                new_var = driver.driver.variables.new()
                new_var.name = var.name
                new_var.type = var.type
                new_var.targets[0].id = var.targets[0].id
                new_var.targets[0].data_path = var.targets[0].data_path

            driver.driver.type = source_prop.driver.type
            driver.driver.expression = source_prop.driver.expression

        return {'FINISHED'}

class COPY_DRIVERS_PT_panel(bpy.types.Panel):
    bl_label = "Copy Drivers"
    bl_idname = "COPY_DRIVERS_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Copy Drivers'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "copy_drivers_source")
        layout.prop(context.scene, "copy_drivers_target")
        layout.operator("object.copy_drivers")

def register():
    bpy.utils.register_class(COPY_DRIVERS_OT_operator)
    bpy.utils.register_class(COPY_DRIVERS_PT_panel)
    bpy.types.Scene.copy_drivers_source = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.copy_drivers_target = bpy.props.PointerProperty(type=bpy.types.Object)

def unregister():
    bpy.utils.unregister_class(COPY_DRIVERS_OT_operator)
    bpy.utils.unregister_class(COPY_DRIVERS_PT_panel)
    del bpy.types.Scene.copy_drivers_source
    del bpy.types.Scene.copy_drivers_target

if __name__ == "__main__":
    register()
