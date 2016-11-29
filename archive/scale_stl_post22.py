#### import the simple module from the paraview
import os
import sys

from paraview.simple import *

#### disable automatic camera reset on 'Show'

renderView1 = GetActiveViewOrCreate('RenderView')

l36stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L36.stl'])
l36stlDisplay = Show(l36stl, renderView1)
transform1 = Transform(Input=l36stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l36stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L36_scale.stl', proxy=transform1)
Hide(transform1, renderView1)

l73stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L73.stl'])
l73stlDisplay = Show(l73stl, renderView1)
transform1 = Transform(Input=l73stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l73stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L73_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l50stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L50.stl'])
l50stlDisplay = Show(l50stl, renderView1)
transform1 = Transform(Input=l50stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l50stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L50_scale.stl', proxy=transform1)
Hide(transform1, renderView1)

l51stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L51.stl'])
l51stlDisplay = Show(l51stl, renderView1)
transform1 = Transform(Input=l51stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l51stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L51_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l52stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L52.stl'])
l52stlDisplay = Show(l52stl, renderView1)
transform1 = Transform(Input=l52stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l52stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L52_scale.stl', proxy=transform1)
Hide(transform1, renderView1)



l53stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L53.stl'])
l53stlDisplay = Show(l53stl, renderView1)
transform1 = Transform(Input=l53stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l53stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L53_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l54stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L54.stl'])
l54stlDisplay = Show(l54stl, renderView1)
transform1 = Transform(Input=l54stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l54stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L54_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l58stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L58.stl'])
l58stlDisplay = Show(l58stl, renderView1)
transform1 = Transform(Input=l58stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l58stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L58_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l60stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L60.stl'])
l60stlDisplay = Show(l60stl, renderView1)
transform1 = Transform(Input=l60stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l60stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L60_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l61stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L61.stl'])
l61stlDisplay = Show(l61stl, renderView1)
transform1 = Transform(Input=l61stl)
transform1.Transform = 'Transform'
Hide3DWidgets(proxy=transform1)
transform1.Transform.Scale = [0.001, 0.001, 0.001]
transform1Display = Show(transform1, renderView1)
Hide(l61stl, renderView1)
transform1Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L61_scale.stl', proxy=transform1)
Hide(transform1, renderView1)


l56stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L56.stl'])
l56stlDisplay = Show(l56stl, renderView1)
transform2 = Transform(Input=l56stl)
transform2.Transform = 'Transform'
Hide3DWidgets(proxy=transform2)
transform2.Transform.Scale = [0.001, 0.001, 0.001]
transform2Display = Show(transform2, renderView1)
Hide(l56stl, renderView1)
transform2Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L56_scale.stl', proxy=transform2)
Hide(transform2, renderView1)

l55stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L55.stl'])
l55stlDisplay = Show(l55stl, renderView1)
transform3 = Transform(Input=l55stl)
transform3.Transform = 'Transform'
Hide3DWidgets(proxy=transform3)
transform3.Transform.Scale = [0.001, 0.001, 0.001]
transform3Display = Show(transform3, renderView1)
Hide(l55stl, renderView1)
transform3Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L55_scale.stl', proxy=transform3)
Hide(transform3, renderView1)

l57stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L57.stl'])
l57stlDisplay = Show(l57stl, renderView1)
transform4 = Transform(Input=l57stl)
transform4.Transform = 'Transform'
Hide3DWidgets(proxy=transform4)
transform4.Transform.Scale = [0.001, 0.001, 0.001]
transform4Display = Show(transform4, renderView1)
Hide(l57stl, renderView1)
transform4Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L57_scale.stl', proxy=transform4)
Hide(transform4, renderView1)

l70stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L70.stl'])
l70stlDisplay = Show(l70stl, renderView1)
transform5 = Transform(Input=l70stl)
transform5.Transform = 'Transform'
Hide3DWidgets(proxy=transform5)
transform5.Transform.Scale = [0.001, 0.001, 0.001]
transform5Display = Show(transform5, renderView1)
Hide(l70stl, renderView1)
transform5Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L70_scale.stl', proxy=transform5)
Hide(transform5, renderView1)

l730stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L730.stl'])
l730stlDisplay = Show(l730stl, renderView1)
transform6 = Transform(Input=l730stl)
transform6.Transform = 'Transform'
Hide3DWidgets(proxy=transform6)
transform6.Transform.Scale = [0.001, 0.001, 0.001]
transform6Display = Show(transform6, renderView1)
Hide(l730stl, renderView1)
transform6Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L730_scale.stl', proxy=transform6)
Hide(transform6, renderView1)

l780stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L780.stl'])
l780stlDisplay = Show(l780stl, renderView1)
transform7 = Transform(Input=l780stl)
transform7.Transform = 'Transform'
Hide3DWidgets(proxy=transform7)
transform7.Transform.Scale = [0.001, 0.001, 0.001]
transform7Display = Show(transform7, renderView1)
Hide(l780stl, renderView1)
transform7Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L780_scale.stl', proxy=transform7)
Hide(transform7, renderView1)


l781stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L781.stl'])
l781stlDisplay = Show(l781stl, renderView1)
transform8 = Transform(Input=l781stl)
transform8.Transform = 'Transform'
Hide3DWidgets(proxy=transform8)
transform8.Transform.Scale = [0.001, 0.001, 0.001]
transform8Display = Show(transform8, renderView1)
Hide(l781stl, renderView1)
transform8Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L781_scale.stl', proxy=transform8)
Hide(transform8, renderView1)


l902stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L902.stl'])
l902stlDisplay = Show(l902stl, renderView1)
transform9 = Transform(Input=l902stl)
transform9.Transform = 'Transform'
Hide3DWidgets(proxy=transform9)
transform9.Transform.Scale = [0.001, 0.001, 0.001]
transform9Display = Show(transform9, renderView1)
Hide(l902stl, renderView1)
transform9Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L902_scale.stl', proxy=transform9)
Hide(transform9, renderView1)


l901stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L901.stl'])
l901stlDisplay = Show(l901stl, renderView1)
transform10 = Transform(Input=l901stl)
transform10.Transform = 'Transform'
Hide3DWidgets(proxy=transform10)
transform10.Transform.Scale = [0.001, 0.001, 0.001]
transform10Display = Show(transform10, renderView1)
Hide(l901stl, renderView1)
transform10Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L901_scale.stl', proxy=transform10)
Hide(transform10, renderView1)

l903stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L903.stl'])
l903stlDisplay = Show(l903stl, renderView1)
transform12 = Transform(Input=l903stl)
transform12.Transform = 'Transform'
Hide3DWidgets(proxy=transform12)
transform12.Transform.Scale = [0.001, 0.001, 0.001]
transform12Display = Show(transform12, renderView1)
Hide(l903stl, renderView1)
transform12Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L903_scale.stl', proxy=transform12)
Hide(transform12, renderView1)


l904stl = STLReader(FileNames=['/Users/keritaylor/Dropbox/Elemental Data for Mark T/CFD022/STL/L904.stl'])
l904stlDisplay = Show(l904stl, renderView1)
transform12 = Transform(Input=l904stl)
transform12.Transform = 'Transform'
Hide3DWidgets(proxy=transform12)
transform12.Transform.Scale = [0.001, 0.001, 0.001]
transform12Display = Show(transform12, renderView1)
Hide(l904stl, renderView1)
transform12Display.SetScalarBarVisibility(renderView1, True)
renderView1.ResetCamera()
SaveData('/Users/keritaylor/LCS/ensightfiles/CFD022/L904_scale.stl', proxy=transform12)
Hide(transform12, renderView1)









