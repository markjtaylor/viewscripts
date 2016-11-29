#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
slice1 = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 234]

# hide data in view
Hide(slice1, renderView1)

# find source
streamTracer2 = FindSource('StreamTracer2')

# set active source
SetActiveSource(streamTracer2)

# create a new 'Contour'
contour1 = Contour(Input=streamTracer2)
contour1.ContourBy = ['POINTS', 'AngularVelocity']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# find source
clip1 = FindSource('Clip1')

# find source
streamTracer1 = FindSource('StreamTracer1')

# find source
tube1 = FindSource('Tube1')

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'IntegrationTime']

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.ColorArrayName = [None, '']
contour1Display.GlyphType = 'Arrow'
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(streamTracer2, renderView1)

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
extractSurface1 = FindSource('ExtractSurface1')

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-250.0, 0.0, 0.0, 1.0, 250.0, 1.0, 0.0, 0.0]
pressureLUT.ColorSpace = 'HSV'
pressureLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pressureLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
pressureLUT.RescaleTransferFunction(-1228.5826416, 431.529998779)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [-5.0, 0.0, 0.0, 1.0, 30.0, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-5.0, 30.9616234973)

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [-5.0, 0.0, 0.5, 0.0, 30.0, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-5.0, 30.9616234973)

# get animation track
contour1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=contour1)

# create keyframes for this animation track

# create a key frame
keyFrame6390 = CompositeKeyFrame()

# create a key frame
keyFrame6391 = CompositeKeyFrame()
keyFrame6391.KeyTime = 1.0
keyFrame6391.KeyValues = [0.8758881903216709]

# initialize the animation track
contour1ContourValuesTrack.KeyFrames = [keyFrame6390, keyFrame6391]

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame6393 = CameraKeyFrame()
keyFrame6393.Position = [-4.987794734897423, 1.87166297673143, 1.9479435837029397]
keyFrame6393.FocalPoint = [3.983714759042828, -1.8785647414330147, -0.5849593220302026]
keyFrame6393.ViewUp = [0.1884927689231993, -0.19865748863570415, 0.9617721550724062]
keyFrame6393.ParallelScale = 6.745505525367322
keyFrame6393.PositionPathPoints = [0.0, -4.89663502630931, -1.0114175295696721, 2.8862447669660147, -3.8494026963656784, -1.3607681751032852, 4.67004213280253, -1.3318293727958497, -1.1903516285566118, 4.6700421328025294, 1.694457503966538, -0.5652612184651029, 2.8862447669660125, 4.073519206706017, 0.2757397645578953, -7.181755190543981e-16, 4.896635026309306, 1.0114175295696706, -2.886244766966013, 3.8494026963656744, 1.3607681751032832, -4.670042132802527, 1.3318293727958472, 1.1903516285566098, -4.670042132802525, -1.694457503966538, 0.5652612184651012, -2.886244766966009, -4.073519206706014, -0.2757397645578963]
keyFrame6393.FocalPathPoints = [0.0, 0.0, 0.0]
keyFrame6393.ClosedPositionPath = 1

# create a key frame
keyFrame6394 = CameraKeyFrame()
keyFrame6394.KeyTime = 1.0
keyFrame6394.Position = [-4.987794734897423, 1.87166297673143, 1.9479435837029397]
keyFrame6394.FocalPoint = [3.983714759042828, -1.8785647414330147, -0.5849593220302026]
keyFrame6394.ViewUp = [0.1884927689231993, -0.19865748863570415, 0.9617721550724062]
keyFrame6394.ParallelScale = 6.745505525367322

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame6393, keyFrame6394]

# get camera animation track for the view
cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame6405 = CameraKeyFrame()
keyFrame6405.Position = [-4.987794734897423, 1.87166297673143, 1.9479435837029397]
keyFrame6405.FocalPoint = [3.983714759042828, -1.8785647414330147, -0.5849593220302026]
keyFrame6405.ViewUp = [0.1884927689231993, -0.19865748863570415, 0.9617721550724062]
keyFrame6405.ParallelScale = 6.745505525367322
keyFrame6405.PositionPathPoints = [0.0, -4.89663502630931, -1.0114175295696721, 2.8862447669660147, -3.8494026963656784, -1.3607681751032852, 4.67004213280253, -1.3318293727958497, -1.1903516285566118, 4.6700421328025294, 1.694457503966538, -0.5652612184651029, 2.8862447669660125, 4.073519206706017, 0.2757397645578953, -7.181755190543981e-16, 4.896635026309306, 1.0114175295696706, -2.886244766966013, 3.8494026963656744, 1.3607681751032832, -4.670042132802527, 1.3318293727958472, 1.1903516285566098, -4.670042132802525, -1.694457503966538, 0.5652612184651012, -2.886244766966009, -4.073519206706014, -0.2757397645578963]
keyFrame6405.FocalPathPoints = [0.0, 0.0, 0.0]
keyFrame6405.ClosedPositionPath = 1

# create a key frame
keyFrame6406 = CameraKeyFrame()
keyFrame6406.KeyTime = 1.0
keyFrame6406.Position = [-4.987794734897423, 1.87166297673143, 1.9479435837029397]
keyFrame6406.FocalPoint = [3.983714759042828, -1.8785647414330147, -0.5849593220302026]
keyFrame6406.ViewUp = [0.1884927689231993, -0.19865748863570415, 0.9617721550724062]
keyFrame6406.ParallelScale = 6.745505525367322

# initialize the animation track
cameraAnimationCue1_1.KeyFrames = [keyFrame6405, keyFrame6406]

# set active source
SetActiveSource(clip1)

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-1228.5826416015625, 0.0, 0.5, 0.0, 431.5299987792969, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# create a new 'Shrink'
shrink1 = Shrink(Input=clip1)

# Properties modified on shrink1
shrink1.ShrinkFactor = 1.0

# get color transfer function/color map for 'AbsolutePressure'
absolutePressureLUT = GetColorTransferFunction('AbsolutePressure')
absolutePressureLUT.RGBPoints = [100096.4140625, 0.231373, 0.298039, 0.752941, 100926.47265625, 0.865003, 0.865003, 0.865003, 101756.53125, 0.705882, 0.0156863, 0.14902]
absolutePressureLUT.ScalarRangeInitialized = 1.0

# show data in view
shrink1Display = Show(shrink1, renderView1)
# trace defaults for the display properties.
shrink1Display.ColorArrayName = ['CELLS', 'AbsolutePressure']
shrink1Display.LookupTable = absolutePressureLUT
shrink1Display.GlyphType = 'Arrow'
shrink1Display.ScalarOpacityUnitDistance = 0.0711182750127872
shrink1Display.SetScaleArray = [None, '']
shrink1Display.ScaleTransferFunction = 'PiecewiseFunction'
shrink1Display.OpacityArray = [None, '']
shrink1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
shrink1Display.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'AbsolutePressure'
absolutePressurePWF = GetOpacityTransferFunction('AbsolutePressure')
absolutePressurePWF.Points = [100096.4140625, 0.0, 0.5, 0.0, 101756.53125, 1.0, 0.5, 0.0]
absolutePressurePWF.ScalarRangeInitialized = 1

# current camera placement for renderView1
renderView1.CameraPosition = [-4.419775846624875, -5.682460492060888, 0.7195992913043833]
renderView1.CameraFocalPoint = [4.036058794663931, -0.36538663651064773, -0.37373222366498454]
renderView1.CameraViewUp = [0.2397273143941459, -0.18528119286318379, 0.952996166993638]
renderView1.CameraParallelScale = 6.745505525367322

# current camera placement for renderView1
renderView1.CameraPosition = [-4.419775846624875, -5.682460492060888, 0.7195992913043833]
renderView1.CameraFocalPoint = [4.036058794663931, -0.36538663651064773, -0.37373222366498454]
renderView1.CameraViewUp = [0.2397273143941459, -0.18528119286318379, 0.952996166993638]
renderView1.CameraParallelScale = 6.745505525367322

# save animation images/movie
WriteAnimation('/Users/keritaylor/LCS/ensightfiles/second_play.avi', Magnification=1, FrameRate=15.0, Compression=True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-4.419780000000001, -5.682459999999999, 0.7195989999999997]
renderView1.CameraFocalPoint = [4.036060000000001, -0.3653869999999999, -0.37373200000000006]
renderView1.CameraViewUp = [0.23972706478552874, -0.18528105007165474, 0.9529962575444144]
renderView1.CameraParallelScale = 6.74551

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
