#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
rp1case = EnSightReader(CaseFileName='/Users/keritaylor/LCS/ensightfiles/inp_rp1/elemental_star1m300k.case')


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

rp1caseDisplay = Show(rp1case, renderView1)
rp1caseDisplay.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'AbsolutePressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-3.0, 0.231373, 0.298039, 0.752941, -0.9496047496795654, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Blue to Red Rainbow', True)


# show data in view
rp1caseDisplay = Show(rp1case, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
rp1caseDisplay.SetScalarBarVisibility(renderView1, False)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=rp1case)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)


# hide data in view
Hide(rp1case, renderView1)

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, False)

# create a new 'Clip'
clip1 = Clip(Input=extractSurface1)
clip1.Scalars = ['CELLS', 'AbsolutePressure']

# Properties modified on clip1
clip1.ClipType = 'Box'
clip1.InsideOut = 1

# Properties modified on clip1.ClipType
clip1.ClipType.Bounds = [-1.5, 7.0, -2.5, 2.8887559011536723e-09, 0.0, 1.5]
clip1.ClipType.Position = [0.001, -0.001, 0.001]
clip1.ClipType.Scale = [0.98, 0.98, 0.98]

# show data in view
clip1Display = Show(clip1, renderView1)

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1)

# set scalar coloring
ColorBy(clip1Display, ('CELLS', 'Pressure'))

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True)

# Rescale transfer function
pressureLUT.RescaleTransferFunction(-250.0, 250.0)

# Rescale transfer function
#pressurePWF.RescaleTransferFunction(-250.0, 250.0)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)


#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.0697988206012288, -0.08148098801403743, -1.7869891152526152]
renderView1.CameraFocalPoint = [1.0798208713531483, -0.6096000075340282, 0.4060007091175053]
renderView1.CameraViewUp = [0.5059647601357299, -0.31569800070552967, -0.8027044498763694]
renderView1.CameraParallelScale = 6.745505525367322

# find source
enSightReader1 = FindSource('EnSightReader1')

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=enSightReader1,
    SeedType='Point Source')
streamTracer1.Vectors = ['CELLS', 'Velocity']
streamTracer1.MaximumStreamlineLength = 13.411200046539307

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'FORWARD'
streamTracer1.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [-0.1, -0.9, 0.15]
streamTracer1.SeedType.Point2 = [-0.1, -0.001, 0.15]
streamTracer1.SeedType.Resolution = 15

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# hide data in view
Hide(enSightReader1, renderView1)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Velocity'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [55.946010717046455, 0.231373, 0.298039, 0.752941, 80.34874800973748, 0.865003, 0.865003, 0.865003, 104.75148530242849, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

velocityLUT.RescaleTransferFunction(-5.0, 30.0)


# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [55.946010717046455, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocityLUT.ApplyPreset('Blue to Red Rainbow', True)
velocityLUT.RescaleTransferFunction(-5.0, 30.0)

# hide color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.4878276355882836, -0.7494322110574833, 1.9095130497029669]
renderView1.CameraFocalPoint = [1.0798208713531494, -0.6096000075340253, 0.40600070911750724]
renderView1.CameraViewUp = [0.38506275983971405, 0.07009092103348225, 0.9202249365091673]
renderView1.CameraParallelScale = 6.745505525367322


# get active source.
streamTracer1 = GetActiveSource()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1)

# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']

# Properties modified on tube1
tube1.Radius = 0.008435356878489255

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [55.946010717046455, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# show data in view
tube1Display = Show(tube1, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, False)


# set active source
SetActiveSource(tube1)


# Properties modified on tube1Display
tube1Display.Opacity = 0.54

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.7811588882402662, -2.1068784148641444, 2.5463676072581394]
renderView1.CameraFocalPoint = [1.0798208713531479, -0.6096000075340253, 0.4060007091175068]
renderView1.CameraViewUp = [0.4969906885904914, 0.24172002704300724, 0.833409673558375]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# find source
enSightReader1 = FindSource('EnSightReader1')

# set active source
SetActiveSource(enSightReader1)


slice1 = Slice(Input=enSightReader1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [2.75, -1.249999998555622, 0.75]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [815, 491]

# get color transfer function/color map for 'AbsolutePressure'

# show data in view
slice1Display = Show(slice1, renderView1)

# hide data in view
Hide(enSightReader1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# find source
clip1 = FindSource('Clip1')

# Properties modified on clip1.ClipType
clip1.ClipType.Position = [0.0009999999999998899, -0.0009999999999998899, 0.0009999999999998899]
clip1.ClipType.Scale = [0.98, 0.9800000000000001, 0.98]




# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [2.0845985899965616, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-5.0, 30.0)

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [2.0845985899965616, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-5.0, 30.0)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1)

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'Velocity'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)



#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.4573392295426908, -3.520612042492187, 0.09447891651323534]
renderView1.CameraFocalPoint = [1.0798208713531474, -0.6096000075340253, 0.40600070911750524]
renderView1.CameraViewUp = [-0.4180256323595505, 0.2715693624604568, 0.8668936797919449]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# find source
enSightReader1 = FindSource('EnSightReader1')

# set active source
SetActiveSource(enSightReader1)

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=enSightReader1,
    SeedType='Point Source')
streamTracer2.Vectors = ['CELLS', 'Velocity']
streamTracer2.MaximumStreamlineLength = 13.411200046539307


# Properties modified on streamTracer2
streamTracer2.IntegrationDirection = 'FORWARD'
streamTracer2.SeedType = 'High Resolution Line Source'

streamTracer2.SeedType.Resolution = 6

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [-0.3, -0.3, 0.1]
streamTracer2.SeedType.Point2 = [-0.3, -0.3, 0.4]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [803, 491]

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)
Hide3DWidgets(proxy=streamTracer2)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.9282228297255046, 1.1921335145632892, 2.0378323114544195]
renderView1.CameraFocalPoint = [1.0798208713531545, -0.6096000075340238, 0.40600070911750713]
renderView1.CameraViewUp = [0.2686089945940614, -0.24596129375734, 0.9313174807746192]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
