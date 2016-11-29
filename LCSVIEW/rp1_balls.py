i=0
ball_delta=1.0/num_balls
for set_a in stream_layer_set.stream_list:
	i=i+1
	Show(set_a.master, set_a.r_view)
	j=0
	for set_b in set_a.ball:
		j=j+1
		set_b.KeyFrame=[]
		Show(set_b.master,set_b.r_view)

		set_b.ContourValuesTrack=GetAnimationTrack('ContourValues', index=-1, proxy=set_b.master)

                key_frame_1 = CompositeKeyFrame()
                key_frame_1.KeyTime = 0.0 
		value_1=(j-1)*ball_delta
                key_frame_1.KeyValues = value_1 
                set_b.KeyFrame.append(key_frame_1)

                key_frame_2 = CompositeKeyFrame()
                key_frame_2.KeyTime = 1.0 
		value_2=(j)*ball_delta
                key_frame_2.KeyValues = value_2 
                set_b.KeyFrame.append(key_frame_2)

		set_b.ContourValuesTrack.KeyFrames = set_b.KeyFrame
		print 'i,j',i,j



renderView1 = GetActiveViewOrCreate('RenderView')

renderView1.CameraPosition = [-2.3153101614821034, -3.227385583658042, 1.1763321443941273]
renderView1.CameraFocalPoint = [2.1425481742297974, 0.8776876655563869, 0.39741223133748194]
renderView1.CameraViewUp = [0.10754311783223755, 0.0713732469455578, 0.9916351836372942]
renderView1.CameraParallelScale = 4.962978048511666

#execfile('/Users/keritaylor/LCS/ParaviewScripts/sub_movewheel.py')

animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 25

#animationScene1.Play()





