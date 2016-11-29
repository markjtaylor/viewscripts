
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


