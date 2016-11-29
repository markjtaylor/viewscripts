# bigwake smallwake
# xtube ytube
# car_scalar, car, ground
# balls_1, balls_2, balls_3, balls_4, balls_5
# wf_1, wf_2, wf_3, wf_4, wf_5
# wr_1, wr_2, wr_3, wr_4, wr_5

Show(wf_1, renderView1)
Hide(wf_2, renderView1)
Hide(wf_3, renderView1)
Hide(wf_4, renderView1)
Hide(wf_5, renderView1)

Show(wr_1, renderView1)
Hide(wr_2, renderView1)
Hide(wr_3, renderView1)
Hide(wr_4, renderView1)
Hide(wr_5, renderView1)


wf_1VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wf_1)

# create a key frame
keyFramewf1000 = CompositeKeyFrame()
keyFramewf1000.Interpolation = 'Boolean'
keyFramewf1000.KeyTime = 0.0
keyFramewf1000.KeyValues = [1]

keyFramewf1001 = CompositeKeyFrame()
keyFramewf1001.Interpolation = 'Boolean'
keyFramewf1001.KeyTime = 0.02
keyFramewf1001.KeyValues = [0]

keyFramewf1002 = CompositeKeyFrame()
keyFramewf1002.Interpolation = 'Boolean'
keyFramewf1002.KeyTime = 0.1
keyFramewf1002.KeyValues = [1]

keyFramewf1003 = CompositeKeyFrame()
keyFramewf1003.Interpolation = 'Boolean'
keyFramewf1003.KeyTime = 0.12
keyFramewf1003.KeyValues = [0]

keyFramewf1004 = CompositeKeyFrame()
keyFramewf1004.Interpolation = 'Boolean'
keyFramewf1004.KeyTime = 0.2
keyFramewf1004.KeyValues = [1]


keyFramewf1005 = CompositeKeyFrame()
keyFramewf1005.Interpolation = 'Boolean'
keyFramewf1005.KeyTime = 0.22
keyFramewf1005.KeyValues = [0]


keyFramewf1006 = CompositeKeyFrame()
keyFramewf1006.Interpolation = 'Boolean'
keyFramewf1006.KeyTime = 0.3
keyFramewf1006.KeyValues = [1]

keyFramewf1007 = CompositeKeyFrame()
keyFramewf1007.Interpolation = 'Boolean'
keyFramewf1007.KeyTime = 0.32
keyFramewf1007.KeyValues = [0]

keyFramewf1008 = CompositeKeyFrame()
keyFramewf1008.Interpolation = 'Boolean'
keyFramewf1008.KeyTime = 0.4
keyFramewf1008.KeyValues = [1]

keyFramewf1009 = CompositeKeyFrame()
keyFramewf1009.Interpolation = 'Boolean'
keyFramewf1009.KeyTime = 0.42
keyFramewf1009.KeyValues = [0]

keyFramewf1010 = CompositeKeyFrame()
keyFramewf1010.Interpolation = 'Boolean'
keyFramewf1010.KeyTime = 0.5
keyFramewf1010.KeyValues = [1]

keyFramewf1011 = CompositeKeyFrame()
keyFramewf1011.Interpolation = 'Boolean'
keyFramewf1011.KeyTime = 0.52
keyFramewf1011.KeyValues = [0]

keyFramewf1012 = CompositeKeyFrame()
keyFramewf1012.Interpolation = 'Boolean'
keyFramewf1012.KeyTime = 0.6
keyFramewf1012.KeyValues = [1]

keyFramewf1013 = CompositeKeyFrame()
keyFramewf1013.Interpolation = 'Boolean'
keyFramewf1013.KeyTime = 0.62
keyFramewf1013.KeyValues = [0]

keyFramewf1014 = CompositeKeyFrame()
keyFramewf1014.Interpolation = 'Boolean'
keyFramewf1014.KeyTime = 0.7
keyFramewf1014.KeyValues = [1]

keyFramewf1015 = CompositeKeyFrame()
keyFramewf1015.Interpolation = 'Boolean'
keyFramewf1015.KeyTime = 0.72
keyFramewf1015.KeyValues = [0]

keyFramewf1016 = CompositeKeyFrame()
keyFramewf1016.Interpolation = 'Boolean'
keyFramewf1016.KeyTime = 0.8
keyFramewf1016.KeyValues = [1]

keyFramewf1017 = CompositeKeyFrame()
keyFramewf1017.Interpolation = 'Boolean'
keyFramewf1017.KeyTime = 0.82
keyFramewf1017.KeyValues = [0]

keyFramewf1018 = CompositeKeyFrame()
keyFramewf1018.Interpolation = 'Boolean'
keyFramewf1018.KeyTime = 0.9
keyFramewf1018.KeyValues = [1]

keyFramewf1019 = CompositeKeyFrame()
keyFramewf1019.Interpolation = 'Boolean'
keyFramewf1019.KeyTime = 0.92
keyFramewf1019.KeyValues = [0]

# create a key frame
keyFramewf1020 = CompositeKeyFrame()
keyFramewf1020.Interpolation = 'Boolean'
keyFramewf1020.KeyTime = 1.0
keyFramewf1020.KeyValues = [1]


wf_1VisibilityTrack.KeyFrames = [keyFramewf1000, keyFramewf1001, keyFramewf1002, keyFramewf1003, keyFramewf1004, keyFramewf1005, keyFramewf1006, keyFramewf1007, keyFramewf1008, keyFramewf1009, keyFramewf1010 , keyFramewf1011, keyFramewf1012, keyFramewf1013, keyFramewf1014, keyFramewf1015, keyFramewf1016, keyFramewf1017, keyFramewf1018, keyFramewf1019, keyFramewf1020 ]


wf_2VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wf_2)

# create a key frame
keyFramewf1999 = CompositeKeyFrame()
keyFramewf1999.Interpolation = 'Boolean'
keyFramewf1999.KeyTime = 0.00
keyFramewf1999.KeyValues = [0]

keyFramewf2000 = CompositeKeyFrame()
keyFramewf2000.Interpolation = 'Boolean'
keyFramewf2000.KeyTime = 0.02
keyFramewf2000.KeyValues = [1]

keyFramewf2001 = CompositeKeyFrame()
keyFramewf2001.Interpolation = 'Boolean'
keyFramewf2001.KeyTime = 0.04
keyFramewf2001.KeyValues = [0]

keyFramewf2002 = CompositeKeyFrame()
keyFramewf2002.Interpolation = 'Boolean'
keyFramewf2002.KeyTime = 0.12
keyFramewf2002.KeyValues = [1]

keyFramewf2003 = CompositeKeyFrame()
keyFramewf2003.Interpolation = 'Boolean'
keyFramewf2003.KeyTime = 0.14
keyFramewf2003.KeyValues = [0]

keyFramewf2004 = CompositeKeyFrame()
keyFramewf2004.Interpolation = 'Boolean'
keyFramewf2004.KeyTime = 0.22
keyFramewf2004.KeyValues = [1]


keyFramewf2005 = CompositeKeyFrame()
keyFramewf2005.Interpolation = 'Boolean'
keyFramewf2005.KeyTime = 0.24
keyFramewf2005.KeyValues = [0]


keyFramewf2006 = CompositeKeyFrame()
keyFramewf2006.Interpolation = 'Boolean'
keyFramewf2006.KeyTime = 0.32
keyFramewf2006.KeyValues = [1]

keyFramewf2007 = CompositeKeyFrame()
keyFramewf2007.Interpolation = 'Boolean'
keyFramewf2007.KeyTime = 0.34
keyFramewf2007.KeyValues = [0]

keyFramewf2008 = CompositeKeyFrame()
keyFramewf2008.Interpolation = 'Boolean'
keyFramewf2008.KeyTime = 0.42
keyFramewf2008.KeyValues = [1]

keyFramewf2009 = CompositeKeyFrame()
keyFramewf2009.Interpolation = 'Boolean'
keyFramewf2009.KeyTime = 0.44
keyFramewf2009.KeyValues = [0]

keyFramewf2010 = CompositeKeyFrame()
keyFramewf2010.Interpolation = 'Boolean'
keyFramewf2010.KeyTime = 0.52
keyFramewf2010.KeyValues = [1]

keyFramewf2011 = CompositeKeyFrame()
keyFramewf2011.Interpolation = 'Boolean'
keyFramewf2011.KeyTime = 0.54
keyFramewf2011.KeyValues = [0]

keyFramewf2012 = CompositeKeyFrame()
keyFramewf2012.Interpolation = 'Boolean'
keyFramewf2012.KeyTime = 0.62
keyFramewf2012.KeyValues = [1]

keyFramewf2013 = CompositeKeyFrame()
keyFramewf2013.Interpolation = 'Boolean'
keyFramewf2013.KeyTime = 0.64
keyFramewf2013.KeyValues = [0]

keyFramewf2014 = CompositeKeyFrame()
keyFramewf2014.Interpolation = 'Boolean'
keyFramewf2014.KeyTime = 0.72
keyFramewf2014.KeyValues = [1]

keyFramewf2015 = CompositeKeyFrame()
keyFramewf2015.Interpolation = 'Boolean'
keyFramewf2015.KeyTime = 0.74
keyFramewf2015.KeyValues = [0]

keyFramewf2016 = CompositeKeyFrame()
keyFramewf2016.Interpolation = 'Boolean'
keyFramewf2016.KeyTime = 0.82
keyFramewf2016.KeyValues = [1]

keyFramewf2017 = CompositeKeyFrame()
keyFramewf2017.Interpolation = 'Boolean'
keyFramewf2017.KeyTime = 0.84
keyFramewf2017.KeyValues = [0]

keyFramewf2018 = CompositeKeyFrame()
keyFramewf2018.Interpolation = 'Boolean'
keyFramewf2018.KeyTime = 0.92
keyFramewf2018.KeyValues = [1]

keyFramewf2019 = CompositeKeyFrame()
keyFramewf2019.Interpolation = 'Boolean'
keyFramewf2019.KeyTime = 0.94
keyFramewf2019.KeyValues = [0]

keyFramewf2020 = CompositeKeyFrame()
keyFramewf2020.Interpolation = 'Boolean'
keyFramewf2020.KeyTime = 1.0
keyFramewf2020.KeyValues = [0]


wf_2VisibilityTrack.KeyFrames = [keyFramewf1999, keyFramewf2000, keyFramewf2001, keyFramewf2002, keyFramewf2003, keyFramewf2004, keyFramewf2005, keyFramewf2006, keyFramewf2007, keyFramewf2008, keyFramewf2009, keyFramewf2010 , keyFramewf2011, keyFramewf2012, keyFramewf2013, keyFramewf2014, keyFramewf2015, keyFramewf2016, keyFramewf2017, keyFramewf2018, keyFramewf2019, keyFramewf2020 ]

wf_3VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wf_3)

# create a key frame
keyFramewf2999 = CompositeKeyFrame()
keyFramewf2999.Interpolation = 'Boolean'
keyFramewf2999.KeyTime = 0.00
keyFramewf2999.KeyValues = [0]

keyFramewf3000 = CompositeKeyFrame()
keyFramewf3000.Interpolation = 'Boolean'
keyFramewf3000.KeyTime = 0.04
keyFramewf3000.KeyValues = [1]

keyFramewf3001 = CompositeKeyFrame()
keyFramewf3001.Interpolation = 'Boolean'
keyFramewf3001.KeyTime = 0.06
keyFramewf3001.KeyValues = [0]

keyFramewf3002 = CompositeKeyFrame()
keyFramewf3002.Interpolation = 'Boolean'
keyFramewf3002.KeyTime = 0.14
keyFramewf3002.KeyValues = [1]

keyFramewf3003 = CompositeKeyFrame()
keyFramewf3003.Interpolation = 'Boolean'
keyFramewf3003.KeyTime = 0.16
keyFramewf3003.KeyValues = [0]

keyFramewf3004 = CompositeKeyFrame()
keyFramewf3004.Interpolation = 'Boolean'
keyFramewf3004.KeyTime = 0.24
keyFramewf3004.KeyValues = [1]


keyFramewf3005 = CompositeKeyFrame()
keyFramewf3005.Interpolation = 'Boolean'
keyFramewf3005.KeyTime = 0.26
keyFramewf3005.KeyValues = [0]


keyFramewf3006 = CompositeKeyFrame()
keyFramewf3006.Interpolation = 'Boolean'
keyFramewf3006.KeyTime = 0.34
keyFramewf3006.KeyValues = [1]

keyFramewf3007 = CompositeKeyFrame()
keyFramewf3007.Interpolation = 'Boolean'
keyFramewf3007.KeyTime = 0.36
keyFramewf3007.KeyValues = [0]

keyFramewf3008 = CompositeKeyFrame()
keyFramewf3008.Interpolation = 'Boolean'
keyFramewf3008.KeyTime = 0.44
keyFramewf3008.KeyValues = [1]

keyFramewf3009 = CompositeKeyFrame()
keyFramewf3009.Interpolation = 'Boolean'
keyFramewf3009.KeyTime = 0.46
keyFramewf3009.KeyValues = [0]

keyFramewf3010 = CompositeKeyFrame()
keyFramewf3010.Interpolation = 'Boolean'
keyFramewf3010.KeyTime = 0.54
keyFramewf3010.KeyValues = [1]

keyFramewf3011 = CompositeKeyFrame()
keyFramewf3011.Interpolation = 'Boolean'
keyFramewf3011.KeyTime = 0.56
keyFramewf3011.KeyValues = [0]

keyFramewf3012 = CompositeKeyFrame()
keyFramewf3012.Interpolation = 'Boolean'
keyFramewf3012.KeyTime = 0.64
keyFramewf3012.KeyValues = [1]

keyFramewf3013 = CompositeKeyFrame()
keyFramewf3013.Interpolation = 'Boolean'
keyFramewf3013.KeyTime = 0.66
keyFramewf3013.KeyValues = [0]

keyFramewf3014 = CompositeKeyFrame()
keyFramewf3014.Interpolation = 'Boolean'
keyFramewf3014.KeyTime = 0.74
keyFramewf3014.KeyValues = [1]

keyFramewf3015 = CompositeKeyFrame()
keyFramewf3015.Interpolation = 'Boolean'
keyFramewf3015.KeyTime = 0.76
keyFramewf3015.KeyValues = [0]

keyFramewf3016 = CompositeKeyFrame()
keyFramewf3016.Interpolation = 'Boolean'
keyFramewf3016.KeyTime = 0.84
keyFramewf3016.KeyValues = [1]

keyFramewf3017 = CompositeKeyFrame()
keyFramewf3017.Interpolation = 'Boolean'
keyFramewf3017.KeyTime = 0.86
keyFramewf3017.KeyValues = [0]

keyFramewf3018 = CompositeKeyFrame()
keyFramewf3018.Interpolation = 'Boolean'
keyFramewf3018.KeyTime = 0.94
keyFramewf3018.KeyValues = [1]

keyFramewf3019 = CompositeKeyFrame()
keyFramewf3019.Interpolation = 'Boolean'
keyFramewf3019.KeyTime = 0.96
keyFramewf3019.KeyValues = [0]

keyFramewf3020 = CompositeKeyFrame()
keyFramewf3020.Interpolation = 'Boolean'
keyFramewf3020.KeyTime = 1.0
keyFramewf3020.KeyValues = [0]


wf_3VisibilityTrack.KeyFrames = [keyFramewf2999, keyFramewf3000, keyFramewf3001, keyFramewf3002, keyFramewf3003, keyFramewf3004, keyFramewf3005, keyFramewf3006, keyFramewf3007, keyFramewf3008, keyFramewf3009, keyFramewf3010 , keyFramewf3011, keyFramewf3012, keyFramewf3013, keyFramewf3014, keyFramewf3015, keyFramewf3016, keyFramewf3017, keyFramewf3018, keyFramewf3019, keyFramewf3020 ]

wf_4VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wf_4)

# create a key frame
keyFramewf3999 = CompositeKeyFrame()
keyFramewf3999.Interpolation = 'Boolean'
keyFramewf3999.KeyTime = 0.00
keyFramewf3999.KeyValues = [0]

keyFramewf4000 = CompositeKeyFrame()
keyFramewf4000.Interpolation = 'Boolean'
keyFramewf4000.KeyTime = 0.06
keyFramewf4000.KeyValues = [1]

keyFramewf4001 = CompositeKeyFrame()
keyFramewf4001.Interpolation = 'Boolean'
keyFramewf4001.KeyTime = 0.08
keyFramewf4001.KeyValues = [0]

keyFramewf4002 = CompositeKeyFrame()
keyFramewf4002.Interpolation = 'Boolean'
keyFramewf4002.KeyTime = 0.16
keyFramewf4002.KeyValues = [1]

keyFramewf4003 = CompositeKeyFrame()
keyFramewf4003.Interpolation = 'Boolean'
keyFramewf4003.KeyTime = 0.18
keyFramewf4003.KeyValues = [0]

keyFramewf4004 = CompositeKeyFrame()
keyFramewf4004.Interpolation = 'Boolean'
keyFramewf4004.KeyTime = 0.26
keyFramewf4004.KeyValues = [1]


keyFramewf4005 = CompositeKeyFrame()
keyFramewf4005.Interpolation = 'Boolean'
keyFramewf4005.KeyTime = 0.28
keyFramewf4005.KeyValues = [0]


keyFramewf4006 = CompositeKeyFrame()
keyFramewf4006.Interpolation = 'Boolean'
keyFramewf4006.KeyTime = 0.36
keyFramewf4006.KeyValues = [1]

keyFramewf4007 = CompositeKeyFrame()
keyFramewf4007.Interpolation = 'Boolean'
keyFramewf4007.KeyTime = 0.38
keyFramewf4007.KeyValues = [0]

keyFramewf4008 = CompositeKeyFrame()
keyFramewf4008.Interpolation = 'Boolean'
keyFramewf4008.KeyTime = 0.46
keyFramewf4008.KeyValues = [1]

keyFramewf4009 = CompositeKeyFrame()
keyFramewf4009.Interpolation = 'Boolean'
keyFramewf4009.KeyTime = 0.48
keyFramewf4009.KeyValues = [0]

keyFramewf4010 = CompositeKeyFrame()
keyFramewf4010.Interpolation = 'Boolean'
keyFramewf4010.KeyTime = 0.56
keyFramewf4010.KeyValues = [1]

keyFramewf4011 = CompositeKeyFrame()
keyFramewf4011.Interpolation = 'Boolean'
keyFramewf4011.KeyTime = 0.58
keyFramewf4011.KeyValues = [0]

keyFramewf4012 = CompositeKeyFrame()
keyFramewf4012.Interpolation = 'Boolean'
keyFramewf4012.KeyTime = 0.66
keyFramewf4012.KeyValues = [1]

keyFramewf4013 = CompositeKeyFrame()
keyFramewf4013.Interpolation = 'Boolean'
keyFramewf4013.KeyTime = 0.68
keyFramewf4013.KeyValues = [0]

keyFramewf4014 = CompositeKeyFrame()
keyFramewf4014.Interpolation = 'Boolean'
keyFramewf4014.KeyTime = 0.76
keyFramewf4014.KeyValues = [1]

keyFramewf4015 = CompositeKeyFrame()
keyFramewf4015.Interpolation = 'Boolean'
keyFramewf4015.KeyTime = 0.78
keyFramewf4015.KeyValues = [0]

keyFramewf4016 = CompositeKeyFrame()
keyFramewf4016.Interpolation = 'Boolean'
keyFramewf4016.KeyTime = 0.86
keyFramewf4016.KeyValues = [1]

keyFramewf4017 = CompositeKeyFrame()
keyFramewf4017.Interpolation = 'Boolean'
keyFramewf4017.KeyTime = 0.88
keyFramewf4017.KeyValues = [0]

keyFramewf4018 = CompositeKeyFrame()
keyFramewf4018.Interpolation = 'Boolean'
keyFramewf4018.KeyTime = 0.96
keyFramewf4018.KeyValues = [1]

keyFramewf4019 = CompositeKeyFrame()
keyFramewf4019.Interpolation = 'Boolean'
keyFramewf4019.KeyTime = 0.98
keyFramewf4019.KeyValues = [0]

keyFramewf4020 = CompositeKeyFrame()
keyFramewf4020.Interpolation = 'Boolean'
keyFramewf4020.KeyTime = 1.0
keyFramewf4020.KeyValues = [0]


wf_4VisibilityTrack.KeyFrames = [keyFramewf3999, keyFramewf4000, keyFramewf4001, keyFramewf4002, keyFramewf4003, keyFramewf4004, keyFramewf4005, keyFramewf4006, keyFramewf4007, keyFramewf4008, keyFramewf4009, keyFramewf4010 , keyFramewf4011, keyFramewf4012, keyFramewf4013, keyFramewf4014, keyFramewf4015, keyFramewf4016, keyFramewf4017, keyFramewf4018, keyFramewf4019, keyFramewf4020 ]

wf_5VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wf_5)

# create a key frame
keyFramewf4999 = CompositeKeyFrame()
keyFramewf4999.Interpolation = 'Boolean'
keyFramewf4999.KeyTime = 0.00
keyFramewf4999.KeyValues = [0]

keyFramewf5000 = CompositeKeyFrame()
keyFramewf5000.Interpolation = 'Boolean'
keyFramewf5000.KeyTime = 0.08
keyFramewf5000.KeyValues = [1]

keyFramewf5001 = CompositeKeyFrame()
keyFramewf5001.Interpolation = 'Boolean'
keyFramewf5001.KeyTime = 0.10
keyFramewf5001.KeyValues = [0]

keyFramewf5002 = CompositeKeyFrame()
keyFramewf5002.Interpolation = 'Boolean'
keyFramewf5002.KeyTime = 0.18
keyFramewf5002.KeyValues = [1]

keyFramewf5003 = CompositeKeyFrame()
keyFramewf5003.Interpolation = 'Boolean'
keyFramewf5003.KeyTime = 0.20
keyFramewf5003.KeyValues = [0]

keyFramewf5004 = CompositeKeyFrame()
keyFramewf5004.Interpolation = 'Boolean'
keyFramewf5004.KeyTime = 0.28
keyFramewf5004.KeyValues = [1]


keyFramewf5005 = CompositeKeyFrame()
keyFramewf5005.Interpolation = 'Boolean'
keyFramewf5005.KeyTime = 0.30
keyFramewf5005.KeyValues = [0]


keyFramewf5006 = CompositeKeyFrame()
keyFramewf5006.Interpolation = 'Boolean'
keyFramewf5006.KeyTime = 0.38
keyFramewf5006.KeyValues = [1]

keyFramewf5007 = CompositeKeyFrame()
keyFramewf5007.Interpolation = 'Boolean'
keyFramewf5007.KeyTime = 0.40
keyFramewf5007.KeyValues = [0]

keyFramewf5008 = CompositeKeyFrame()
keyFramewf5008.Interpolation = 'Boolean'
keyFramewf5008.KeyTime = 0.48
keyFramewf5008.KeyValues = [1]

keyFramewf5009 = CompositeKeyFrame()
keyFramewf5009.Interpolation = 'Boolean'
keyFramewf5009.KeyTime = 0.50
keyFramewf5009.KeyValues = [0]

keyFramewf5010 = CompositeKeyFrame()
keyFramewf5010.Interpolation = 'Boolean'
keyFramewf5010.KeyTime = 0.58
keyFramewf5010.KeyValues = [1]

keyFramewf5011 = CompositeKeyFrame()
keyFramewf5011.Interpolation = 'Boolean'
keyFramewf5011.KeyTime = 0.60
keyFramewf5011.KeyValues = [0]

keyFramewf5012 = CompositeKeyFrame()
keyFramewf5012.Interpolation = 'Boolean'
keyFramewf5012.KeyTime = 0.68
keyFramewf5012.KeyValues = [1]

keyFramewf5013 = CompositeKeyFrame()
keyFramewf5013.Interpolation = 'Boolean'
keyFramewf5013.KeyTime = 0.70
keyFramewf5013.KeyValues = [0]

keyFramewf5014 = CompositeKeyFrame()
keyFramewf5014.Interpolation = 'Boolean'
keyFramewf5014.KeyTime = 0.78
keyFramewf5014.KeyValues = [1]

keyFramewf5015 = CompositeKeyFrame()
keyFramewf5015.Interpolation = 'Boolean'
keyFramewf5015.KeyTime = 0.80
keyFramewf5015.KeyValues = [0]

keyFramewf5016 = CompositeKeyFrame()
keyFramewf5016.Interpolation = 'Boolean'
keyFramewf5016.KeyTime = 0.88
keyFramewf5016.KeyValues = [1]

keyFramewf5017 = CompositeKeyFrame()
keyFramewf5017.Interpolation = 'Boolean'
keyFramewf5017.KeyTime = 0.90
keyFramewf5017.KeyValues = [0]

keyFramewf5018 = CompositeKeyFrame()
keyFramewf5018.Interpolation = 'Boolean'
keyFramewf5018.KeyTime = 0.98
keyFramewf5018.KeyValues = [1]

keyFramewf5019 = CompositeKeyFrame()
keyFramewf5019.Interpolation = 'Boolean'
keyFramewf5019.KeyTime = 1.0
keyFramewf5019.KeyValues = [0]


wf_5VisibilityTrack.KeyFrames = [keyFramewf4999, keyFramewf5000, keyFramewf5001, keyFramewf5002, keyFramewf5003, keyFramewf5004, keyFramewf5005, keyFramewf5006, keyFramewf5007, keyFramewf5008, keyFramewf5009, keyFramewf5010 , keyFramewf5011, keyFramewf5012, keyFramewf5013, keyFramewf5014, keyFramewf5015, keyFramewf5016, keyFramewf5017, keyFramewf5018, keyFramewf5019 ]

wr_1VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wr_1)

# create a key frame
keyFramewr1000 = CompositeKeyFrame()
keyFramewr1000.Interpolation = 'Boolean'
keyFramewr1000.KeyTime = 0.0
keyFramewr1000.KeyValues = [1]

keyFramewr1001 = CompositeKeyFrame()
keyFramewr1001.Interpolation = 'Boolean'
keyFramewr1001.KeyTime = 0.02
keyFramewr1001.KeyValues = [0]

keyFramewr1002 = CompositeKeyFrame()
keyFramewr1002.Interpolation = 'Boolean'
keyFramewr1002.KeyTime = 0.1
keyFramewr1002.KeyValues = [1]

keyFramewr1003 = CompositeKeyFrame()
keyFramewr1003.Interpolation = 'Boolean'
keyFramewr1003.KeyTime = 0.12
keyFramewr1003.KeyValues = [0]

keyFramewr1004 = CompositeKeyFrame()
keyFramewr1004.Interpolation = 'Boolean'
keyFramewr1004.KeyTime = 0.2
keyFramewr1004.KeyValues = [1]


keyFramewr1005 = CompositeKeyFrame()
keyFramewr1005.Interpolation = 'Boolean'
keyFramewr1005.KeyTime = 0.22
keyFramewr1005.KeyValues = [0]


keyFramewr1006 = CompositeKeyFrame()
keyFramewr1006.Interpolation = 'Boolean'
keyFramewr1006.KeyTime = 0.3
keyFramewr1006.KeyValues = [1]

keyFramewr1007 = CompositeKeyFrame()
keyFramewr1007.Interpolation = 'Boolean'
keyFramewr1007.KeyTime = 0.32
keyFramewr1007.KeyValues = [0]

keyFramewr1008 = CompositeKeyFrame()
keyFramewr1008.Interpolation = 'Boolean'
keyFramewr1008.KeyTime = 0.4
keyFramewr1008.KeyValues = [1]

keyFramewr1009 = CompositeKeyFrame()
keyFramewr1009.Interpolation = 'Boolean'
keyFramewr1009.KeyTime = 0.42
keyFramewr1009.KeyValues = [0]

keyFramewr1010 = CompositeKeyFrame()
keyFramewr1010.Interpolation = 'Boolean'
keyFramewr1010.KeyTime = 0.5
keyFramewr1010.KeyValues = [1]

keyFramewr1011 = CompositeKeyFrame()
keyFramewr1011.Interpolation = 'Boolean'
keyFramewr1011.KeyTime = 0.52
keyFramewr1011.KeyValues = [0]

keyFramewr1012 = CompositeKeyFrame()
keyFramewr1012.Interpolation = 'Boolean'
keyFramewr1012.KeyTime = 0.6
keyFramewr1012.KeyValues = [1]

keyFramewr1013 = CompositeKeyFrame()
keyFramewr1013.Interpolation = 'Boolean'
keyFramewr1013.KeyTime = 0.62
keyFramewr1013.KeyValues = [0]

keyFramewr1014 = CompositeKeyFrame()
keyFramewr1014.Interpolation = 'Boolean'
keyFramewr1014.KeyTime = 0.7
keyFramewr1014.KeyValues = [1]

keyFramewr1015 = CompositeKeyFrame()
keyFramewr1015.Interpolation = 'Boolean'
keyFramewr1015.KeyTime = 0.72
keyFramewr1015.KeyValues = [0]

keyFramewr1016 = CompositeKeyFrame()
keyFramewr1016.Interpolation = 'Boolean'
keyFramewr1016.KeyTime = 0.8
keyFramewr1016.KeyValues = [1]

keyFramewr1017 = CompositeKeyFrame()
keyFramewr1017.Interpolation = 'Boolean'
keyFramewr1017.KeyTime = 0.82
keyFramewr1017.KeyValues = [0]

keyFramewr1018 = CompositeKeyFrame()
keyFramewr1018.Interpolation = 'Boolean'
keyFramewr1018.KeyTime = 0.9
keyFramewr1018.KeyValues = [1]

keyFramewr1019 = CompositeKeyFrame()
keyFramewr1019.Interpolation = 'Boolean'
keyFramewr1019.KeyTime = 0.92
keyFramewr1019.KeyValues = [0]

# create a key frame
keyFramewr1020 = CompositeKeyFrame()
keyFramewr1020.Interpolation = 'Boolean'
keyFramewr1020.KeyTime = 1.0
keyFramewr1020.KeyValues = [1]


wr_1VisibilityTrack.KeyFrames = [keyFramewr1000, keyFramewr1001, keyFramewr1002, keyFramewr1003, keyFramewr1004, keyFramewr1005, keyFramewr1006, keyFramewr1007, keyFramewr1008, keyFramewr1009, keyFramewr1010 , keyFramewr1011, keyFramewr1012, keyFramewr1013, keyFramewr1014, keyFramewr1015, keyFramewr1016, keyFramewr1017, keyFramewr1018, keyFramewr1019, keyFramewr1020 ]


wr_2VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wr_2)

# create a key frame
keyFramewr1999 = CompositeKeyFrame()
keyFramewr1999.Interpolation = 'Boolean'
keyFramewr1999.KeyTime = 0.00
keyFramewr1999.KeyValues = [0]

keyFramewr2000 = CompositeKeyFrame()
keyFramewr2000.Interpolation = 'Boolean'
keyFramewr2000.KeyTime = 0.02
keyFramewr2000.KeyValues = [1]

keyFramewr2001 = CompositeKeyFrame()
keyFramewr2001.Interpolation = 'Boolean'
keyFramewr2001.KeyTime = 0.04
keyFramewr2001.KeyValues = [0]

keyFramewr2002 = CompositeKeyFrame()
keyFramewr2002.Interpolation = 'Boolean'
keyFramewr2002.KeyTime = 0.12
keyFramewr2002.KeyValues = [1]

keyFramewr2003 = CompositeKeyFrame()
keyFramewr2003.Interpolation = 'Boolean'
keyFramewr2003.KeyTime = 0.14
keyFramewr2003.KeyValues = [0]

keyFramewr2004 = CompositeKeyFrame()
keyFramewr2004.Interpolation = 'Boolean'
keyFramewr2004.KeyTime = 0.22
keyFramewr2004.KeyValues = [1]


keyFramewr2005 = CompositeKeyFrame()
keyFramewr2005.Interpolation = 'Boolean'
keyFramewr2005.KeyTime = 0.24
keyFramewr2005.KeyValues = [0]


keyFramewr2006 = CompositeKeyFrame()
keyFramewr2006.Interpolation = 'Boolean'
keyFramewr2006.KeyTime = 0.32
keyFramewr2006.KeyValues = [1]

keyFramewr2007 = CompositeKeyFrame()
keyFramewr2007.Interpolation = 'Boolean'
keyFramewr2007.KeyTime = 0.34
keyFramewr2007.KeyValues = [0]

keyFramewr2008 = CompositeKeyFrame()
keyFramewr2008.Interpolation = 'Boolean'
keyFramewr2008.KeyTime = 0.42
keyFramewr2008.KeyValues = [1]

keyFramewr2009 = CompositeKeyFrame()
keyFramewr2009.Interpolation = 'Boolean'
keyFramewr2009.KeyTime = 0.44
keyFramewr2009.KeyValues = [0]

keyFramewr2010 = CompositeKeyFrame()
keyFramewr2010.Interpolation = 'Boolean'
keyFramewr2010.KeyTime = 0.52
keyFramewr2010.KeyValues = [1]

keyFramewr2011 = CompositeKeyFrame()
keyFramewr2011.Interpolation = 'Boolean'
keyFramewr2011.KeyTime = 0.54
keyFramewr2011.KeyValues = [0]

keyFramewr2012 = CompositeKeyFrame()
keyFramewr2012.Interpolation = 'Boolean'
keyFramewr2012.KeyTime = 0.62
keyFramewr2012.KeyValues = [1]

keyFramewr2013 = CompositeKeyFrame()
keyFramewr2013.Interpolation = 'Boolean'
keyFramewr2013.KeyTime = 0.64
keyFramewr2013.KeyValues = [0]

keyFramewr2014 = CompositeKeyFrame()
keyFramewr2014.Interpolation = 'Boolean'
keyFramewr2014.KeyTime = 0.72
keyFramewr2014.KeyValues = [1]

keyFramewr2015 = CompositeKeyFrame()
keyFramewr2015.Interpolation = 'Boolean'
keyFramewr2015.KeyTime = 0.74
keyFramewr2015.KeyValues = [0]

keyFramewr2016 = CompositeKeyFrame()
keyFramewr2016.Interpolation = 'Boolean'
keyFramewr2016.KeyTime = 0.82
keyFramewr2016.KeyValues = [1]

keyFramewr2017 = CompositeKeyFrame()
keyFramewr2017.Interpolation = 'Boolean'
keyFramewr2017.KeyTime = 0.84
keyFramewr2017.KeyValues = [0]

keyFramewr2018 = CompositeKeyFrame()
keyFramewr2018.Interpolation = 'Boolean'
keyFramewr2018.KeyTime = 0.92
keyFramewr2018.KeyValues = [1]

keyFramewr2019 = CompositeKeyFrame()
keyFramewr2019.Interpolation = 'Boolean'
keyFramewr2019.KeyTime = 0.94
keyFramewr2019.KeyValues = [0]

keyFramewr2020 = CompositeKeyFrame()
keyFramewr2020.Interpolation = 'Boolean'
keyFramewr2020.KeyTime = 1.0
keyFramewr2020.KeyValues = [0]


wr_2VisibilityTrack.KeyFrames = [keyFramewr1999, keyFramewr2000, keyFramewr2001, keyFramewr2002, keyFramewr2003, keyFramewr2004, keyFramewr2005, keyFramewr2006, keyFramewr2007, keyFramewr2008, keyFramewr2009, keyFramewr2010 , keyFramewr2011, keyFramewr2012, keyFramewr2013, keyFramewr2014, keyFramewr2015, keyFramewr2016, keyFramewr2017, keyFramewr2018, keyFramewr2019, keyFramewr2020 ]

wr_3VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wr_3)

# create a key frame
keyFramewr2999 = CompositeKeyFrame()
keyFramewr2999.Interpolation = 'Boolean'
keyFramewr2999.KeyTime = 0.00
keyFramewr2999.KeyValues = [0]

keyFramewr3000 = CompositeKeyFrame()
keyFramewr3000.Interpolation = 'Boolean'
keyFramewr3000.KeyTime = 0.04
keyFramewr3000.KeyValues = [1]

keyFramewr3001 = CompositeKeyFrame()
keyFramewr3001.Interpolation = 'Boolean'
keyFramewr3001.KeyTime = 0.06
keyFramewr3001.KeyValues = [0]

keyFramewr3002 = CompositeKeyFrame()
keyFramewr3002.Interpolation = 'Boolean'
keyFramewr3002.KeyTime = 0.14
keyFramewr3002.KeyValues = [1]

keyFramewr3003 = CompositeKeyFrame()
keyFramewr3003.Interpolation = 'Boolean'
keyFramewr3003.KeyTime = 0.16
keyFramewr3003.KeyValues = [0]

keyFramewr3004 = CompositeKeyFrame()
keyFramewr3004.Interpolation = 'Boolean'
keyFramewr3004.KeyTime = 0.24
keyFramewr3004.KeyValues = [1]


keyFramewr3005 = CompositeKeyFrame()
keyFramewr3005.Interpolation = 'Boolean'
keyFramewr3005.KeyTime = 0.26
keyFramewr3005.KeyValues = [0]


keyFramewr3006 = CompositeKeyFrame()
keyFramewr3006.Interpolation = 'Boolean'
keyFramewr3006.KeyTime = 0.34
keyFramewr3006.KeyValues = [1]

keyFramewr3007 = CompositeKeyFrame()
keyFramewr3007.Interpolation = 'Boolean'
keyFramewr3007.KeyTime = 0.36
keyFramewr3007.KeyValues = [0]

keyFramewr3008 = CompositeKeyFrame()
keyFramewr3008.Interpolation = 'Boolean'
keyFramewr3008.KeyTime = 0.44
keyFramewr3008.KeyValues = [1]

keyFramewr3009 = CompositeKeyFrame()
keyFramewr3009.Interpolation = 'Boolean'
keyFramewr3009.KeyTime = 0.46
keyFramewr3009.KeyValues = [0]

keyFramewr3010 = CompositeKeyFrame()
keyFramewr3010.Interpolation = 'Boolean'
keyFramewr3010.KeyTime = 0.54
keyFramewr3010.KeyValues = [1]

keyFramewr3011 = CompositeKeyFrame()
keyFramewr3011.Interpolation = 'Boolean'
keyFramewr3011.KeyTime = 0.56
keyFramewr3011.KeyValues = [0]

keyFramewr3012 = CompositeKeyFrame()
keyFramewr3012.Interpolation = 'Boolean'
keyFramewr3012.KeyTime = 0.64
keyFramewr3012.KeyValues = [1]

keyFramewr3013 = CompositeKeyFrame()
keyFramewr3013.Interpolation = 'Boolean'
keyFramewr3013.KeyTime = 0.66
keyFramewr3013.KeyValues = [0]

keyFramewr3014 = CompositeKeyFrame()
keyFramewr3014.Interpolation = 'Boolean'
keyFramewr3014.KeyTime = 0.74
keyFramewr3014.KeyValues = [1]

keyFramewr3015 = CompositeKeyFrame()
keyFramewr3015.Interpolation = 'Boolean'
keyFramewr3015.KeyTime = 0.76
keyFramewr3015.KeyValues = [0]

keyFramewr3016 = CompositeKeyFrame()
keyFramewr3016.Interpolation = 'Boolean'
keyFramewr3016.KeyTime = 0.84
keyFramewr3016.KeyValues = [1]

keyFramewr3017 = CompositeKeyFrame()
keyFramewr3017.Interpolation = 'Boolean'
keyFramewr3017.KeyTime = 0.86
keyFramewr3017.KeyValues = [0]

keyFramewr3018 = CompositeKeyFrame()
keyFramewr3018.Interpolation = 'Boolean'
keyFramewr3018.KeyTime = 0.94
keyFramewr3018.KeyValues = [1]

keyFramewr3019 = CompositeKeyFrame()
keyFramewr3019.Interpolation = 'Boolean'
keyFramewr3019.KeyTime = 0.96
keyFramewr3019.KeyValues = [0]

keyFramewr3020 = CompositeKeyFrame()
keyFramewr3020.Interpolation = 'Boolean'
keyFramewr3020.KeyTime = 1.0
keyFramewr3020.KeyValues = [0]


wr_3VisibilityTrack.KeyFrames = [keyFramewr2999, keyFramewr3000, keyFramewr3001, keyFramewr3002, keyFramewr3003, keyFramewr3004, keyFramewr3005, keyFramewr3006, keyFramewr3007, keyFramewr3008, keyFramewr3009, keyFramewr3010 , keyFramewr3011, keyFramewr3012, keyFramewr3013, keyFramewr3014, keyFramewr3015, keyFramewr3016, keyFramewr3017, keyFramewr3018, keyFramewr3019, keyFramewr3020 ]

wr_4VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wr_4)

# create a key frame
keyFramewr3999 = CompositeKeyFrame()
keyFramewr3999.Interpolation = 'Boolean'
keyFramewr3999.KeyTime = 0.00
keyFramewr3999.KeyValues = [0]

keyFramewr4000 = CompositeKeyFrame()
keyFramewr4000.Interpolation = 'Boolean'
keyFramewr4000.KeyTime = 0.06
keyFramewr4000.KeyValues = [1]

keyFramewr4001 = CompositeKeyFrame()
keyFramewr4001.Interpolation = 'Boolean'
keyFramewr4001.KeyTime = 0.08
keyFramewr4001.KeyValues = [0]

keyFramewr4002 = CompositeKeyFrame()
keyFramewr4002.Interpolation = 'Boolean'
keyFramewr4002.KeyTime = 0.16
keyFramewr4002.KeyValues = [1]

keyFramewr4003 = CompositeKeyFrame()
keyFramewr4003.Interpolation = 'Boolean'
keyFramewr4003.KeyTime = 0.18
keyFramewr4003.KeyValues = [0]

keyFramewr4004 = CompositeKeyFrame()
keyFramewr4004.Interpolation = 'Boolean'
keyFramewr4004.KeyTime = 0.26
keyFramewr4004.KeyValues = [1]


keyFramewr4005 = CompositeKeyFrame()
keyFramewr4005.Interpolation = 'Boolean'
keyFramewr4005.KeyTime = 0.28
keyFramewr4005.KeyValues = [0]


keyFramewr4006 = CompositeKeyFrame()
keyFramewr4006.Interpolation = 'Boolean'
keyFramewr4006.KeyTime = 0.36
keyFramewr4006.KeyValues = [1]

keyFramewr4007 = CompositeKeyFrame()
keyFramewr4007.Interpolation = 'Boolean'
keyFramewr4007.KeyTime = 0.38
keyFramewr4007.KeyValues = [0]

keyFramewr4008 = CompositeKeyFrame()
keyFramewr4008.Interpolation = 'Boolean'
keyFramewr4008.KeyTime = 0.46
keyFramewr4008.KeyValues = [1]

keyFramewr4009 = CompositeKeyFrame()
keyFramewr4009.Interpolation = 'Boolean'
keyFramewr4009.KeyTime = 0.48
keyFramewr4009.KeyValues = [0]

keyFramewr4010 = CompositeKeyFrame()
keyFramewr4010.Interpolation = 'Boolean'
keyFramewr4010.KeyTime = 0.56
keyFramewr4010.KeyValues = [1]

keyFramewr4011 = CompositeKeyFrame()
keyFramewr4011.Interpolation = 'Boolean'
keyFramewr4011.KeyTime = 0.58
keyFramewr4011.KeyValues = [0]

keyFramewr4012 = CompositeKeyFrame()
keyFramewr4012.Interpolation = 'Boolean'
keyFramewr4012.KeyTime = 0.66
keyFramewr4012.KeyValues = [1]

keyFramewr4013 = CompositeKeyFrame()
keyFramewr4013.Interpolation = 'Boolean'
keyFramewr4013.KeyTime = 0.68
keyFramewr4013.KeyValues = [0]

keyFramewr4014 = CompositeKeyFrame()
keyFramewr4014.Interpolation = 'Boolean'
keyFramewr4014.KeyTime = 0.76
keyFramewr4014.KeyValues = [1]

keyFramewr4015 = CompositeKeyFrame()
keyFramewr4015.Interpolation = 'Boolean'
keyFramewr4015.KeyTime = 0.78
keyFramewr4015.KeyValues = [0]

keyFramewr4016 = CompositeKeyFrame()
keyFramewr4016.Interpolation = 'Boolean'
keyFramewr4016.KeyTime = 0.86
keyFramewr4016.KeyValues = [1]

keyFramewr4017 = CompositeKeyFrame()
keyFramewr4017.Interpolation = 'Boolean'
keyFramewr4017.KeyTime = 0.88
keyFramewr4017.KeyValues = [0]

keyFramewr4018 = CompositeKeyFrame()
keyFramewr4018.Interpolation = 'Boolean'
keyFramewr4018.KeyTime = 0.96
keyFramewr4018.KeyValues = [1]

keyFramewr4019 = CompositeKeyFrame()
keyFramewr4019.Interpolation = 'Boolean'
keyFramewr4019.KeyTime = 0.98
keyFramewr4019.KeyValues = [0]

keyFramewr4020 = CompositeKeyFrame()
keyFramewr4020.Interpolation = 'Boolean'
keyFramewr4020.KeyTime = 1.0
keyFramewr4020.KeyValues = [0]


wr_4VisibilityTrack.KeyFrames = [keyFramewr3999, keyFramewr4000, keyFramewr4001, keyFramewr4002, keyFramewr4003, keyFramewr4004, keyFramewr4005, keyFramewr4006, keyFramewr4007, keyFramewr4008, keyFramewr4009, keyFramewr4010 , keyFramewr4011, keyFramewr4012, keyFramewr4013, keyFramewr4014, keyFramewr4015, keyFramewr4016, keyFramewr4017, keyFramewr4018, keyFramewr4019, keyFramewr4020 ]

wr_5VisibilityTrack = GetAnimationTrack('Visibility', index=-1, proxy=wr_5)

# create a key frame
keyFramewr4999 = CompositeKeyFrame()
keyFramewr4999.Interpolation = 'Boolean'
keyFramewr4999.KeyTime = 0.00
keyFramewr4999.KeyValues = [0]

keyFramewr5000 = CompositeKeyFrame()
keyFramewr5000.Interpolation = 'Boolean'
keyFramewr5000.KeyTime = 0.08
keyFramewr5000.KeyValues = [1]

keyFramewr5001 = CompositeKeyFrame()
keyFramewr5001.Interpolation = 'Boolean'
keyFramewr5001.KeyTime = 0.10
keyFramewr5001.KeyValues = [0]

keyFramewr5002 = CompositeKeyFrame()
keyFramewr5002.Interpolation = 'Boolean'
keyFramewr5002.KeyTime = 0.18
keyFramewr5002.KeyValues = [1]

keyFramewr5003 = CompositeKeyFrame()
keyFramewr5003.Interpolation = 'Boolean'
keyFramewr5003.KeyTime = 0.20
keyFramewr5003.KeyValues = [0]

keyFramewr5004 = CompositeKeyFrame()
keyFramewr5004.Interpolation = 'Boolean'
keyFramewr5004.KeyTime = 0.28
keyFramewr5004.KeyValues = [1]


keyFramewr5005 = CompositeKeyFrame()
keyFramewr5005.Interpolation = 'Boolean'
keyFramewr5005.KeyTime = 0.30
keyFramewr5005.KeyValues = [0]


keyFramewr5006 = CompositeKeyFrame()
keyFramewr5006.Interpolation = 'Boolean'
keyFramewr5006.KeyTime = 0.38
keyFramewr5006.KeyValues = [1]

keyFramewr5007 = CompositeKeyFrame()
keyFramewr5007.Interpolation = 'Boolean'
keyFramewr5007.KeyTime = 0.40
keyFramewr5007.KeyValues = [0]

keyFramewr5008 = CompositeKeyFrame()
keyFramewr5008.Interpolation = 'Boolean'
keyFramewr5008.KeyTime = 0.48
keyFramewr5008.KeyValues = [1]

keyFramewr5009 = CompositeKeyFrame()
keyFramewr5009.Interpolation = 'Boolean'
keyFramewr5009.KeyTime = 0.50
keyFramewr5009.KeyValues = [0]

keyFramewr5010 = CompositeKeyFrame()
keyFramewr5010.Interpolation = 'Boolean'
keyFramewr5010.KeyTime = 0.58
keyFramewr5010.KeyValues = [1]

keyFramewr5011 = CompositeKeyFrame()
keyFramewr5011.Interpolation = 'Boolean'
keyFramewr5011.KeyTime = 0.60
keyFramewr5011.KeyValues = [0]

keyFramewr5012 = CompositeKeyFrame()
keyFramewr5012.Interpolation = 'Boolean'
keyFramewr5012.KeyTime = 0.68
keyFramewr5012.KeyValues = [1]

keyFramewr5013 = CompositeKeyFrame()
keyFramewr5013.Interpolation = 'Boolean'
keyFramewr5013.KeyTime = 0.70
keyFramewr5013.KeyValues = [0]

keyFramewr5014 = CompositeKeyFrame()
keyFramewr5014.Interpolation = 'Boolean'
keyFramewr5014.KeyTime = 0.78
keyFramewr5014.KeyValues = [1]

keyFramewr5015 = CompositeKeyFrame()
keyFramewr5015.Interpolation = 'Boolean'
keyFramewr5015.KeyTime = 0.80
keyFramewr5015.KeyValues = [0]

keyFramewr5016 = CompositeKeyFrame()
keyFramewr5016.Interpolation = 'Boolean'
keyFramewr5016.KeyTime = 0.88
keyFramewr5016.KeyValues = [1]

keyFramewr5017 = CompositeKeyFrame()
keyFramewr5017.Interpolation = 'Boolean'
keyFramewr5017.KeyTime = 0.90
keyFramewr5017.KeyValues = [0]

keyFramewr5018 = CompositeKeyFrame()
keyFramewr5018.Interpolation = 'Boolean'
keyFramewr5018.KeyTime = 0.98
keyFramewr5018.KeyValues = [1]

keyFramewr5019 = CompositeKeyFrame()
keyFramewr5019.Interpolation = 'Boolean'
keyFramewr5019.KeyTime = 1.0
keyFramewr5019.KeyValues = [0]


wr_5VisibilityTrack.KeyFrames = [keyFramewr4999, keyFramewr5000, keyFramewr5001, keyFramewr5002, keyFramewr5003, keyFramewr5004, keyFramewr5005, keyFramewr5006, keyFramewr5007, keyFramewr5008, keyFramewr5009, keyFramewr5010 , keyFramewr5011, keyFramewr5012, keyFramewr5013, keyFramewr5014, keyFramewr5015, keyFramewr5016, keyFramewr5017, keyFramewr5018, keyFramewr5019 ]



animationScene1 = GetAnimationScene()
animationScene1.NumberOfFrames = 100
