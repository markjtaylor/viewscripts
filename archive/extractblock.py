#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
extractSurface1 = FindSource('ExtractSurface1')

# create a new 'Extract Block'
extractBlock2 = ExtractBlock(Input=extractSurface1)

# find source
tube1 = FindSource('Tube1')

# find source
streamTracer2 = FindSource('StreamTracer2')

# find source
slice1 = FindSource('Slice1')

# Properties modified on extractBlock2
extractBlock2.BlockIndices = [2]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# get color transfer function/color map for 'AbsolutePressure'
absolutePressureLUT = GetColorTransferFunction('AbsolutePressure')
absolutePressureLUT.RGBPoints = [93204.5234375, 0.231373, 0.298039, 0.752941, 98663.83984375, 0.865003, 0.865003, 0.865003, 104123.15625, 0.705882, 0.0156863, 0.14902]
absolutePressureLUT.ScalarRangeInitialized = 1.0

# show data in view
extractBlock2Display = Show(extractBlock2, renderView1)
# trace defaults for the display properties.
extractBlock2Display.ColorArrayName = ['CELLS', 'AbsolutePressure']
extractBlock2Display.LookupTable = absolutePressureLUT
extractBlock2Display.GlyphType = 'Arrow'
extractBlock2Display.SetScaleArray = [None, '']
extractBlock2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractBlock2Display.OpacityArray = [None, '']
extractBlock2Display.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
extractBlock2Display.SetScalarBarVisibility(renderView1, True)

# find source
extractSelection1 = FindSource('ExtractSelection1')

# find source
extractBlock1 = FindSource('ExtractBlock1')

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
clip1 = FindSource('Clip1')

# find source
streamTracer1 = FindSource('StreamTracer1')

# get opacity transfer function/opacity map for 'AbsolutePressure'
absolutePressurePWF = GetOpacityTransferFunction('AbsolutePressure')
absolutePressurePWF.Points = [93204.5234375, 0.0, 0.5, 0.0, 104123.15625, 1.0, 0.5, 0.0]
absolutePressurePWF.ScalarRangeInitialized = 1

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.007671878185092, -1.4124847039233812, 0.6634002118208335]
renderView1.CameraFocalPoint = [0.7703385502099991, -0.457888275384903, 0.31779877841472626]
renderView1.CameraViewUp = [0.14452932918374892, -0.06309162049196576, 0.9874870735505319]
renderView1.CameraParallelScale = 0.7655111610903408

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).