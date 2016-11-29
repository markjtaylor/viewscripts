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
path_name = '/fast_naca12_570k/output_30.pvtu'
path_name = root_name + path_name

input_format = "vtu"
input_vbles = ['velocity, u', 'pressure, p', 'tke_k', 'dissipation_epsilon', 'turbulent viscosity,nu_T']
input_locate = "point"

naca12 = Volume_vtu(input_locate,path_name,input_vbles)

#make_lcs_bg(naca12.r_view,script_path,802,491)

# set scalar coloring - to do - get this function work
#naca12.vol_colour('Pressure')

Hide(naca12.master,naca12.r_view)

pressure_colour = pseudo_scalar('pressure, p',-8000.0,2500.0)
velocity_colour = pseudo_scalar('velocity, u',0.0,100.0)

wing = cut_od(naca12,'pressure, p')

wing.Display.SetScalarBarVisibility(wing.r_view, True)
naca12.Display.SetScalarBarVisibility(naca12.r_view, False)

UpdatePipeline()

Show(wing.master,wing.r_view)

stream_1 = line_stream(naca12,'velocity, u',0.3,-0.7,0.3,0.3,-0.5,0.3,12)
Show(stream_1.master,stream_1.r_view)
stream_1.make_tube(.008,0.54)
Show(stream_1.tube,stream_1.r_view)

stream_2 = line_stream(naca12,'velocity, u',-0.1,-0.5,0.15,-0.1,-0.5,0.55,12)
Show(stream_2.master,stream_2.r_view)

xslice_1= plane_slice(naca12,1.8,-0.6,0.4,'x','pressure, p')
Show(xslice_1.master,xslice_1.r_view)

Render()
