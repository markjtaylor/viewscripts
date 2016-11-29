# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

#streamTracer9SeedTypePoint1Track = GetAnimationTrack('Point1', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint2Track = GetAnimationTrack('Point2', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint1Track.KeyFrames = [keyFrame16980, keyFrame16981]

#Hide(road, V
#Show(ytube, V

stream_2.SeedTypePoint1Track = GetAnimationTrack('Point1', index=1, proxy=stream_2.master.SeedType)


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

keyFrame17000.KeyValues = [0.01]
keyFrame17001.KeyValues = [1.10]
keyFrame17002.KeyValues = [0.01]
keyFrame17003.KeyValues = [1.10]
keyFrame17004.KeyValues = [0.01]
keyFrame17005.KeyValues = [1.10]
keyFrame17006.KeyValues = [0.01]
keyFrame17007.KeyValues = [1.10]
keyFrame17008.KeyValues = [0.01]
keyFrame17009.KeyValues = [1.10]
keyFrame17010.KeyValues = [0.01]

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

stream_2.SeedTypePoint1Track.KeyFrames = [keyFrame17000, keyFrame17001, keyFrame17002, keyFrame17003, keyFrame17004, keyFrame17005, keyFrame17006, keyFrame17007,keyFrame17008, keyFrame17009 , keyFrame17010]

stream_2.SeedTypePoint2Track = GetAnimationTrack('Point2', index=1, proxy=stream_2.master.SeedType)

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

keyFrame18000.KeyValues = [0.01]
keyFrame18001.KeyValues = [1.10]
keyFrame18002.KeyValues = [0.01]
keyFrame18003.KeyValues = [1.10]
keyFrame18004.KeyValues = [0.01]
keyFrame18005.KeyValues = [1.10]
keyFrame18006.KeyValues = [0.01]
keyFrame18007.KeyValues = [1.10]
keyFrame18008.KeyValues = [0.01]
keyFrame18009.KeyValues = [1.10]
keyFrame18010.KeyValues = [0.01]

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


stream_2.SeedTypePoint2Track.KeyFrames = [keyFrame18000, keyFrame18001, keyFrame18002, keyFrame18003, keyFrame18004, keyFrame18005, keyFrame18006, keyFrame18007,keyFrame18008, keyFrame18009 , keyFrame18010]

#renderView1.CameraPosition = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
#renderView1.CameraFocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
#renderView1.CameraViewUp =  [0.0, 0.0, 1.0]
#renderView1.CameraParallelScale = 4.960141706121346

renderView1 = GetActiveViewOrCreate('RenderView')

cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

keyFrame6400 = CameraKeyFrame()
keyFrame6400.KeyTime = 0.0
keyFrame6400.Position = [-6.198446058783462, 0.0, 0.5746111914049834]
keyFrame6400.FocalPoint = [2.75, 0.0, 0.5746111914049834]
keyFrame6400.ViewUp = [0.0, 0.0, 1.0]
keyFrame6400.ParallelScale = 4.964612270537943



keyFrame6405 = CameraKeyFrame()
keyFrame6405.KeyTime = 0.5
keyFrame6405.Position = [2.75, 10.82761973112799, 0.5746111914049834]
keyFrame6405.FocalPoint = [2.75, 0.0, 0.5746111914049834]
keyFrame6405.ViewUp = [0.0, 0.0, 1.0]
keyFrame6405.ParallelScale = 4.964612270537943



keyFrame6410 = CameraKeyFrame()
keyFrame6410.KeyTime = 1.0
keyFrame6410.Position = [11.68983985462386, -4.267762414427995e-06, 0.18224625844337633]
keyFrame6410.FocalPoint = [2.75, 0.0, 0.5746111914049834]
keyFrame6410.ViewUp = [0.043847270159590286, 8.698946788215357e-05, 0.9990382421771373]
keyFrame6410.ParallelScale = 4.964612270537943






cameraAnimationCue1_1.KeyFrames = [keyFrame6400, keyFrame6405, keyFrame6410]




animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 3
