import os
import sys
import math
from paraview.simple import *

def	make_lcs_bg(view,path_name,x_width,y_height):
	view.UseTexturedBackground = 0

	view.Background = [0.90, 0.90, 0.90]
	view.ViewSize = [x_width, y_height]
	txt = servermanager.rendering.ImageTexture()
#txt.SourceProcess="Client"
#	txt.FileName = "/Users/keritaylor/LCS/ensightfiles/logos/LCSlogo_lightbg_lhcorner.png"
	txt.FileName = os.path.join(path_name, "logos" + "/" + "LCSlogo_lightbg_lhcorner_comp.png")

	view.BackgroundTexture = txt
	view.UseTexturedBackground = 1


def	get_centre_radius(name,orientation):

        bounds_range=name.master.GetDataInformation().GetBounds()
	print bounds_range

	x1=bounds_range[0]	
	x2=bounds_range[1]	
	y1=bounds_range[2]	
	y2=bounds_range[3]	
	z1=bounds_range[4]	
	z2=bounds_range[5]	

	x_c=(x1 + x2)/2
	y_c=(y1 + y2)/2
	z_c=(z1 + z2)/2

	centre=(x_c,y_c,z_c)
	if orientation=='x':
		radius=math.sqrt((y_c*y_c)+(z_c*z_c))
	if orientation=='y':
		radius=math.sqrt((x_c*x_c)+(z_c*z_c))
	if orientation=='z':
		radius=math.sqrt((y_c*y_c)+(x_c*x_c))

	return centre,radius

def	turn_on_headlight(render_view,strength):
	render_view.LightSwitch = 1 
	render_view.LightIntensity = 0.1 	
