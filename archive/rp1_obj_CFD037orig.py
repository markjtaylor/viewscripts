import os
import sys
#from paraview.simple import *


#if I need the path of this file use the next line
#dir_path = os.path.dirname(os.path.realpath(__file__))

script_path='/Users/mark/LCS/ParaviewScripts_mjt/LCSVIEW'
functions_path = os.path.join(script_path,'functions')

#make sure functions_path is in the sys path for finding python functions
sys.path.append(functions_path)
sys.path.append(script_path)
from fn import *
from cl import *

obj_root_name='/Users/mark/LCS/ensight_files/rp1_obj/car_and_driver/'
stl_root_name='/Users/mark/LCS/ensight_files/rp1_upgrade_obj/car_and_driver_no_wheels/'

chassis_list=[]
wheels_list=[]

red=[0.66,0.33,0.0]
dark_grey=[0.2,0.2,0.2]
grey=[0.35,0.35,0.35]
mid_grey=[0.5,0.5,0.5]
light_grey=[0.7,0.7,0.7]
very_light_grey=[0.85,0.85,0.85]
white=[1.0,1.0,1.0]
black=[0.01,0.01,0.01]
light_black=[.1,.1,.1]
no_colour=''

road_surface = make_plane(-1.5,-2.5,0.0,-1.5,2.5,0.0,7.0,-2.5,0.0,dark_grey,0.3)

make_lcs_bg(road_surface.r_view,script_path,802,491)
turn_on_headlight(road_surface.r_view,0.1)
road_surface.r_view.OrientationAxesVisibility = 0

stl_path_name = 'Aluminium.stl'
stl_path_name_aluminium = stl_root_name + stl_path_name
aluminium = get_stl(stl_path_name_aluminium,.001,.001,.001,light_grey)
chassis_list.append(aluminium)

stl_path_name = 'Carbon Bodywork.stl'
stl_path_name_carbon = stl_root_name + stl_path_name
carbon = get_stl(stl_path_name_carbon,.001,.001,.001,light_black)
chassis_list.append(carbon)

stl_path_name = 'Floor.stl'
stl_path_name_floor_surface = stl_root_name + stl_path_name
floor_surface = get_stl(stl_path_name_floor_surface,.001,.001,.001,black)
chassis_list.append(floor_surface)

stl_path_name = 'Lighting.stl'
stl_path_name_lighting = stl_root_name + stl_path_name
lighting = get_stl(stl_path_name_lighting,.001,.001,.001,light_grey)
chassis_list.append(lighting)


stl_path_name = 'Rear Wing.stl'
stl_path_name_rearwing = stl_root_name + stl_path_name
rearwing = get_stl(stl_path_name_rearwing,.001,.001,.001,white)
chassis_list.append(rearwing)

stl_path_name = 'Trim.stl'
stl_path_name_trim = stl_root_name + stl_path_name
trim = get_stl(stl_path_name_trim,.001,.001,.001,dark_grey)
chassis_list.append(trim)

stl_path_name = 'Black Bodywork.stl'
stl_path_name_blackbody = stl_root_name + stl_path_name
blackbody = get_stl(stl_path_name_blackbody,.001,.001,.001,black)
chassis_list.append(blackbody)

stl_path_name = 'Driver etc.stl'
stl_path_name_drivers = stl_root_name + stl_path_name
drivers = get_stl(stl_path_name_drivers,.001,.001,.001,light_grey)
chassis_list.append(drivers)

stl_path_name = 'Helmets.stl'
stl_path_name_helmets = stl_root_name + stl_path_name
helmets = get_stl(stl_path_name_helmets,.001,.001,.001,white)
chassis_list.append(helmets)

stl_path_name = 'Painted Bodywork.stl'
stl_path_name_paintedbody = stl_root_name + stl_path_name
paintedbody = get_stl(stl_path_name_paintedbody,.001,.001,.001,white)
chassis_list.append(paintedbody)

stl_path_name = 'Screen.stl'
stl_path_name_paintedbody = stl_root_name + stl_path_name
paintedbody = get_stl(stl_path_name_paintedbody,.001,.001,.001,grey)
chassis_list.append(paintedbody)


obj_path_name = 'Elemental Rp1 satin black.obj'
obj_path_name_dsatinblack = obj_root_name + obj_path_name
dsatinblack = get_obj_file(obj_path_name_dsatinblack,0.01,.01,.01,0.0,0.0,0.11,light_black)


obj_path_name = 'Elemental Rp1 metallic satin black.obj'
obj_path_name_satinblack = obj_root_name + obj_path_name
wheels = get_obj_file(obj_path_name_satinblack,0.01,.01,.01,0.0,0.0,0.11,mid_grey)


obj_path_name = 'Elemental Rp1 tyres.obj'
obj_path_name_tyres = obj_root_name + obj_path_name
tyres = get_obj_file(obj_path_name_tyres,0.01,.01,.01,0.0,0.0,0.11,light_black)



#need to separate the front and rear  wheels and tyres
Hide(wheels.master,wheels.r_view)
Hide(tyres.master,tyres.r_view)

fwheels=make_plane_clip(wheels,2.2,0,.32,1.,0.,0.,1,grey)
rwheels=make_plane_clip(wheels,2.2,0,.32,1.,0.,0.,0,grey)

ftyres=make_plane_clip(tyres,2.2,0,.32,1.,0.,0.,1,light_black)
rtyres=make_plane_clip(tyres,2.2,0,.32,1.,0.,0.,0,light_black)

# need the front wheel nuts to rotate with the wheels

fwheelnuts=cut_stl_box(dsatinblack,0.78,0.0,0.178,.078,1.,.2646,1,light_black)
inverse_fwheelnuts=cut_stl_box(dsatinblack,0.78,0.0,0.178,.078,1.,.2646,0,light_black)

bounds_range=dsatinblack.master.GetDataInformation().GetBounds()
print bounds_range
bounds_range=inverse_fwheelnuts.master.GetDataInformation().GetBounds()
print bounds_range


# we also need the rear wheel nuts


right_rwheelnuts=cut_stl_box(inverse_fwheelnuts,3.30,0.88,0.194,.071,.1584,.2646,1,light_black)
inverse_rightrwheelnuts=cut_stl_box(inverse_fwheelnuts,3.30,0.88,0.194,.071,.1584,.2646,0,light_black)

left_rwheelnuts=cut_stl_box(inverse_rightrwheelnuts,3.30,-0.88,0.194,.071,.1584,.2646,1,light_black)
blacksatin_parts=cut_stl_box(inverse_rightrwheelnuts,3.30,-0.88,0.194,.071,.1584,.2646,0,light_black)

chassis_list.append(blacksatin_parts)
Hide(blacksatin_parts.master,blacksatin_parts.r_view)

rwheelnuts=join_stl(right_rwheelnuts,left_rwheelnuts,light_black)

move_file = '/rp1_movewheel.py'
move_file = script_path + move_file
execfile(move_file)
