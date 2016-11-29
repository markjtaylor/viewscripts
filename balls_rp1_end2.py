# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

Show(streamTracer4, renderView1)
Show(streamTracer5, renderView1)
Show(streamTracer6, renderView1)
Show(streamTracer7, renderView1)
Show(streamTracer8, renderView1)

Hide(balls_1, renderView1)
Hide(balls_2, renderView1)
Hide(balls_3, renderView1)
Hide(balls_4, renderView1)
Hide(balls_5, renderView1)

Hide(secballs_1, renderView1)
Hide(secballs_2, renderView1)
Hide(secballs_3, renderView1)
Hide(secballs_4, renderView1)
Hide(secballs_5, renderView1)

Show(thiballs_1, renderView1)
Show(thiballs_2, renderView1)
Show(thiballs_3, renderView1)
Show(thiballs_4, renderView1)
Show(thiballs_5, renderView1)

Show(fouballs_1, renderView1)
Show(fouballs_2, renderView1)
Show(fouballs_3, renderView1)
Show(fouballs_4, renderView1)
Show(fouballs_5, renderView1)

balls_1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_1)
balls_2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_2)
balls_3ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_3)
balls_4ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_4)
balls_5ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_5)

secballs_1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=secballs_1)
secballs_2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=secballs_2)
secballs_3ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=secballs_3)
secballs_4ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=secballs_4)
secballs_5ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=secballs_5)

thiballs_1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=thiballs_1)
thiballs_2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=thiballs_2)
thiballs_3ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=thiballs_3)
thiballs_4ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=thiballs_4)
thiballs_5ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=thiballs_5)

fouballs_1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=fouballs_1)
fouballs_2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=fouballs_2)
fouballs_3ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=fouballs_3)
fouballs_4ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=fouballs_4)
fouballs_5ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=fouballs_5)


keyFa1 = CompositeKeyFrame()
keyFa2 = CompositeKeyFrame()


keyFa1.KeyTime = 0.0
keyFa1.KeyValues = [0.01]
keyFa2.KeyTime = 1.00
keyFa2.KeyValues = [.25]

balls_1ContourValuesTrack.KeyFrames = [ keyFa1, keyFa2]


keyFb1 = CompositeKeyFrame()
keyFb2 = CompositeKeyFrame()


keyFb1.KeyTime = 0.0
keyFb1.KeyValues = [0.01]
keyFb2.KeyTime = 1.0
keyFb2.KeyValues = [0.25]

balls_2ContourValuesTrack.KeyFrames = [ keyFb1, keyFb2]


keyFc1 = CompositeKeyFrame()
keyFc2 = CompositeKeyFrame()


keyFc1.KeyTime = 0.0
keyFc1.KeyValues = [0.01]
keyFc2.KeyTime = 1.0
keyFc2.KeyValues = [0.25]

balls_3ContourValuesTrack.KeyFrames = [ keyFc1, keyFc2]

keyFd1 = CompositeKeyFrame()
keyFd2 = CompositeKeyFrame()


keyFd1.KeyTime = 0.0
keyFd1.KeyValues = [0.01]
keyFd2.KeyTime = 1.0   
keyFd2.KeyValues = [0.25]

balls_4ContourValuesTrack.KeyFrames = [ keyFd1, keyFd2]


keyFe1 = CompositeKeyFrame()
keyFe2 = CompositeKeyFrame()


keyFe1.KeyTime = 0.0
keyFe1.KeyValues = [0.01]
keyFe2.KeyTime = 1.0
keyFe2.KeyValues = [0.25]

balls_5ContourValuesTrack.KeyFrames = [ keyFe1, keyFe2]

##########################################################################

keyGa1 = CompositeKeyFrame()
keyGa2 = CompositeKeyFrame()


keyGa1.KeyTime = 0.0
keyGa1.KeyValues = [0.26]
keyGa2.KeyTime = 1.00
keyGa2.KeyValues = [.50]

secballs_1ContourValuesTrack.KeyFrames = [ keyGa1, keyGa2]


keyGb1 = CompositeKeyFrame()
keyGb2 = CompositeKeyFrame()


keyGb1.KeyTime = 0.0
keyGb1.KeyValues = [0.26]
keyGb2.KeyTime = 1.0
keyGb2.KeyValues = [0.50]

secballs_2ContourValuesTrack.KeyFrames = [ keyGb1, keyGb2]


keyGc1 = CompositeKeyFrame()
keyGc2 = CompositeKeyFrame()


keyGc1.KeyTime = 0.0
keyGc1.KeyValues = [0.26]
keyGc2.KeyTime = 1.0
keyGc2.KeyValues = [0.50]

secballs_3ContourValuesTrack.KeyFrames = [ keyGc1, keyGc2]

keyGd1 = CompositeKeyFrame()
keyGd2 = CompositeKeyFrame()


keyGd1.KeyTime = 0.0
keyGd1.KeyValues = [0.26]
keyGd2.KeyTime = 1.0   
keyGd2.KeyValues = [0.50]

secballs_4ContourValuesTrack.KeyFrames = [ keyGd1, keyGd2]


keyGe1 = CompositeKeyFrame()
keyGe2 = CompositeKeyFrame()


keyGe1.KeyTime = 0.0
keyGe1.KeyValues = [0.26]
keyGe2.KeyTime = 1.0
keyGe2.KeyValues = [0.50]

secballs_5ContourValuesTrack.KeyFrames = [keyGe1, keyGe2]

##########################################################################

keyHa1 = CompositeKeyFrame()
keyHa2 = CompositeKeyFrame()


keyHa1.KeyTime = 0.0
keyHa1.KeyValues = [0.51]
keyHa2.KeyTime = 1.00
keyHa2.KeyValues = [.75]

thiballs_1ContourValuesTrack.KeyFrames = [ keyHa1, keyHa2]


keyHb1 = CompositeKeyFrame()
keyHb2 = CompositeKeyFrame()


keyHb1.KeyTime = 0.0
keyHb1.KeyValues = [0.51]
keyHb2.KeyTime = 1.0
keyHb2.KeyValues = [0.75]

thiballs_2ContourValuesTrack.KeyFrames = [ keyHb1, keyHb2]


keyHc1 = CompositeKeyFrame()
keyHc2 = CompositeKeyFrame()


keyHc1.KeyTime = 0.0
keyHc1.KeyValues = [0.51]
keyHc2.KeyTime = 1.0
keyHc2.KeyValues = [0.75]

thiballs_3ContourValuesTrack.KeyFrames = [ keyHc1, keyHc2]

keyHd1 = CompositeKeyFrame()
keyHd2 = CompositeKeyFrame()


keyHd1.KeyTime = 0.0
keyHd1.KeyValues = [0.51]
keyHd2.KeyTime = 1.0   
keyHd2.KeyValues = [0.75]

thiballs_4ContourValuesTrack.KeyFrames = [ keyHd1, keyHd2]


keyHe1 = CompositeKeyFrame()
keyHe2 = CompositeKeyFrame()


keyHe1.KeyTime = 0.0
keyHe1.KeyValues = [0.51]
keyHe2.KeyTime = 1.0
keyHe2.KeyValues = [0.75]

thiballs_5ContourValuesTrack.KeyFrames = [ keyHe1, keyHe2]


#####################################################################################

keyIa1 = CompositeKeyFrame()
keyIa2 = CompositeKeyFrame()


keyIa1.KeyTime = 0.0
keyIa1.KeyValues = [0.76]
keyIa2.KeyTime = 1.00
keyIa2.KeyValues = [1.00]

fouballs_1ContourValuesTrack.KeyFrames = [ keyIa1, keyIa2]


keyIb1 = CompositeKeyFrame()
keyIb2 = CompositeKeyFrame()


keyIb1.KeyTime = 0.0
keyIb1.KeyValues = [0.76]
keyIb2.KeyTime = 1.0
keyIb2.KeyValues = [1.0]

fouballs_2ContourValuesTrack.KeyFrames = [ keyIb1, keyIb2]


keyIc1 = CompositeKeyFrame()
keyIc2 = CompositeKeyFrame()


keyIc1.KeyTime = 0.0
keyIc1.KeyValues = [0.76]
keyIc2.KeyTime = 1.0
keyIc2.KeyValues = [1.00]

fouballs_3ContourValuesTrack.KeyFrames = [ keyIc1, keyIc2]

keyId1 = CompositeKeyFrame()
keyId2 = CompositeKeyFrame()


keyId1.KeyTime = 0.0
keyId1.KeyValues = [0.76]
keyId2.KeyTime = 1.0   
keyId2.KeyValues = [1.00]

fouballs_4ContourValuesTrack.KeyFrames = [ keyId1, keyId2]


keyIe1 = CompositeKeyFrame()
keyIe2 = CompositeKeyFrame()


keyIe1.KeyTime = 0.0
keyIe1.KeyValues = [0.76]
keyIe2.KeyTime = 1.0
keyIe2.KeyValues = [1.00]

fouballs_5ContourValuesTrack.KeyFrames = [ keyIe1, keyIe2]

#######################################################################

#renderView1.CameraPosition = [-3.0695652890450127, -2.956670692061946, 2.8719589858417587]
#renderView1.CameraFocalPoint = [2.4869069333622393, 0.8111934860219328, -0.21388773056320454]
#renderView1.CameraViewUp = [0.31461402249359816, 0.2790811690661092, 0.9072660678781564]
#renderView1.CameraParallelScale = 4.960141706121346

renderView1.CameraPosition = [-2.3153101614821034, -3.227385583658042, 1.1763321443941273]
renderView1.CameraFocalPoint = [2.1425481742297974, 0.8776876655563869, 0.39741223133748194]
renderView1.CameraViewUp = [0.10754311783223755, 0.0713732469455578, 0.9916351836372942]
renderView1.CameraParallelScale = 4.962978048511666

execfile('/Users/keritaylor/LCS/ParaviewScripts/sub_movewheel.py')

animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 25

#animationScene1.Play()





