
# find source
streamTracer2 = FindSource('StreamTracer2')

# create a new 'Contour'
contour1 = Contour(Input=streamTracer2)
contour1.ContourBy = ['POINTS', 'IntegrationTime']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [803, 491]

# show data in view
contour1Display = Show(contour1, renderView1)

# hide data in view
Hide(streamTracer2, renderView1)


# Properties modified on contour1Display
contour1Display.GlyphType = 'Sphere'

# Properties modified on contour1Display.GlyphType
contour1Display.GlyphType.Radius = 0.03

ColorBy(contour1Display, ('POINTS', '_MRL_Velocity'))

# change representation type
contour1Display.SetRepresentationType('3D Glyphs')

# Properties modified on contour1Display
contour1Display.SetScaleArray = [None, 'AngularVelocity']

# Properties modified on contour1Display
contour1Display.OpacityArray = [None, 'AngularVelocity']

# set scalar coloring
ColorBy(contour1Display, ('POINTS', '_MRL_Velocity'))


# get animation track
contour1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=contour1)

# create keyframes for this animation track

# create a key frame
keyFrame6379 = CompositeKeyFrame()

# create a key frame
keyFrame6380 = CompositeKeyFrame()
keyFrame6380.KeyTime = 1.0
keyFrame6380.KeyValues = [0.12787830847213727]

# initialize the animation track
contour1ContourValuesTrack.KeyFrames = [keyFrame6379, keyFrame6380]

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'MRLVelocity'
mRLVelocityLUT = GetColorTransferFunction('MRLVelocity')
mRLVelocityLUT.RGBPoints = [46.56043112903288, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
mRLVelocityLUT.ColorSpace = 'HSV'
mRLVelocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
mRLVelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'MRLVelocity'
mRLVelocityPWF = GetOpacityTransferFunction('MRLVelocity')
mRLVelocityPWF.Points = [46.56043112903288, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
mRLVelocityPWF.ScalarRangeInitialized = 1

# hide color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.9282228297255046, 1.1921335145632892, 2.0378323114544195]
renderView1.CameraFocalPoint = [1.0798208713531545, -0.6096000075340238, 0.40600070911750713]
renderView1.CameraViewUp = [0.2686089945940614, -0.24596129375734, 0.9313174807746192]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
