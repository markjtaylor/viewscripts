
from paraview.simple import *
from paraview.servermanager import *
import sys
sys.path.append("/Users/keritaylor/LCS/ParaviewScripts")
import utilities as lcs


# set up
file='/Users/keritaylor/LCS/ensightfiles/inp_rp1/elemental_star1m300k.case'
vbles=['Pressure','Velocity']
sel_vbl=vbles[0]
vec_vbl=vbles[1]
visible=1

print sel_vbl


lcs.load_ensight(file,sel_vbl,visible)


