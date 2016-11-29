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

Hide(thiballs_1, renderView1)
Hide(thiballs_2, renderView1)
Hide(thiballs_3, renderView1)
Hide(thiballs_4, renderView1)
Hide(thiballs_5, renderView1)

Hide(fouballs_1, renderView1)
Hide(fouballs_2, renderView1)
Hide(fouballs_3, renderView1)
Hide(fouballs_4, renderView1)
Hide(fouballs_5, renderView1)


renderView1.CameraPosition = [-3.0695652890450127, -2.956670692061946, 2.8719589858417587]
renderView1.CameraFocalPoint = [2.4869069333622393, 0.8111934860219328, -0.21388773056320454]
renderView1.CameraViewUp = [0.31461402249359816, 0.2790811690661092, 0.9072660678781564]
renderView1.CameraParallelScale = 4.960141706121346

# current camera placement for renderView1
renderView1.CameraPosition = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
renderView1.CameraFocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
renderView1.CameraViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
renderView1.CameraParallelScale = 4.962978048511666

# get camera animation track for the view
cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame6405 = CameraKeyFrame()
keyFrame6405.Position = [-3.0695652890450127, -2.956670692061946, 2.8719589858417587]
keyFrame6405.FocalPoint =  [2.4869069333622393, 0.8111934860219328, -0.21388773056320454]
keyFrame6405.ViewUp =  [0.31461402249359816, 0.2790811690661092, 0.9072660678781564]
keyFrame6405.ParallelScale = 4.960141706121346

# create a key frame
keyFrame6406 = CameraKeyFrame()
keyFrame6406.KeyTime = 1.0
keyFrame6406.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6406.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6406.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6406.ParallelScale = 4.962978048511666

# initialize the animation track
cameraAnimationCue1_1.KeyFrames = [keyFrame6405, keyFrame6406]

animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 25
