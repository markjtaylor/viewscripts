# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

#streamTracer9SeedTypePoint1Track = GetAnimationTrack('Point1', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint2Track = GetAnimationTrack('Point2', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint1Track.KeyFrames = [keyFrame16980, keyFrame16981]

Hide(road, renderView1)
Show(ytube, renderView1)

streamTracer2SeedTypePoint1Track = GetAnimationTrack('Point1', index=1, proxy=streamTracer2.SeedType)


# create a key frame
keyFrame17000 = CompositeKeyFrame()
keyFrame17001 = CompositeKeyFrame()
keyFrame17002 = CompositeKeyFrame()
keyFrame17003 = CompositeKeyFrame()
keyFrame17004 = CompositeKeyFrame()
keyFrame17005 = CompositeKeyFrame()
keyFrame17006 = CompositeKeyFrame()
keyFrame17007 = CompositeKeyFrame()
keyFrame17008 = CompositeKeyFrame()
keyFrame17009 = CompositeKeyFrame()
keyFrame17010 = CompositeKeyFrame()

keyFrame17000.KeyValues = [-1.10]
keyFrame17001.KeyValues = [1.10]
keyFrame17002.KeyValues = [-1.10]
keyFrame17003.KeyValues = [1.10]
keyFrame17004.KeyValues = [-1.10]
keyFrame17005.KeyValues = [1.10]
keyFrame17006.KeyValues = [-1.10]
keyFrame17007.KeyValues = [1.10]
keyFrame17008.KeyValues = [-1.10]
keyFrame17009.KeyValues = [1.10]
keyFrame17010.KeyValues = [-1.10]

keyFrame17000.KeyTime = [0.]
keyFrame17001.KeyTime = [.10]
keyFrame17002.KeyTime = [.20]
keyFrame17003.KeyTime = [.30]
keyFrame17004.KeyTime = [.40]
keyFrame17005.KeyTime = [.50]
keyFrame17006.KeyTime = [.60]
keyFrame17007.KeyTime = [.70]
keyFrame17008.KeyTime = [.80]
keyFrame17009.KeyTime = [.90]
keyFrame17010.KeyTime = [1.00]

# create a key frame

streamTracer2SeedTypePoint1Track.KeyFrames = [keyFrame17000, keyFrame17001, keyFrame17002, keyFrame17003, keyFrame17004, keyFrame17005, keyFrame17006, keyFrame17007,keyFrame17008, keyFrame17009 , keyFrame17010]

streamTracer2SeedTypePoint2Track = GetAnimationTrack('Point2', index=1, proxy=streamTracer2.SeedType)

# create a key frame
keyFrame18000 = CompositeKeyFrame()
keyFrame18001 = CompositeKeyFrame()
keyFrame18002 = CompositeKeyFrame()
keyFrame18003 = CompositeKeyFrame()
keyFrame18004 = CompositeKeyFrame()
keyFrame18005 = CompositeKeyFrame()
keyFrame18006 = CompositeKeyFrame()
keyFrame18007 = CompositeKeyFrame()
keyFrame18008 = CompositeKeyFrame()
keyFrame18009 = CompositeKeyFrame()
keyFrame18010 = CompositeKeyFrame()

keyFrame18000.KeyValues = [-1.10]
keyFrame18001.KeyValues = [1.10]
keyFrame18002.KeyValues = [-1.10]
keyFrame18003.KeyValues = [1.10]
keyFrame18004.KeyValues = [-1.10]
keyFrame18005.KeyValues = [1.10]
keyFrame18006.KeyValues = [-1.10]
keyFrame18007.KeyValues = [1.10]
keyFrame18008.KeyValues = [-1.10]
keyFrame18009.KeyValues = [1.10]
keyFrame18010.KeyValues = [-1.10]

keyFrame18000.KeyTime = [0.]
keyFrame18001.KeyTime = [.10]
keyFrame18002.KeyTime = [.20]
keyFrame18003.KeyTime = [.30]
keyFrame18004.KeyTime = [.40]
keyFrame18005.KeyTime = [.50]
keyFrame18006.KeyTime = [.60]
keyFrame18007.KeyTime = [.70]
keyFrame18008.KeyTime = [.80]
keyFrame18009.KeyTime = [.90]
keyFrame18010.KeyTime = [1.00]


streamTracer2SeedTypePoint2Track.KeyFrames = [keyFrame18000, keyFrame18001, keyFrame18002, keyFrame18003, keyFrame18004, keyFrame18005, keyFrame18006, keyFrame18007,keyFrame18008, keyFrame18009 , keyFrame18010]

#renderView1.CameraPosition = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
#renderView1.CameraFocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
#renderView1.CameraViewUp =  [0.0, 0.0, 1.0]
#renderView1.CameraParallelScale = 4.960141706121346

cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

keyFrame6400 = CameraKeyFrame()
keyFrame6400.KeyTime = 0.0
keyFrame6400.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6400.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6400.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6400.ParallelScale = 4.962978048511666

keyFrame6401 = CameraKeyFrame()
keyFrame6401.KeyTime = 0.1
keyFrame6401.Position = [-.9,4.68,3.05]
keyFrame6401.FocalPoint = [2.52, -.68,-.070]
keyFrame6401.ViewUp = [.179,-.400, .89]
keyFrame6401.ParallelScale = 4.962978048511666

keyFrame6402 = CameraKeyFrame()
keyFrame6402.KeyTime = 0.2
keyFrame6402.Position = [1.786,4.37,-1.73]
keyFrame6402.FocalPoint = [2.733,-1.38,1.3]
keyFrame6402.ViewUp = [-.188,.339,.921]
keyFrame6402.ParallelScale = 4.962978048511666

keyFrame6403 = CameraKeyFrame()
keyFrame6403.KeyTime = 0.3
keyFrame6403.Position = [.287,3.52,-4.73]
keyFrame6403.FocalPoint = [2.279,-.938,1.505]
keyFrame6403.ViewUp = [-.4044,.677,.6144]
keyFrame6403.ParallelScale = 4.962978048511666


keyFrame6404 = CameraKeyFrame()
keyFrame6404.KeyTime = 0.4
keyFrame6404.Position = [2.422,.541,-6.49]
keyFrame6404.FocalPoint = [1.81,-.221,1.367]
keyFrame6404.ViewUp = [-.467,.882,.049]
keyFrame6404.ParallelScale = 4.962978048511666

keyFrame6405 = CameraKeyFrame()
keyFrame6405.KeyTime = 0.5
keyFrame6405.Position = [5.65,.03,-6.5]
keyFrame6405.FocalPoint = [2.136,-.275,.584]
keyFrame6405.ViewUp = [-.89,-.002,-.444]
keyFrame6405.ParallelScale = 4.962978048511666

keyFrame6406 = CameraKeyFrame()
keyFrame6406.KeyTime = 0.6
keyFrame6406.Position = [6.465,-5.43,-2.42]
keyFrame6406.FocalPoint = [2.89, -.508, .003]
keyFrame6406.ViewUp = [.649, -.1, -.753]
keyFrame6406.ParallelScale = 4.962978048511666

keyFrame6407 = CameraKeyFrame()
keyFrame6407.KeyTime = 0.7
keyFrame6407.Position = [2.61,-6.268,3.08]
keyFrame6407.FocalPoint = [1.858,-1.3,1.07]
keyFrame6407.ViewUp = [-.5,-.38,-.773]
keyFrame6407.ParallelScale = 4.962978048511666

keyFrame6408 = CameraKeyFrame()
keyFrame6408.KeyTime = 0.8
keyFrame6408.Position = [6.845,1.259,4.59]
keyFrame6408.FocalPoint = [2.837,.261,1.098]
keyFrame6408.ViewUp = [-.149,-.892,.426]
keyFrame6408.ParallelScale = 4.962978048511666


keyFrame6409 = CameraKeyFrame()
keyFrame6409.KeyTime = 0.9
keyFrame6409.Position = [1.5649,4.9395,2.439]
keyFrame6409.FocalPoint = [2.344,-1.012,-.171]
keyFrame6409.ViewUp = [.21656,-.368,.904]
keyFrame6409.ParallelScale = 4.962978048511666


keyFrame6410 = CameraKeyFrame()
keyFrame6410.KeyTime = 1.0
keyFrame6410.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6410.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6410.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6410.ParallelScale = 4.962978048511666

cameraAnimationCue1_1.KeyFrames = [keyFrame6400, keyFrame6401, keyFrame6402, keyFrame6403, keyFrame6404, keyFrame6405, keyFrame6406, keyFrame6407,keyFrame6408, keyFrame6409 , keyFrame6410]

execfile('/Users/keritaylor/LCS/ParaviewScripts/sub_movewheel.py')



animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 10
