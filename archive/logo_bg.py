#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# Properties modified on renderView1
renderView1.Background = [0.9019607843137255, 0.9019607843137255, 0.9019607843137255]

# Properties modified on renderView1
renderView1.UseTexturedBackground = 1

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.7703385502099991, -0.457888275384903, 3.2755067816534926]
renderView1.CameraFocalPoint = [0.7703385502099991, -0.457888275384903, 0.31779877841472626]
renderView1.CameraParallelScale = 0.7655111610903408

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).