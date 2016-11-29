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

path_name = '/ensight_rp1_baseline/fifth_run_final.case'
path_name = root_name + path_name

input_format = "ensight"
input_vbles = ['p', 'U']
input_locate = "cell"

pre_reflect = Volume_ensight(input_locate,path_name,input_vbles)
Hide(pre_reflect.master,pre_reflect.r_view)


initial_case = mirror_geom(pre_reflect,'Y')
Hide(initial_case.master,pre_reflect.r_view)

second_case = make_cp(initial_case,'p',20,input_locate)
Hide(second_case.master,second_case.r_view)

rp1case = make_cp0(second_case,'p','U',20,input_locate)
Hide(rp1case.master,rp1case.r_view)

make_lcs_bg(rp1case.r_view,script_path,802,491)
turn_on_headlight(rp1case.r_view,0.1)
rp1case.r_view.OrientationAxesVisibility = 0

stream_1 = line_stream(rp1case,'U',-0.3,-0.9,0.03,-0.3,0.9,0.03,30)
Show(stream_1.master,stream_1.r_view)
Hide(stream_1.master,stream_1.r_view)
stream_1.make_tube(.008,0.54)
Show(stream_1.tube,stream_1.r_view)
Hide(stream_1.tube,stream_1.r_view)

xslice_1= plane_slice(rp1case,2.75,-1.25,0.75,'x','Cp0')
Show(xslice_1.master,xslice_1.r_view)
Hide(xslice_1.master,xslice_1.r_view)

yslice_1= plane_slice(rp1case,2.75,-1.25,0.75,'y','Cp0')
Show(yslice_1.master,yslice_1.r_view)
Hide(yslice_1.master,yslice_1.r_view)


stream_2 = line_stream(rp1case,'U',-0.3,-0.3,0.03,-0.3,-0.3,0.7,12)
Show(stream_2.master,stream_2.r_view)
Hide(stream_2.master,stream_2.r_view)
stream_2.make_tube(.015,0.54)
Show(stream_2.tube,stream_2.r_view)
Hide(stream_2.tube,stream_2.r_view)



big_wake = make_contour(rp1case, 'U' , 6.0, 0.29)
Hide(big_wake.master,big_wake.r_view)
wake = make_contour(rp1case, 'U' , 4.0, 0.29)
Hide(wake.master,wake.r_view)
small_wake = make_contour(rp1case, 'U' , 2.0, 0.29)
Hide(small_wake.master,small_wake.r_view)

num_balls=4
stream_layer_set = make_stream_set(rp1case,'U',-1.5,-1.0,0.03,-1.5, 1.0,0.03,15,4,0.1,'z','y',.03,num_balls)


pressure_colour = pseudo_scalar('p',-150.0,250.0)
velocity_colour = pseudo_scalar('U',-5.0,30.0)

cp_colour = pseudo_scalar('Cp',-1.0,1.0)
cp0_colour = pseudo_scalar('Cp0',0.0,1.0)




