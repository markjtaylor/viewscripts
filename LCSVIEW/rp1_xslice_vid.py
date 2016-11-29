# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5


Show(xslice_1.master, xslice_1.r_view)

slice1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=xslice_1.master)

# create a key frame
keyFrame17002 = CompositeKeyFrame()
keyFrame17002.KeyValues = [-2.98]

# create a key frame
keyFrame17003 = CompositeKeyFrame()
keyFrame17003.KeyTime = 1.0
keyFrame17003.KeyValues = [6.98]

slice1ContourValuesTrack.KeyFrames = [keyFrame17002, keyFrame17003]

#xslice_1.r_view.CameraPosition = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
#xslice_1.r_view.CameraFocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
#xslice_1.r_view.CameraViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
#xslice_1.r_view.CameraParallelScale = 4.960141706121346

xslice_1.r_view.CameraPosition = [-5.591959449857433, 0.1509741441970938, 3.302553817126535]
xslice_1.r_view.CameraFocalPoint = [2.2416279787634705, 0.08521598793475985, 0.548952439645099]
xslice_1.r_view.CameraViewUp = [0.3316174747658507, -0.0004729405927432705, 0.9434138152248547]
xslice_1.r_view.CameraParallelScale = 5.5743686526254885



# initialize the animation track


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
