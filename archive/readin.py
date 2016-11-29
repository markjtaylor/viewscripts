#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
elemental_star1m300kcase = EnSightReader(CaseFileName='/Users/keritaylor/LCS/ensightfiles/inp_rp1/elemental_star1m300k.case')
elemental_star1m300kcase.CellArrays = ['AbsolutePressure', 'Density', 'Pressure', 'PressureCoefficient', 'TotalPressureCoefficient', 'TurbulentDissipationRate', 'TurbulentKineticEnergy', 'VelocityMagnitude', 'Velocityi', 'Velocityj', 'Velocityk', 'WallY', 'Velocity']

# find source
enSightReader2 = FindSource('EnSightReader2')

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
elemental_star1m300kcase_1 = FindSource('elemental_star1m300k.case')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# get color transfer function/color map for 'AbsolutePressure'
absolutePressureLUT = GetColorTransferFunction('AbsolutePressure')
absolutePressureLUT.RGBPoints = [100096.4140625, 0.231373, 0.298039, 0.752941, 100926.47265625, 0.865003, 0.865003, 0.865003, 101756.53125, 0.705882, 0.0156863, 0.14902]
absolutePressureLUT.ScalarRangeInitialized = 1.0

# show data in view
elemental_star1m300kcaseDisplay = Show(elemental_star1m300kcase, renderView1)
# trace defaults for the display properties.
elemental_star1m300kcaseDisplay.ColorArrayName = ['CELLS', 'AbsolutePressure']
elemental_star1m300kcaseDisplay.LookupTable = absolutePressureLUT
elemental_star1m300kcaseDisplay.GlyphType = 'Arrow'
elemental_star1m300kcaseDisplay.ScalarOpacityUnitDistance = 0.07987112137848386
elemental_star1m300kcaseDisplay.SetScaleArray = [None, '']
elemental_star1m300kcaseDisplay.ScaleTransferFunction = 'PiecewiseFunction'
elemental_star1m300kcaseDisplay.OpacityArray = [None, '']
elemental_star1m300kcaseDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
elemental_star1m300kcaseDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'AbsolutePressure'
absolutePressurePWF = GetOpacityTransferFunction('AbsolutePressure')
absolutePressurePWF.Points = [100096.4140625, 0.0, 0.5, 0.0, 101756.53125, 1.0, 0.5, 0.0]
absolutePressurePWF.ScalarRangeInitialized = 1

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.455058822243128, 13.329107241734313, 9.183873080779295]
renderView1.CameraFocalPoint = [2.7499999999999964, -1.2499999985556212, 0.7500000000000014]
renderView1.CameraViewUp = [0.35085000026626834, -0.3910308566804191, 0.8508813938716354]
renderView1.CameraParallelScale = 4.493050189304694

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).