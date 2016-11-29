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
streamTracer11.SeedType.Center = [0.7703385502099991, -0.457888275384903, 0.31779877841472626]
streamTracer11.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer11
streamTracer11.SurfaceStreamlines = 1

# Properties modified on streamTracer11.SeedType
streamTracer11.SeedType.NumberOfPoints = 200

# show data in view
streamTracer11Display = Show(streamTracer11, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend
streamTracer11Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(extractBlock3)

# create a new 'Stream Tracer'
streamTracer12 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer12.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer12.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer12.SeedType.Center = [0.7703385502099991, -0.457888275384903, 0.31779877841472626]
streamTracer12.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer12.SeedType
streamTracer12.SeedType.Center = [0.7703385502099991, -0.257888275384903, 0.31779877841472626]
streamTracer12.SeedType.NumberOfPoints = 200

streamTracer12.SurfaceStreamlines = 1
# show data in view
streamTracer12Display = Show(streamTracer12, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend
streamTracer12Display.SetScalarBarVisibility(renderView1, True)


# create a new 'Stream Tracer'
streamTracer13 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer13.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer13.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer13.SeedType.Center = [0.7703385502099991, -0.457888275384903, 0.31779877841472626]
streamTracer13.SurfaceStreamlines = 1
streamTracer13.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer13.SeedType
streamTracer13.SeedType.Center = [0.7703385502099991, -0.507888275384903, 0.31779877841472626]
streamTracer13.SeedType.NumberOfPoints = 200

# show data in view
streamTracer13Display = Show(streamTracer13, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend
streamTracer13Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on streamTracer13.SeedType
streamTracer13.SeedType.Center = [0.7703385502099991, -0.057888275384903, 0.31779877841472626]


# Properties modified on streamTracer13.SeedType
streamTracer13.SeedType.Radius = 0.120118805766106
streamTracer13.SurfaceStreamlines = 1

# set active source
SetActiveSource(extractBlock3)

# create a new 'Stream Tracer'
streamTracer14 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer14.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer14.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer14.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer14
streamTracer14.SurfaceStreamlines = 1

# Properties modified on streamTracer14.SeedType
streamTracer14.SeedType.Center = [0.7703385502099991, -0.557888275384903, 0.31779877841472626]
streamTracer14.SeedType.NumberOfPoints = 200

# show data in view
streamTracer14Display = Show(streamTracer14, renderView1)
# trace defaults for the display properties.

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend

# create a new 'Stream Tracer'
streamTracer15 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer15.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer15.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer15.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer15
streamTracer15.SurfaceStreamlines = 1

# Properties modified on streamTracer15.SeedType
streamTracer15.SeedType.Center = [0.7703385502099991, -0.657888275384903, 0.31779877841572626]
streamTracer15.SeedType.NumberOfPoints = 200

# show data in view
streamTracer15Display = Show(streamTracer15, renderView1)

# hide data in view
Hide(extractBlock3, renderView1)

# show color bar/color legend
streamTracer15Display.SetScalarBarVisibility(renderView1, False)

# show color bar/color legend

# create a new 'Stream Tracer'
streamTracer16 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer16.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer16.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer16.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer16
streamTracer16.SurfaceStreamlines = 1

# Properties modified on streamTracer16.SeedType
streamTracer16.SeedType.Center = [0.7703385502099991, -0.757888275384903, 0.31779877841672626]
streamTracer16.SeedType.NumberOfPoints = 200

# show data in view
streamTracer16Display = Show(streamTracer16, renderView1)

# hide data in view
Hide(extractBlock3, renderView1)


# show color bar/color legend

# create a new 'Stream Tracer'
streamTracer17 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer17.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer17.MaximumStreamlineLength = 1.2011880576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer17.SeedType.Radius = 0.12011880576610566

# Properties modified on streamTracer17
streamTracer17.SurfaceStreamlines = 1

# Properties modified on streamTracer17.SeedType
streamTracer17.SeedType.Center = [0.7703385502099991, -0.807888275384903, 0.31779877841772626]
streamTracer17.SeedType.NumberOfPoints = 200

# show data in view
streamTracer17Display = Show(streamTracer17, renderView1)

# hide data in view
Hide(extractBlock3, renderView1)


# show color bar/color legend

# create a new 'Stream Tracer'
streamTracer18 = StreamTracer(Input=extractBlock3,
    SeedType='Point Source')
streamTracer18.Vectors = ['POINTS', 'skinfriction_Vector']
streamTracer18.MaximumStreamlineLength = 1.2011980576610565

# init the 'Point Source' selected for 'SeedType'
streamTracer18.SeedType.Radius = 0.12011980576610566

# Properties modified on streamTracer18
streamTracer18.SurfaceStreamlines = 1

# Properties modified on streamTracer18.SeedType
streamTracer18.SeedType.Center = [0.7703385502099991, -0.857888275384903, 0.31879877841872626]
streamTracer18.SeedType.NumberOfPoints = 200

# show data in view
streamTracer18Display = Show(streamTracer18, renderView1)
