#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
naca12 = EnSightReader(CaseFileName='/Users/keritaylor/LCS/ensightfiles/inp_naca0012/MESH_06M/fw271981.case')
naca12.CellArrays = ['AbsolutePressure', 'Density', 'Pressure',  '_MRL_skinFriction', '_MRL_Velocity']


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
