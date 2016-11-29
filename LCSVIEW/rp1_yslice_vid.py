# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5


Show(yslice_1.master, yslice_1.r_view)

slice1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=yslice_1.master)

# create a key frame
keyFrame17002 = CompositeKeyFrame()
keyFrame17002.KeyValues = [-1.5]

# create a key frame
keyFrame17003 = CompositeKeyFrame()
keyFrame17003.KeyTime = 1.0
keyFrame17003.KeyValues = [4.0]

slice1ContourValuesTrack.KeyFrames = [keyFrame17002, keyFrame17003]


yslice_1.r_view.CameraPosition = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
yslice_1.r_view.CameraFocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
yslice_1.r_view.CameraViewUp =  [0.0, 0.0, 1.0]
yslice_1.r_view.CameraParallelScale = 4.960141706121346



# initialize the animation track


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
