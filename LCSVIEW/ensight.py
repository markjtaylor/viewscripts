import os
import sys
from paraview.simple import *


#if I need the path of this file use the next line
#dir_path = os.path.dirname(os.path.realpath(__file__))

script_path='/Users/keritaylor/LCS/ParaviewScripts/LCSVIEW'
functions_path = os.path.join(script_path,'functions')

#make sure functions_path is in the sys path for finding python functions
sys.path.append(functions_path)
from fn import * 
from cl import *

root_name='/Users/keritaylor/LCS/ensightfiles'

path_name ='/inp_naca0012/MESH_06M/fw271981.case'
path_name = root_name + path_name

input_format = "ensight"
input_vbles = ['AbsolutePressure', 'Density', 'Pressure',  '_MRL_skinFrictionU', '_MRL_skinFrictionV', '_MRL_skinFrictionW', '_MRL_Velocity']
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
naca12_stream = add_surface_points_vector('skinfriction_Vector',naca12, '_MRL_skinFrictionU', '_MRL_skinFrictionV', '_MRL_skinFrictionW' )
wing_stream = Surface(naca12_stream,input_surfaces)
Hide(naca12_stream.master,naca12_stream.r_view)
Hide(wing_stream.master,wing_stream.r_view)

pressure_colour = pseudo_scalar('Pressure',-8000.0,2500.0)
velocity_colour = pseudo_scalar('_MRL_Velocity',0.0,100.0)

wing.sur_colour('Pressure')

wing.Display.SetScalarBarVisibility(wing.r_view, True)
naca12.Display.SetScalarBarVisibility(naca12.r_view, False)

UpdatePipeline()

Show(wing.master,wing.r_view)

stream_1 = line_stream(naca12,'_MRL_Velocity',0.3,0.7,0.3,0.3,0.5,0.3,12)
Show(stream_1.master,stream_1.r_view)
stream_1.make_tube(.008,0.54)
Show(stream_1.tube,stream_1.r_view)

stream_2 = line_stream(naca12,'_MRL_Velocity',-0.1,0.5,0.15,-0.1,0.5,0.55,12)
Show(stream_2.master,stream_2.r_view)

xslice_1= plane_slice(naca12,1.8,-0.6,0.4,'x','Pressure')
Show(xslice_1.master,xslice_1.r_view)

surface_stream=surface_stream(naca12_stream,wing_stream,'skinfriction_Vector','x', 'Pressure')
Show(surface_stream.master,surface_stream.r_view)

Render()


