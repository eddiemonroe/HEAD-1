# This module controls the user interface in Blender that
# is used to manage the rigControl

import bpy
import pdb

class BLRigControl(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "RigControl"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_context = "object"


	# bpy.types.Scene.commandListenerActive = bpy.props.BoolProperty( name = "commandListenerActive", default=False)

	def draw(self, context):
		layout = self.layout
		obj = context.object

		row = layout.row()
		prop = row.operator("wm.command_listener", text='Start Command Listener')

		row = layout.row()
		prop = row.operator("wm.animation_playback", text='Test Emotion Cycle')

		row = layout.row()
		row.label(text="Expression Controls", icon='ARMATURE_DATA')

		# row = layout.row()
		# row.label(text="Active object is: " + obj.name)
		# row = layout.row()
		# row.prop(obj, "name")

		row = layout.row()




def register():
	bpy.utils.register_class(BLRigControl)


def unregister():
	bpy.utils.unregister_class(BLRigControl)


def refresh():
	try:
		register()
	except ValueError:
		print('Re-registering')
		unregister()
		register()
	