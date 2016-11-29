# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5


Show(slice2, renderView1)

slice2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=slice2)

# create a key frame
keyFrame17002 = CompositeKeyFrame()
keyFrame17002.KeyValues = [-1.50]

# create a key frame
keyFrame17003 = CompositeKeyFrame()
keyFrame17003.KeyTime = 1.0
keyFrame17003.KeyValues = [4.00]

slice2ContourValuesTrack.KeyFrames = [keyFrame17002, keyFrame17003]

renderView1.CameraPosition = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
renderView1.CameraFocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
renderView1.CameraViewUp =  [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 4.960141706121346


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
