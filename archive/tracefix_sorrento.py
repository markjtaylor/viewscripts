#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
enSightReader1 = FindSource('EnSightReader1')

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=enSightReader1,
    SeedType='Point Source')
streamTracer2.Vectors = ['CELLS', '_MRL_Velocity']
streamTracer2.MaximumStreamlineLength = 13.411200046539307

# init the 'Point Source' selected for 'SeedType'
streamTracer2.SeedType.Center = [1.0798208713531494, -0.609600007534027, 0.40600070911750663]
streamTracer2.SeedType.Radius = 1.3411200046539307

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2)

# Properties modified on streamTracer2
streamTracer2.IntegrationDirection = 'FORWARD'
streamTracer2.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [-0.3, -0.4, -0.0003992804267909378]
streamTracer2.SeedType.Point2 = [-0.3, 5.00764e-17, 0.8124006986618042]
streamTracer2.SeedType.Resolution = 75

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)
# trace defaults for the display properties.
streamTracer2Display.ColorArrayName = [None, '']
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(enSightReader1, renderView1)

# Properties modified on enSightReader1
enSightReader1.CellArrays = ['AbsolutePressure', 'Density', 'Pressure', '_MRL_skinFriction', '_MRL_Velocity']

# find source
extractBlock1 = FindSource('ExtractBlock1')

# Properties modified on extractBlock1
extractBlock1.BlockIndices = []

# find source
streamTracer1 = FindSource('StreamTracer1')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.6703950748207224, 2.3550769658549453, 0.15917520984812186]
renderView1.CameraFocalPoint = [0.7703385502099989, -0.4578882753849025, 0.3177987784147263]
renderView1.CameraViewUp = [-0.2749957855101373, 0.033807085619362534, -0.9608508723592789]
renderView1.CameraParallelScale = 0.7655111610903408

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).