#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# find source
clip1 = FindSource('Clip1')

# set active source
SetActiveSource(clip1)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-1228.5826416015625, 0.0, 0.0, 1.0, 431.5299987792969, 1.0, 0.0, 0.0]
pressureLUT.ColorSpace = 'HSV'
pressureLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pressureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-1228.5826416015625, 0.0, 0.5, 0.0, 431.5299987792969, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# hide data in view
Hide(clip1, renderView1)

# create a new 'Reflect'
reflect1 = Reflect(Input=clip1)

# Properties modified on reflect1
reflect1.Plane = 'Y'

# get color transfer function/color map for 'AbsolutePressure'
absolutePressureLUT = GetColorTransferFunction('AbsolutePressure')
absolutePressureLUT.RGBPoints = [100096.4140625, 0.231373, 0.298039, 0.752941, 100926.47265625, 0.865003, 0.865003, 0.865003, 101756.53125, 0.705882, 0.0156863, 0.14902]
absolutePressureLUT.ScalarRangeInitialized = 1.0

# show data in view
reflect1Display = Show(reflect1, renderView1)
# trace defaults for the display properties.
reflect1Display.ColorArrayName = ['CELLS', 'AbsolutePressure']
reflect1Display.LookupTable = absolutePressureLUT
reflect1Display.GlyphType = 'Arrow'
reflect1Display.ScalarOpacityUnitDistance = 0.060457659070088605
reflect1Display.SetScaleArray = [None, '']
reflect1Display.ScaleTransferFunction = 'PiecewiseFunction'
reflect1Display.OpacityArray = [None, '']
reflect1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# find source
shrink1 = FindSource('Shrink1')

# find source
streamTracer1 = FindSource('StreamTracer1')

# find source
streamTracer2 = FindSource('StreamTracer2')

# find source
tube1 = FindSource('Tube1')

# find source
slice1 = FindSource('Slice1')

# find source
contour1 = FindSource('Contour1')

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
extractSurface1 = FindSource('ExtractSurface1')

# get opacity transfer function/opacity map for 'AbsolutePressure'
absolutePressurePWF = GetOpacityTransferFunction('AbsolutePressure')
absolutePressurePWF.Points = [100096.4140625, 0.0, 0.5, 0.0, 101756.53125, 1.0, 0.5, 0.0]
absolutePressurePWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(clip1)

# hide data in view
Hide(reflect1, renderView1)

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.ColorArrayName = ['CELLS', 'Pressure']
clip1Display.LookupTable = pressureLUT
clip1Display.GlyphType = 'Arrow'
clip1Display.ScalarOpacityUnitDistance = 0.0711182750127872
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# destroy reflect1
Delete(reflect1)
del reflect1

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.45566764458166, -8.563557973332257, -0.19368873935110303]
renderView1.CameraFocalPoint = [3.0755011772196097, -0.41871381594076784, -0.18559994155536275]
renderView1.CameraViewUp = [0.05321949289776696, -0.01157585207150332, 0.9985157411000206]
renderView1.CameraParallelScale = 6.74551

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).