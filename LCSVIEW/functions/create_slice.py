
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

