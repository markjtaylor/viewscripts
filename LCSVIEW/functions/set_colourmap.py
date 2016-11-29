

# get color transfer function/color map for 'MRLVelocity'
mRLVelocityLUT = GetColorTransferFunction('MRLVelocity')
mRLVelocityLUT.RGBPoints = [55.946010717046455, 0.231373, 0.298039, 0.752941, 80.34874800973748, 0.865003, 0.865003, 0.865003, 104.75148530242849, 0.705882, 0.0156863, 0.14902]
mRLVelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'MRLVelocity'
mRLVelocityPWF = GetOpacityTransferFunction('MRLVelocity')
mRLVelocityPWF.Points = [55.946010717046455, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
mRLVelocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mRLVelocityLUT.ApplyPreset('Blue to Red Rainbow', True)

