# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5


# get camera animation track for the view
cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

keyFrame6407 = CameraKeyFrame()
keyFrame6407.KeyTime = 0.0
keyFrame6407.Position = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
keyFrame6407.FocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
keyFrame6407.ViewUp = [0.0, 0.0, 1.0]
keyFrame6407.ParallelScale = 4.962978048511666

# create a key frame
keyFrame6408 = CameraKeyFrame()
keyFrame6408.KeyTime = 1.0
keyFrame6408.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6408.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6408.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6408.ParallelScale = 4.962978048511666


# initialize the animation track
cameraAnimationCue1_1.KeyFrames = [keyFrame6407, keyFrame6408]

animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 25
