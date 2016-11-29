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


stream_2.SeedTypePoint2Track.KeyFrames = [keyFrame18000, keyFrame18001, keyFrame18002, keyFrame18003, keyFrame18004, keyFrame18005, keyFrame18006, keyFrame18007,keyFrame18008, keyFrame18009 , keyFrame18010]

#renderView1.CameraPosition = [2.867598309209287, -10.817869609900256, 1.6820229811919147]
#renderView1.CameraFocalPoint = [2.867598309209287, 0.0, 1.6820229811919147]
#renderView1.CameraViewUp =  [0.0, 0.0, 1.0]
#renderView1.CameraParallelScale = 4.960141706121346

renderView1 = GetActiveViewOrCreate('RenderView')

cameraAnimationCue1_1 = GetCameraTrack(view=renderView1)

keyFrame6400 = CameraKeyFrame()
keyFrame6400.KeyTime = 0.0
keyFrame6400.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6400.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6400.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6400.ParallelScale = 4.962978048511666

keyFrame6401 = CameraKeyFrame()
keyFrame6401.KeyTime = 0.1
keyFrame6401.Position = [-3.5632658811556697, 6.233996641216281, 2.289653225350815]
keyFrame6401.FocalPoint = [3.7932425185981913, -1.2923328408157977, 0.08697350099580475]
keyFrame6401.ViewUp =  [0.16141699322140712, -0.1285882326799578, 0.9784731067922129]
keyFrame6401.ParallelScale = 7.218241254981319

keyFrame6402 = CameraKeyFrame()
keyFrame6402.KeyTime = 0.2
keyFrame6402.Position = [-0.9471042939673051, 8.471381394703528, -2.7171826379376394]
keyFrame6402.FocalPoint = [3.155755101225574, -0.8008897909277594, 0.8615295772634196]
keyFrame6402.ViewUp = [-0.11789051337584082, 0.31172806924878715, 0.942829484953883]
keyFrame6402.ParallelScale =  9.218241254981319

keyFrame6403 = CameraKeyFrame()
keyFrame6403.KeyTime = 0.3
keyFrame6403.Position = [3.5867909133492915, 0.6094017745659527, -12.561995491145348]
keyFrame6403.FocalPoint = [3.8610440849453287, -0.1820016238026081, 0.5014919772490217]
keyFrame6403.ViewUp = [-0.16664120260847284, 0.983995838458562, 0.06311021699720054]
keyFrame6403.ParallelScale = 4.96

keyFrame6404 = CameraKeyFrame()
keyFrame6404.KeyTime = 0.4
keyFrame6404.Position = [1.3313924467705942, -0.22554861054282907, -12.494250644044676]
keyFrame6404.FocalPoint =[3.4325227503495683, -0.11171858422867881, 0.4258319079542673]
keyFrame6404.ViewUp = [-0.6909835591723336, 0.7150458400487741, 0.10607152107176264]
keyFrame6404.ParallelScale = 4.96


keyFrame6405 = CameraKeyFrame()
keyFrame6405.KeyTime = 0.5
keyFrame6405.Position = [-1.116062988043704, -0.16590478127383002, -9.56813407762224]
keyFrame6405.FocalPoint = [2.136,-.275,.584]
keyFrame6405.ViewUp = [-.89,-.002,-.444]
keyFrame6405.ParallelScale = 4.9618


keyFrame6406 = CameraKeyFrame()
keyFrame6406.KeyTime = 0.6
keyFrame6406.Position = [0.2629036537732321, -9.565791922515924, 5.00677124582225]
keyFrame6406.FocalPoint = [3.363813020388003, 0.013433543043737103, 1.0493203664398782]
keyFrame6406.ViewUp = [-0.35120960210345, -0.2581296946364247, -0.9000115977792967]
keyFrame6406.ParallelScale = 4.9608



keyFrame6407 = CameraKeyFrame()
keyFrame6407.KeyTime = 0.7
keyFrame6407.Position = [2.0898733862794687, -0.35194464999287645, 13.63973283405161]
keyFrame6407.FocalPoint = [3.2623307816831932, 0.7994494255461743, 0.6529751818601389]
keyFrame6407.ViewUp = [-0.41225668849608993, -0.9034822848373907, -0.11732085822753774]
keyFrame6407.ParallelScale = 4.9618

keyFrame6408 = CameraKeyFrame()
keyFrame6408.KeyTime = 0.8
keyFrame6408.Position = [9.053816984055969, 0.8436302340571394, 6.879464014499243]
keyFrame6408.FocalPoint = [3.3936612149260266, 0.1967142704782566, -0.011333220470064907]
keyFrame6408.ViewUp = [-0.25737882335940954, -0.9193040481123095, 0.2977183373768679]
keyFrame6408.ParallelScale = 4.9618

keyFrame6409 = CameraKeyFrame()
keyFrame6409.KeyTime = 0.9
keyFrame6409.Position = [-2.313485301650426, 10.536208520801907, 6.5247001215479035]
keyFrame6409.FocalPoint = [3.6805080728755977, 0.5424093648704214, 0.5621284586645307]
keyFrame6409.ViewUp = [0.1270342872212435, -0.4509165116517203, 0.8834798183263921]
keyFrame6409.ParallelScale = 4.9618



keyFrame6410 = CameraKeyFrame()
keyFrame6410.KeyTime = 1.0
keyFrame6410.Position = [-5.147698595692705, 0.04595506530282371, 1.085844613286125]
keyFrame6410.FocalPoint = [2.75, 0.04595506530282371, 0.4782627841729094]
keyFrame6410.ViewUp = [0.07670485145646333, 0.0, 0.9970538429608714]
keyFrame6410.ParallelScale = 11.218

cameraAnimationCue1_1.KeyFrames = [keyFrame6400, keyFrame6401, keyFrame6402, keyFrame6403, keyFrame6404, keyFrame6405, keyFrame6406, keyFrame6407,keyFrame6408, keyFrame6409 , keyFrame6410]




animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 10
