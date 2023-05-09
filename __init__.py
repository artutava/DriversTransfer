bl_info = {
    "name": "FACE TRANSFER",
    "author": "SirCruX Studios",
    "version": (1, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > FACE TRANSFER",
    "description": "Copies drivers from one object to another",
    "category": "Object",
}

import bpy

class FACETRANSFER_OT_add_arkit(bpy.types.Operator):
    bl_idname = "facetransfer.add_arkit"
    bl_label = "Add Arkit Shapekeys"
    bl_description = "Create Arkit Compatible Shapekeys"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.object

        shapelist = [ "browInnerUp", "browDown_L", "browDown_R", "browOuterUp_L", "browOuterUp_R", "eyeLookUp_L", "eyeLookUp_R", "eyeLookDown_L", "eyeLookDown_R", "eyeLookIn_L", "eyeLookIn_R", "eyeLookOut_L", "eyeLookOut_R", "eyeBlink_L", "eyeBlink_R", "eyeSquint_L", "eyeSquint_R", "eyeWide_L", "eyeWide_R", "cheekPuff", "cheekSquint_L", "cheekSquint_R", "noseSneer_L", "noseSneer_R", "jawOpen", "jawForward", "jawLeft", "jawRight", "mouthFunnel", "mouthPucker", "mouthLeft", "mouthRight", "mouthRollUpper", "mouthRollLower", "mouthShrugUpper", "mouthShrugLower", "mouthClose", "mouthSmile_L", "mouthSmile_R", "mouthFrown_L", "mouthFrown_R", "mouthDimple_L", "mouthDimple_R", "mouthUpperUp_L", "mouthUpperUp_R", "mouthLowerDown_L", "mouthLowerDown_R", "mouthPress_L", "mouthPress_R", "mouthStretch_L", "mouthStretch_R", "tongueOut"]


        for each in shapelist:
            print(each)
            obj.shape_key_add(name = each, from_mix=False)
        
        return {'FINISHED'}

class FACETRANSFER_OT_add_fc(bpy.types.Operator):
    bl_idname = "facetransfer.add_fc"
    bl_label = "Add FC Shapekeys"
    bl_description = "Create FC Compatible Shapekeys"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.object

        shapelist = [ "FC_browInnerUp", "FC_browDown_L", "FC_browDown_R", "FC_browOuterUp_L", "FC_browOuterUp_R", "FC_eyeLookUp_L", "FC_eyeLookUp_R", "FC_eyeLookDown_L", "FC_eyeLookDown_R", "FC_eyeLookIn_L", "FC_eyeLookIn_R", "FC_eyeLookOut_L", "FC_eyeLookOut_R", "FC_eyeBlink_L", "FC_eyeBlink_R", "FC_eyeSquint_L", "FC_eyeSquint_R", "FC_eyeWide_L", "FC_eyeWide_R", "FC_cheekPuff", "FC_cheekSquint_L", "FC_cheekSquint_R", "FC_noseSneer_L", "FC_noseSneer_R", "FC_jawOpen", "FC_jawForward", "FC_jawLeft", "FC_jawRight", "FC_mouthFunnel", "FC_mouthPucker", "FC_mouthLeft", "FC_mouthRight", "FC_mouthRollUpper", "FC_mouthRollLower", "FC_mouthShrugUpper", "FC_mouthShrugLower", "FC_mouthClose", "FC_mouthSmile_L", "FC_mouthSmile_R", "FC_mouthFrown_L", "FC_mouthFrown_R", "FC_mouthDimple_L", "FC_mouthDimple_R", "FC_mouthUpperUp_L", "FC_mouthUpperUp_R", "FC_mouthLowerDown_L", "FC_mouthLowerDown_R", "FC_mouthPress_L", "FC_mouthPress_R", "FC_mouthStretch_L", "FC_mouthStretch_R", "FC_tongueOut"]


        for each in shapelist:
            print(each)
            obj.shape_key_add(name = each, from_mix=False)
        return {'FINISHED'}
    

class FACETRANSFER_OT_arkit_to_FC(bpy.types.Operator):
    bl_idname = "facetransfer.arkit_to_fc"
    bl_label = "Convert Arkit to FC"
    bl_description = "Convert Arkit to FC Shapekeys"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.object
        shapelist = [ "browInnerUp", "browDown_L", "browDown_R", "browOuterUp_L", "browOuterUp_R", "eyeLookUp_L", "eyeLookUp_R", "eyeLookDown_L", "eyeLookDown_R", "eyeLookIn_L", "eyeLookIn_R", "eyeLookOut_L", "eyeLookOut_R", "eyeBlink_L", "eyeBlink_R", "eyeSquint_L", "eyeSquint_R", "eyeWide_L", "eyeWide_R", "cheekPuff", "cheekSquint_L", "cheekSquint_R", "noseSneer_L", "noseSneer_R", "jawOpen", "jawForward", "jawLeft", "jawRight", "mouthFunnel", "mouthPucker", "mouthLeft", "mouthRight", "mouthRollUpper", "mouthRollLower", "mouthShrugUpper", "mouthShrugLower", "mouthClose", "mouthSmile_L", "mouthSmile_R", "mouthFrown_L", "mouthFrown_R", "mouthDimple_L", "mouthDimple_R", "mouthUpperUp_L", "mouthUpperUp_R", "mouthLowerDown_L", "mouthLowerDown_R", "mouthPress_L", "mouthPress_R", "mouthStretch_L", "mouthStretch_R", "tongueOut"]

        # Get the selected object
        selected_object = bpy.context.active_object

        # Iterate through the shape keys in the list
        for shape_key_name in shapelist:
            shape_key = selected_object.data.shape_keys.key_blocks.get(shape_key_name)
            
            # If the shape key exists, add the "FC_" prefix
            if shape_key:
                shape_key.name = "FC_" + shape_key_name
        return {'FINISHED'}

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

class FACETRANSFER_OT_copy_drivers(bpy.types.Operator):
    bl_idname = "facetransfer.copy_drivers"
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
                    new_var.targets[0].data_path = var.targets[0].data_path.replace(source_obj.data.name, target_obj.data.name)
                else:
                    id_data = var.targets[0].id
                    owner = next((obj for obj in context.scene.objects if obj.data == id_data), None)
                    if var.type == 'SINGLE_PROP' and target_obj:
                        
                        if var.type == 'SINGLE_PROP' and target_obj:
                        
                            if owner and owner.type == 'MESH':
                                new_var.targets[0].id_type= 'MESH'
                                new_var.targets[0].id = target_obj.data
                                new_var.targets[0].data_path = var.targets[0].data_path
                            else:
                                new_var.targets[0].id_type= 'MESH'
                                new_var.targets[0].id = target_obj.data
                                new_var.targets[0].data_path = var.targets[0].data_path.lstrip("data.")
                            
                        else:
                            new_var.targets[0].id = id_data
                            new_var.targets[0].data_path = var.targets[0].data_path

                new_var.targets[0].transform_type = var.targets[0].transform_type
                new_var.targets[0].transform_space = var.targets[0].transform_space
                new_var.targets[0].bone_target = var.targets[0].bone_target

            driver.driver.type = source_driver.driver.type
            driver.driver.expression = source_driver.driver.expression

            # Copy f-curve and control points
            source_fcurve = source_driver.keyframe_points
            target_fcurve = driver.keyframe_points

            # Clear target F-Curve's keyframe points
            target_fcurve.clear()

            # Add keyframe points from the source F-Curve to the target F-Curve
            for source_cp in source_fcurve:
                target_cp = target_fcurve.insert(source_cp.co[0], source_cp.co[1])
                target_cp.interpolation = source_cp.interpolation
                target_cp.easing = source_cp.easing
                target_cp.handle_left_type = source_cp.handle_left_type
                target_cp.handle_right_type = source_cp.handle_right_type
                target_cp.handle_left = source_cp.handle_left.copy()
                target_cp.handle_right = source_cp.handle_right.copy()
                target_cp.select_left_handle = source_cp.select_left_handle
                target_cp.select_right_handle = source_cp.select_right_handle
                target_cp.select_control_point = source_cp.select_control_point

            # Remove the Generator modifier if present
            for mod in driver.modifiers:
                if mod.type == 'GENERATOR':
                    driver.modifiers.remove(mod)
                    
            driver.extrapolation = 'LINEAR'



        return {'FINISHED'}


class FACETRANSFER_OT_type_obj_to_mesh(bpy.types.Operator):
    bl_idname = "facetransfer.type_obj_to_mesh"
    bl_label = "ID Type Obj to Mesh"
    bl_description = "Convert vars ID types in Drivers, removing prefix .data from datapaths. It helps avoiding dependency cycles"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # Get the active object
        obj = bpy.context.active_object

        # Check if the object has shape keys
        if obj.data.shape_keys:

            # Iterate through shape key drivers
            for fcurve in obj.data.shape_keys.animation_data.drivers:

                # Iterate through the driver variables
                for var in fcurve.driver.variables:

                    # Check if the variable's type is single property
                    if var.type == 'SINGLE_PROP':

                        # Store the current target ID
                        current_target_id = var.targets[0].id

                        # Update the data path to remove "data."
                        if var.targets[0].data_path.startswith("data."):
                            var.targets[0].data_path = var.targets[0].data_path[5:]

                        # Change id_type from "OBJECT" to "MESH" while keeping the same ID block
                        if var.targets[0].id_type == 'OBJECT':
                            var.targets[0].id_type = 'MESH'
                            var.targets[0].id = current_target_id.data

            # Refresh the depsgraph to update the changes
            bpy.context.evaluated_depsgraph_get().update()
        else:
            print("The active object does not have any shape keys.")
        return {'FINISHED'}




class FACETRANSFER_PT_panel(bpy.types.Panel):
    bl_label = "FACE TRANSFER"
    bl_idname = "FACE_TRANSFER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Face Transfer'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "copy_drivers_source", text="Source Mesh")
        layout.prop(context.scene, "copy_drivers_target", text="Target Mesh")
        layout.prop_search(context.scene, "copy_drivers_target_armature", context.scene, "objects", text="Target Armature")
        layout.separator()
        layout.operator("facetransfer.copy_drivers")
        layout.operator("object.delete_all_shape_key_drivers")
        layout.separator()
        layout.operator("facetransfer.add_arkit")
        layout.operator("facetransfer.add_fc")
        layout.operator("facetransfer.arkit_to_fc")
        layout.separator()
        layout.operator("facetransfer.type_obj_to_mesh")
        
        
        





def register():
    bpy.utils.register_class(FACETRANSFER_OT_type_obj_to_mesh)
    bpy.utils.register_class(FACETRANSFER_OT_add_arkit)
    bpy.utils.register_class(FACETRANSFER_OT_add_fc)
    bpy.utils.register_class(FACETRANSFER_OT_arkit_to_FC)
    bpy.utils.register_class(FACETRANSFER_OT_copy_drivers)
    bpy.utils.register_class(DeleteAllShapeKeyDriversOperator)
    bpy.utils.register_class(FACETRANSFER_PT_panel)
    bpy.types.Scene.copy_drivers_source = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.copy_drivers_target = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.copy_drivers_target_armature = bpy.props.PointerProperty(
        type=bpy.types.Object,
        poll=lambda self, obj: obj.type == 'ARMATURE',
    )

def unregister():
    bpy.utils.unregister_class(FACETRANSFER_OT_type_obj_to_mesh)
    bpy.utils.unregister_class(FACETRANSFER_OT_add_arkit)
    bpy.utils.unregister_class(FACETRANSFER_OT_add_fc)
    bpy.utils.unregister_class(FACETRANSFER_OT_arkit_to_FC)
    bpy.utils.unregister_class(FACETRANSFER_OT_copy_drivers)
    bpy.utils.unregister_class(DeleteAllShapeKeyDriversOperator)
    bpy.utils.unregister_class(FACETRANSFER_PT_panel)
    del bpy.types.Scene.copy_drivers_source
    del bpy.types.Scene.copy_drivers_target
    del bpy.types.Scene.copy_drivers_target_armature

if __name__ == "__main__":
    register()
