# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

Hide(streamTracer4, renderView1)
Hide(streamTracer5, renderView1)
Hide(streamTracer6, renderView1)
Hide(streamTracer7, renderView1)
Hide(streamTracer8, renderView1)

Show(slice1, renderView1)

slice1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=slice1)

# create a key frame
keyFrame17002 = CompositeKeyFrame()
keyFrame17002.KeyValues = [-4.98]

# create a key frame
keyFrame17003 = CompositeKeyFrame()
keyFrame17003.KeyTime = 1.0
keyFrame17003.KeyValues = [4.98]

slice1ContourValuesTrack.KeyFrames = [keyFrame17002, keyFrame17003]

renderView1.CameraPosition = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
renderView1.CameraFocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
renderView1.CameraViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
renderView1.CameraParallelScale = 4.960141706121346



# initialize the animation track


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
