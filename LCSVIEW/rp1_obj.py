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

obj_path_name = 'Elemental Rp1 Anodised Aluminuim.obj'
obj_path_name_anodealum = obj_root_name + obj_path_name
anodealum = get_obj_file(obj_path_name_anodealum,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(anodealum)


obj_path_name = 'Elemental Rp1 aluminium.obj'
obj_path_name_alum = obj_root_name + obj_path_name
alum = get_obj_file(obj_path_name_alum,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(alum)

obj_path_name = 'Elemental Rp1 amber LED.obj'
obj_path_name_amber = obj_root_name + obj_path_name
amber = get_obj_file(obj_path_name_amber,0.01,.01,.01,0.0,0.0,0.11,very_light_grey)
chassis_list.append(amber)

obj_path_name = 'Elemental Rp1 black fabric.obj'
obj_path_name_blackfab = obj_root_name + obj_path_name
blackfab = get_obj_file(obj_path_name_blackfab,0.01,.01,.01,0.0,0.0,0.11,dark_grey)
chassis_list.append(blackfab)

obj_path_name = 'Elemental Rp1 black visor polycarbonate.obj'
obj_path_name_visor = obj_root_name + obj_path_name
visor = get_obj_file(obj_path_name_visor,0.01,.01,.01,0.0,0.0,0.11,dark_grey)
chassis_list.append(visor)

obj_path_name = 'Elemental Rp1 carbon fibre.obj'
obj_path_name_carbon = obj_root_name + obj_path_name
carbon = get_obj_file(obj_path_name_carbon,0.01,.01,.01,0.0,0.0,0.11,light_black)
chassis_list.append(carbon)

obj_path_name = 'Elemental Rp1 cast steel.obj'
obj_path_name_steel = obj_root_name + obj_path_name
steel = get_obj_file(obj_path_name_steel,0.01,.01,.01,0.0,0.0,0.11,dark_grey)
chassis_list.append(steel)

obj_path_name = 'Elemental Rp1 chrome.obj'
obj_path_name_chrome = obj_root_name + obj_path_name
chrome = get_obj_file(obj_path_name_chrome,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(chrome)

obj_path_name = 'Elemental Rp1 clear glass.obj'
obj_path_name_glass = obj_root_name + obj_path_name
glass = get_obj_file(obj_path_name_glass,0.01,.01,.01,0.0,0.0,0.11,very_light_grey)
chassis_list.append(glass)

obj_path_name = 'Elemental Rp1 driver_anodized alluminium.obj'
obj_path_name_danodealum = obj_root_name + obj_path_name
danodealum = get_obj_file(obj_path_name_danodealum,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(danodealum)

obj_path_name = 'Elemental Rp1 driver_black fabric.obj'
obj_path_name_dblackfab = obj_root_name + obj_path_name
dblackfab = get_obj_file(obj_path_name_dblackfab,0.01,.01,.01,0.0,0.0,0.11,black)
chassis_list.append(dblackfab)

obj_path_name = 'Elemental Rp1 driver_black foam.obj'
obj_path_name_blackfoam = obj_root_name + obj_path_name
blackfoam = get_obj_file(obj_path_name_blackfoam,0.01,.01,.01,0.0,0.0,0.11,black)
chassis_list.append(blackfoam)

obj_path_name = 'Elemental Rp1 driver_black matte plastic.obj'
obj_path_name_blackplastic = obj_root_name + obj_path_name
blackplastic = get_obj_file(obj_path_name_blackplastic,0.01,.01,.01,0.0,0.0,0.11,black)
chassis_list.append(blackplastic)

obj_path_name = 'Elemental Rp1 driver_black seatbelt.obj'
obj_path_name_seatbelt = obj_root_name + obj_path_name
seatbelt = get_obj_file(obj_path_name_seatbelt,0.01,.01,.01,0.0,0.0,0.11,dark_grey)
chassis_list.append(seatbelt)

obj_path_name = 'Elemental Rp1 driver_black transparent polycarbonate.obj'
obj_path_name_polycarb = obj_root_name + obj_path_name
polycarb = get_obj_file(obj_path_name_polycarb,0.01,.01,.01,0.0,0.0,0.11,light_black)
chassis_list.append(polycarb)

obj_path_name = 'Elemental Rp1 driver_white fabric.obj'
obj_path_name_whitefab = obj_root_name + obj_path_name
whitefab = get_obj_file(obj_path_name_whitefab,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(whitefab)

obj_path_name = 'Elemental Rp1 driver_white plastic.obj'
obj_path_name_whiteplastic = obj_root_name + obj_path_name
whiteplastic = get_obj_file(obj_path_name_whiteplastic,0.01,.01,.01,0.0,0.0,0.11,white)
chassis_list.append(whiteplastic)

obj_path_name = 'Elemental Rp1 flat black.obj'
obj_path_name_flatblack = obj_root_name + obj_path_name
flatblack = get_obj_file(obj_path_name_flatblack,0.01,.01,.01,0.0,0.0,0.11,black)
chassis_list.append(flatblack)

obj_path_name = 'Elemental Rp1 flat white.obj'
obj_path_name_flatwhite = obj_root_name + obj_path_name
flatwhite = get_obj_file(obj_path_name_flatwhite,0.01,.01,.01,0.0,0.0,0.11,very_light_grey)
chassis_list.append(flatwhite)

obj_path_name = 'Elemental Rp1 green LED.obj'
obj_path_name_greenl = obj_root_name + obj_path_name
greenl = get_obj_file(obj_path_name_greenl,0.01,.01,.01,0.0,0.0,0.11,dark_grey)
chassis_list.append(greenl)

obj_path_name = 'Elemental Rp1 machined aluminuim.obj'
obj_path_name_machalum = obj_root_name + obj_path_name
machalum = get_obj_file(obj_path_name_machalum,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(machalum)

obj_path_name = 'Elemental Rp1 metallic satin black.obj'
obj_path_name_satinblack = obj_root_name + obj_path_name
wheels = get_obj_file(obj_path_name_satinblack,0.01,.01,.01,0.0,0.0,0.11,mid_grey)

obj_path_name = 'Elemental Rp1 metallic white.obj'
obj_path_name_metwhite = obj_root_name + obj_path_name
metwhite = get_obj_file(obj_path_name_metwhite,0.01,.01,.01,0.0,0.0,0.11,white)
chassis_list.append(metwhite)

obj_path_name = 'Elemental Rp1 red LED.obj'
obj_path_name_redl = obj_root_name + obj_path_name
redl = get_obj_file(obj_path_name_redl,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(redl)

obj_path_name = 'Elemental Rp1 red anodised aluminium.obj'
obj_path_name_redalum = obj_root_name + obj_path_name
redalum = get_obj_file(obj_path_name_redalum,0.01,.01,.01,0.0,0.0,0.11,very_light_grey)
chassis_list.append(redalum)

obj_path_name = 'Elemental Rp1 red paint.obj'
obj_path_name_redpaint = obj_root_name + obj_path_name
redpaint = get_obj_file(obj_path_name_redpaint,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(redpaint)

obj_path_name = 'Elemental Rp1 red perspex.obj'
obj_path_name_redperspex = obj_root_name + obj_path_name
redperspex = get_obj_file(obj_path_name_redperspex,0.01,.01,.01,0.0,0.0,0.11,light_grey)
chassis_list.append(redperspex)

obj_path_name = 'Elemental Rp1 satin black.obj'
obj_path_name_dsatinblack = obj_root_name + obj_path_name
dsatinblack = get_obj_file(obj_path_name_dsatinblack,0.01,.01,.01,0.0,0.0,0.11,light_black)

obj_path_name = 'Elemental Rp1 tyres.obj'
obj_path_name_tyres = obj_root_name + obj_path_name
tyres = get_obj_file(obj_path_name_tyres,0.01,.01,.01,0.0,0.0,0.11,light_black)

obj_path_name = 'Elemental Rp1 white LED.obj'
obj_path_name_whiteled = obj_root_name + obj_path_name
whiteled = get_obj_file(obj_path_name_whiteled,0.001,.001,.001,0.0,0.0,0.11,very_light_grey)
chassis_list.append(whiteled)


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

rwheelnuts=join_stl(right_rwheelnuts,left_rwheelnuts,light_black)

move_file = '/rp1_movewheel.py'
move_file = script_path + move_file
execfile(move_file)
