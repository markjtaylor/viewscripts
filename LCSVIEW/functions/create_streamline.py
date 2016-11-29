

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

