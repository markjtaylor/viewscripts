# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5

Show(StreamTracer4, renderView1)
Show(StreamTracer4, renderView1)
Show(StreamTracer4, renderView1)
Show(StreamTracer4, renderView1)
Show(StreamTracer4, renderView1)

Show(balls_1, renderView1)
Show(balls_2, renderView1)
Show(balls_3, renderView1)
Show(balls_4, renderView1)
Show(balls_5, renderView1)

balls_1ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_1)
balls_2ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_2)
balls_3ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_3)
balls_4ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_4)
balls_5ContourValuesTrack = GetAnimationTrack('ContourValues', index=-1, proxy=balls_5)


keyFa0 = CompositeKeyFrame()
keyFa1 = CompositeKeyFrame()
keyFa2 = CompositeKeyFrame()


keyFa1.KeyTime = 0.0
keyFa1.KeyValues = [0.01]
keyFa1.KeyTime = 0.99
keyFa1.KeyValues = [0.9155857776783118]
keyFa2.KeyTime = 1.00
keyFa2.KeyValues = [1.5]

balls_1ContourValuesTrack.KeyFrames = [keyFa0, keyFa1, keyFa2]


keyFb0 = CompositeKeyFrame()
keyFb1 = CompositeKeyFrame()
keyFb2 = CompositeKeyFrame()


keyFb1.KeyTime = 0.0
keyFb1.KeyValues = [0.01]
keyFb1.KeyTime = 0.99
keyFb1.KeyValues = [0.9155857776783118]
keyFb2.KeyTime = 1.0
keyFb2.KeyValues = [1.5]

balls_2ContourValuesTrack.KeyFrames = [keyFb0, keyFb1, keyFb2]


keyFc0 = CompositeKeyFrame()
keyFc1 = CompositeKeyFrame()
keyFc2 = CompositeKeyFrame()


keyFc1.KeyTime = 0.0
keyFc1.KeyValues = [0.01]
keyFc1.KeyTime = 0.99
keyFc1.KeyValues = [0.9155857776783118]
keyFc2.KeyTime = 1.0
keyFc2.KeyValues = [1.5]

balls_3ContourValuesTrack.KeyFrames = [keyFc0, keyFc1, keyFc2]




keyFd0 = CompositeKeyFrame()
keyFd1 = CompositeKeyFrame()
keyFd2 = CompositeKeyFrame()


keyFd1.KeyTime = 0.0
keyFd1.KeyValues = [0.01]
keyFd1.KeyTime = 0.99
keyFd1.KeyValues = [0.9155857776783118]
keyFd2.KeyTime = 1.0   
keyFd2.KeyValues = [1.5]

balls_4ContourValuesTrack.KeyFrames = [keyFd0, keyFd1, keyFd2]



keyFe0 = CompositeKeyFrame()
keyFe1 = CompositeKeyFrame()
keyFe2 = CompositeKeyFrame()


keyFe1.KeyTime = 0.0
keyFe1.KeyValues = [0.01]
keyFe1.KeyTime = 0.99
keyFe1.KeyValues = [0.9155857776783118]
keyFe2.KeyTime = 1.0
keyFe2.KeyValues = [1.5]

balls_5ContourValuesTrack.KeyFrames = [keyFe0, keyFe1, keyFe2]


renderView1.CameraPosition = [-3.0695652890450127, -2.956670692061946, 2.8719589858417587]
renderView1.CameraFocalPoint = [2.4869069333622393, 0.8111934860219328, -0.21388773056320454]
renderView1.CameraViewUp = [0.31461402249359816, 0.2790811690661092, 0.9072660678781564]
renderView1.CameraParallelScale = 4.960141706121346


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 5

#animationScene1.Play()





