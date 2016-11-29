Hide(rwheelnuts.master,rwheelnuts.r_view)

#4 looks good for num_wheelsets
num_spokes_channels=4
num_repeats=4
#15 looks good for num_wheelsets
num_wheelsets=15
spoke_offset=-360.0/(num_spokes_channels * num_wheelsets)
time=1.0
time_loop_length=time/num_repeats
time_delta=time_loop_length/num_wheelsets


#make the sets for rotation

front_spoke_set=make_rotate_set(fwheels,0.930,-.872779,.317120,'y',spoke_offset,num_wheelsets)
back_spoke_set=make_rotate_set(rwheels,3.45,-.871896,.325954,'y',spoke_offset,num_wheelsets)

#front_tyre_set=make_rotate_set(ftyres,0.930,-.872779,.317120,'y',spoke_offset,num_wheelsets)
#back_tyre_set=make_rotate_set(rtyres,3.45,-.871896,.325954,'y',spoke_offset,num_wheelsets)
Show(ftyres.master,ftyres.r_view)
Show(rtyres.master,rtyres.r_view)

front_wheelnuts_set=make_rotate_set(fwheelnuts,0.930,-.872779,.317120,'y',spoke_offset,num_wheelsets)
back_wheelnuts_set=make_rotate_set(rwheelnuts,3.45,-.871896,.325954,'y',spoke_offset,num_wheelsets)


# first hide everything ahead of animation

for set in front_spoke_set.rotlist:
	Hide(set.master,set.r_view)

for set in back_spoke_set.rotlist:
	Hide(set.master,set.r_view)

#for set in front_tyre_set.rotlist:
#	Hide(set.master,set.r_view)

#for set in back_tyre_set.rotlist:
#	Hide(set.master,set.r_view)

for set in front_wheelnuts_set.rotlist:
	Hide(set.master,set.r_view)

for set in back_wheelnuts_set.rotlist:
	Hide(set.master,set.r_view)

spin_list=[front_spoke_set,back_spoke_set,front_wheelnuts_set,back_wheelnuts_set]
#spin_list=[front_spoke_set,back_spoke_set,front_tyre_set,back_tyre_set,front_wheelnuts_set,back_wheelnuts_set]
#spin_list=[front_spoke_set]

for spin_set in spin_list:
	j=0

	for set in spin_set.rotlist:
		set.VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=set.master)
		set.keyFrame=[]
		time=0.0

		for k in range(0,num_repeats):
			for i in range(0,num_wheelsets):
				key_frame = CompositeKeyFrame()
				key_frame.Interpolation ='Boolean'
				key_frame.KeyTime = time 
				if i == j:
					visibility=1.0
				else:
					visibility=0.0
				key_frame.KeyValues = [visibility]
				set.keyFrame.append(key_frame)
				time=time+time_delta

		set.VisibilityTrack.KeyFrames=set.keyFrame
		j=j+1


animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100

#view=GetActiveView()
#view.ViewSize=[3000,2000]

#view.ResetCamera()
#view.CameraPosition = [-0.2535251578621551, -3.968489879804233, 1.3730632428360967]
#view.CameraFocalPoint = [2.7499999999999996, 8.970735985278077e-17, 0.5358429932966828]
#view.CameraViewUp = [0.02788014222304762, 0.18609728019084748, 0.9821356830780521]
#view.CameraParallelScale = 4.96040266244862

#WriteAnimation('test.avi',Magnification=1, FrameRate=15.0, Compression=True)
