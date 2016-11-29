
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

