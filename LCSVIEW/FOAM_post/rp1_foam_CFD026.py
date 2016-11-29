import os
import sys
from paraview.simple import *


#if I need the path of this file use the next line
#dir_path = os.path.dirname(os.path.realpath(__file__))

script_path='/Users/mark/LCS/ParaviewScripts_mjt/LCSVIEW'
functions_path = os.path.join(script_path,'functions')

#make sure functions_path is in the sys path for finding python functions
sys.path.append(functions_path)
from fn import *
from cl import *

root_name='/Users/mark/LCS/ensight_files'

path_name = '/ensight_rp1_CFD026/lrh_run.case'
path_name = root_name + path_name

input_format = "ensight"
input_vbles = ['p', 'U']
input_locate = "cell"


pre_reflect = Volume_ensight(input_locate,path_name,input_vbles)


rp1case = reflect_geom(pre_reflect,'Y')

make_lcs_bg(rp1case.r_view,script_path,802,491)
turn_on_headlight(rp1case.r_view,0.1)
rp1case.r_view.OrientationAxesVisibility = 0


Hide(pre_reflect.master,pre_reflect.r_view)
Hide(rp1case.master,rp1case.r_view)


rp1car = cut_od(rp1case,'p','positive')

road = get_road(rp1case,'p','positive')

Show(rp1car.master,rp1car.r_view)
Show(road.master,road.r_view)

stream_1 = line_stream(rp1case,'U',-0.3,-0.9,0.14,-0.3,0.9,0.14,50)
Show(stream_1.master,stream_1.r_view)
stream_1.make_tube(.006,0.54)
Show(stream_1.tube,stream_1.r_view)

xslice_1= plane_slice(rp1case,2.75,-1.25,0.75,'x','U')
Show(xslice_1.master,xslice_1.r_view)

yslice_1= plane_slice(rp1case,2.75,1.25,0.75,'y','U')
Show(yslice_1.master,yslice_1.r_view)


stream_2 = line_stream(rp1case,'U',-0.3,0.3,0.03,-0.3,0.3,0.7,12)
Show(stream_2.master,stream_2.r_view)
stream_2.make_tube(.015,0.54)
Show(stream_2.tube,stream_2.r_view)

red=[0.66,0.33,0.0]
dark_grey=[0.2,0.2,0.2]
light_grey=[0.7,0.7,0.7]
no_colour=''


pressure_colour = pseudo_scalar('p',-250.0,250.0)
velocity_colour = pseudo_scalar('U',-5.0,30.0)

bigwake = make_contour(rp1case, 'U' , 6.0, 0.29)
wake = make_contour(rp1case, 'U' , 4.0, 0.29)
smallwake = make_contour(rp1case, 'U' , 2.0, 0.29)







