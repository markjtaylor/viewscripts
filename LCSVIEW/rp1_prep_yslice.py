# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5


# get camera animation track for the view
cameraAnimationCue1_1 = GetCameraTrack(view=yslice_1.r_view)

# create keyframes for this animation track


# create a key frame
keyFrame6407 = CameraKeyFrame()
keyFrame6407.Position = [-5.591959449857433, 0.1509741441970938, 3.302553817126535]
keyFrame6407.FocalPoint = [2.2416279787634705, 0.08521598793475985, 0.548952439645099]
keyFrame6407.ViewUp = [0.3316174747658507, -0.0004729405927432705, 0.9434138152248547]
keyFrame6407.ParallelScale = 5.5743686526254885


keyFrame6408 = CameraKeyFrame()
keyFrame6408.KeyTime = 1.0
keyFrame6408.Position = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
keyFrame6408.FocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
keyFrame6408.ViewUp = [0.0, 0.0, 1.0]
keyFrame6408.ParallelScale = 4.960141706121346


# initialize the animation track
cameraAnimationCue1_1.KeyFrames = [keyFrame6407, keyFrame6408]

animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 25
