#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
enSightReader1 = FindSource('EnSightReader1')

# set active source
SetActiveSource(enSightReader1)

# create a new 'Cell Data to Point Data'
cellDatatoPointData4 = CellDatatoPointData(Input=enSightReader1)
cellDatatoPointData4Display = Show(cellDatatoPointData4, renderView1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [876, 491]

Hide(enSightReader1, renderView1)

# show color bar/color legend
cellDatatoPointData4Display.SetScalarBarVisibility(renderView1, True)




# create a new 'Calculator'
calculator2 = Calculator(Input=cellDatatoPointData4)

# Properties modified on calculator2
calculator2.ResultArrayName = 'skinfriction_Vector'
calculator2.Function = '_MRL_skinFrictionU*iHat+_MRL_skinFrictionV*jHat+_MRL_skinFrictionW*kHat'

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(cellDatatoPointData4, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, False)

# create a new 'Extract Block'
extractBlock3 = ExtractBlock(Input=calculator2)

# Properties modified on extractBlock3
extractBlock3.BlockIndices = [2]

# show data in view
extractBlock3Display = Show(extractBlock3, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
extractBlock3Display.SetScalarBarVisibility(renderView1, False)


# hide data in view
Hide(extractBlock3, renderView1)

# show data in view
calculator2Display = Show(calculator2, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)


# create a new 'Stream Tracer'
streamTracer11 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer11.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer11.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer11.SeedType.Center = [0.2703385502099991, -0.457888275384903, 0.35779877841472626]
streamTracer11.SeedType.Radius = 0.45011880576610566

# Properties modified on streamTracer11
streamTracer11.SurfaceStreamlines = 1

# Properties modified on streamTracer11.SeedType
streamTracer11.SeedType.NumberOfPoints = 20000

# show data in view
streamTracer11Display = Show(streamTracer11, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend
streamTracer11Display.SetScalarBarVisibility(renderView1, True)

#could consider algorithm where we put point at centre of body and work out radius to generate streamlines
