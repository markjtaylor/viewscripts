import os
import sys
from paraview.simple import *


#if I need the path of this file use the next line
#dir_path = os.path.dirname(os.path.realpath(__file__))

script_path='/home/dmculley/MarkT/ParaviewScripts_mjt/LCSVIEW'
functions_path = os.path.join(script_path,'functions')

#make sure functions_path is in the sys path for finding python functions
sys.path.append(functions_path)
print sys.path



from fn import * 
from cl import *

root_name='/home/dmculley/MarkT'


path_name ='/inp_BIGrp1/trackcar_RP1.case'
path_name = root_name + path_name

input_format = "ensight"
input_vbles = ['PressureCoefficient', 'TotalPressureCoefficient', 'Velocity']
input_locate = "cell"
input_surfaces = [2]

#load the ensight file
pre_reflect = Volume_ensight(input_locate,path_name,input_vbles)

#mirror for comparison with vtu from FAST
naca12 = reflect_geom(pre_reflect,'Y')


#stick our logo in
#make_lcs_bg(naca12.r_view,script_path,802,491)

# set scalar coloring - to do - get this function work
#naca12.vol_colour('Pressure')

Hide(pre_reflect.master,pre_reflect.r_view)
Hide(naca12.master,naca12.r_view)

wing = Surface(naca12,input_surfaces)

#make a skin-friction surface vector from the input scalars
#naca12_stream = add_surface_points_vector('skinfriction_Vector',naca12, 'WallShearStressi', 'WallShearStressj', 'WallShearStressk' )
#wing_stream = Surface(naca12_stream,input_surfaces)
#Hide(naca12_stream.master,naca12_stream.r_view)
#Hide(wing_stream.master,wing_stream.r_view)

pressure_colour = pseudo_scalar('PressureCoefficient',-3.0,1.0)
velocity_colour = pseudo_scalar('Velocity',0.0,80.0)

wing.sur_colour('PressureCoefficient')

wing.Display.SetScalarBarVisibility(wing.r_view, True)
naca12.Display.SetScalarBarVisibility(naca12.r_view, False)

UpdatePipeline()

Show(wing.master,wing.r_view)

#stream_1 = line_stream(naca12,'Velocity',0.3,0.7,0.3,0.3,0.5,0.3,12)
#Show(stream_1.master,stream_1.r_view)
#stream_1.make_tube(.008,0.54)
#Show(stream_1.tube,stream_1.r_view)
#
#stream_2 = line_stream(naca12,'Velocity',-0.1,0.5,0.15,-0.1,0.5,0.55,12)
#Show(stream_2.master,stream_2.r_view)

xslice_1= plane_slice(naca12,1.8,-0.6,0.4,'x','PressureCoefficient')
Show(xslice_1.master,xslice_1.r_view)

#surface_stream=surface_stream(naca12_stream,wing_stream,'skinfriction_Vector','x', 'PressureCoefficient')
#Show(surface_stream.master,surface_stream.r_view)

Render()


