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

