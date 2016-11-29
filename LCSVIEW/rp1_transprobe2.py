# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

#streamTracer9SeedTypePoint1Track = GetAnimationTrack('Point1', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint2Track = GetAnimationTrack('Point2', index=2, proxy=streamTracer9.SeedType)
#streamTracer9SeedTypePoint1Track.KeyFrames = [keyFrame16980, keyFrame16981]

#Hide(road, V
#Show(ytube, V

stream_1.SeedTypePoint1Track = GetAnimationTrack('Point1', index=2, proxy=stream_1.master.SeedType)


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

keyFrame17000.KeyValues = [0.002]
keyFrame17001.KeyValues = [0.10]
keyFrame17002.KeyValues = [0.002]
keyFrame17003.KeyValues = [0.10]
keyFrame17004.KeyValues = [0.002]
keyFrame17005.KeyValues = [0.10]
keyFrame17006.KeyValues = [0.002]
keyFrame17007.KeyValues = [0.10]
keyFrame17008.KeyValues = [0.002]
keyFrame17009.KeyValues = [0.10]
keyFrame17010.KeyValues = [0.002]

keyFrame17000.KeyTime = [0.]
keyFrame17001.KeyTime = [.5]
keyFrame17002.KeyTime = [1.0]
keyFrame17003.KeyTime = [.30]
keyFrame17004.KeyTime = [.40]
keyFrame17005.KeyTime = [.50]
keyFrame17006.KeyTime = [.60]
keyFrame17007.KeyTime = [.70]
keyFrame17008.KeyTime = [.80]
keyFrame17009.KeyTime = [.90]
keyFrame17010.KeyTime = [1.00]

# create a key frame

stream_1.SeedTypePoint1Track.KeyFrames = [keyFrame17000, keyFrame17001, keyFrame17002]

stream_1.SeedTypePoint2Track = GetAnimationTrack('Point2', index=2, proxy=stream_1.master.SeedType)

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

keyFrame18000.KeyValues = [0.002]
keyFrame18001.KeyValues = [0.10]
keyFrame18002.KeyValues = [0.002]
keyFrame18003.KeyValues = [0.10]
keyFrame18004.KeyValues = [0.002]
keyFrame18005.KeyValues = [0.10]
keyFrame18006.KeyValues = [0.002]
keyFrame18007.KeyValues = [0.10]
keyFrame18008.KeyValues = [0.002]
keyFrame18009.KeyValues = [0.10]
keyFrame18010.KeyValues = [0.002]

keyFrame18000.KeyTime = [0.]
keyFrame18001.KeyTime = [.50]
keyFrame18002.KeyTime = [1.0]
keyFrame18003.KeyTime = [.30]
keyFrame18004.KeyTime = [.40]
keyFrame18005.KeyTime = [.50]
keyFrame18006.KeyTime = [.60]
keyFrame18007.KeyTime = [.70]
keyFrame18008.KeyTime = [.80]
keyFrame18009.KeyTime = [.90]
keyFrame18010.KeyTime = [1.00]


stream_1.SeedTypePoint2Track.KeyFrames = [keyFrame18000, keyFrame18001, keyFrame18002]

#renderView1 = GetActiveViewOrCreate('RenderView')
#renderView1.CameraPosition = [-5.147698595692705, 0.045955065.00282371, 1.085844613286125]
#renderView1.CameraFocalPoint = [2.75, 0.045955065.00282371, 0.4782627841729094]
#renderView1.CameraViewUp =  [0.07670485145646333, 0.0, 0.9970538429608714]
#renderView1.CameraParallelScale = 4.960141706121346







animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
