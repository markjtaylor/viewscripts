
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







