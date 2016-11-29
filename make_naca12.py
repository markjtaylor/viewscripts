#### import the simple module from the paraview

from paraview.simple import *
from paraview.servermanager import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
naca12 = EnSightReader(CaseFileName='/Users/mark/LCS/ensightfiles/inp_naca0012/MESH_06M/fw271981.case')
naca12.CellArrays = ['AbsolutePressure', 'Density', 'Pressure',  '_MRL_skinFriction', '_MRL_Velocity', '_MRL_skinFrictionU', '_MRL_skinFrictionV', '_MRL_skinFrictionW' ]


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

naca12Display = GetDisplayProperties(naca12, view=renderView1)

# set scalar coloring
ColorBy(naca12Display, ('CELLS', 'Pressure'))

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-8120.47607421875, 0.231373, 0.298039, 0.752941, -2661.160400390625, 0.865003, 0.865003, 0.865003, 2798.1552734375, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-8120.47607421875, 0.0, 0.5, 0.0, 2798.1552734375, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function
pressureLUT.RescaleTransferFunction(-8000.0, 2500.0)

# Rescale transfer function
pressurePWF.RescaleTransferFunction(-8000.0, 2500.0)

# show data in view
naca12Display.SetScalarBarVisibility(renderView1, False)
naca12Display = Show(naca12, renderView1)
Hide(naca12, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# find source
#naca12 = FindSource('naca12')

# create a new 'Extract Block'
wing = ExtractBlock(Input=naca12)

# we want the second block 
wing.BlockIndices = [2]


wingDisplay = GetDisplayProperties(wing, view=renderView1)

ColorBy(wingDisplay, ('CELLS', 'Pressure'))


# show data in view
wingDisplay = Show(wing, renderView1)

# reset view to fit data
renderView1.ResetCamera()


#now lets do some streamlines

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=naca12,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['CELLS', '_MRL_Velocity']
streamTracer1.MaximumStreamlineLength = 13.411200046539307

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'FORWARD'

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [0.3, -0.7, 0.3]
streamTracer1.SeedType.Point2 = [0.3, -0.5, 0.3]
streamTracer1.SeedType.Resolution = 12

Hide3DWidgets(proxy=streamTracer1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# show data in view
streamTracer1Display = GetDisplayProperties(streamTracer1, view=renderView1)

streamTracer1Display = Show(streamTracer1, renderView1)
ColorBy(streamTracer1Display, ('POINTS', '_MRL_Velocity'))

# hide data in view

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True)


# get color transfer function/color map for 'MRLVelocity'
mRLVelocityLUT = GetColorTransferFunction('MRLVelocity')
mRLVelocityLUT.RGBPoints = [55.946010717046455, 0.231373, 0.298039, 0.752941, 80.34874800973748, 0.865003, 0.865003, 0.865003, 104.75148530242849, 0.705882, 0.0156863, 0.14902]
mRLVelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'MRLVelocity'
mRLVelocityPWF = GetOpacityTransferFunction('MRLVelocity')
mRLVelocityPWF.Points = [55.946010717046455, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
mRLVelocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mRLVelocityLUT.ApplyPreset('Blue to Red Rainbow', True)

# hide color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, False)


#show data in view
streamTracer1Display = Show(streamTracer1, renderView1)


# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']

# Properties modified on tube1
tube1.Radius = 0.008435356878489255
tube1.NumberofSides = 12

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# get color transfer function/color map for 'MRLVelocity'
mRLVelocityLUT = GetColorTransferFunction('MRLVelocity')
mRLVelocityLUT.RGBPoints = [55.946010717046455, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
mRLVelocityLUT.ColorSpace = 'HSV'
mRLVelocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
mRLVelocityLUT.ScalarRangeInitialized = 1.0

# show data in view
tube1Display = Show(tube1, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, False)

# Properties modified on tube1Display
tube1Display.Opacity = 0.54

#now make a second streamline set (which would be used for a particle animation

SetActiveSource(naca12)

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=naca12,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['CELLS', '_MRL_Velocity']
streamTracer2.MaximumStreamlineLength = 13.411200046539307

# Properties modified on streamTracer2
streamTracer2.IntegrationDirection = 'FORWARD'

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [-0.1, -0.5, 0.15]
streamTracer2.SeedType.Point2 = [-0.1, -0.5, 0.55]
streamTracer2.SeedType.Resolution = 12

Hide3DWidgets(proxy=streamTracer2)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# show data in view
streamTracer2Display = GetDisplayProperties(streamTracer2, view=renderView1)

streamTracer2Display = Show(streamTracer2, renderView1)
ColorBy(streamTracer2Display, ('POINTS', '_MRL_Velocity'))

# hide data in view

# rescale color and/or opacity maps used to include current data range
streamTracer2Display.RescaleTransferFunctionToDataRange(True)


# get color transfer function/color map for 'MRLVelocity'
mRLVelocityLUT = GetColorTransferFunction('MRLVelocity')
mRLVelocityLUT.RGBPoints = [55.946010717046455, 0.231373, 0.298039, 0.752941, 80.34874800973748, 0.865003, 0.865003, 0.865003, 104.75148530242849, 0.705882, 0.0156863, 0.14902]
mRLVelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'MRLVelocity'
mRLVelocityPWF = GetOpacityTransferFunction('MRLVelocity')
mRLVelocityPWF.Points = [55.946010717046455, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
mRLVelocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mRLVelocityLUT.ApplyPreset('Blue to Red Rainbow', True)

# hide color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, False)


#show data in view
streamTracer2Display = Show(streamTracer2, renderView1)

#think about using seed ids for this at the current value (blue is under aerofoil, red is above- use hard set values to relabel contour map?




#now make the clip plane 
SetActiveSource(naca12)

# create a new 'Slice'
slice1 = Slice(Input=naca12)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]


# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.7982087135315, -0.609600007534027, 0.40600070911750663]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

slice1Display = GetDisplayProperties(slice1, view=renderView1)


# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'Pressure'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-8120.47607421875, 0.231373, 0.298039, 0.752941, -2661.160400390625, 0.865003, 0.865003, 0.865003, 2798.1552734375, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-8120.47607421875, 0.0, 0.5, 0.0, 2798.1552734375, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function
pressureLUT.RescaleTransferFunction(-8000.0, 2500.0)

# Rescale transfer function
pressurePWF.RescaleTransferFunction(-8000.0, 2500.0)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1)

slice1Display.SetScalarBarVisibility(renderView1, False)


# show data in view
slice1Display = Show(slice1, renderView1)

# now I want the minimum pressure value at this plane and it's x location

slicept1 = CellDatatoPointData(Input=slice1)
slicept1Display = GetDisplayProperties(slicept1, view=renderView1)
slicept1Display.SetScalarBarVisibility(renderView1, False)

ColorBy(slicept1Display, ('POINTS', 'Pressure'))
slicept1Display = Show(slicept1, renderView1)

#min=100000
#numPoints=slicept1.GetDataInformation().GetNumberOfPoints()
#for i in range(0, numPoints):
#	if (min < slicept1.Pressure.GetValue(i)):
#		min = slicept1.Pressure.GetValue(i)
#		print(i,min)







