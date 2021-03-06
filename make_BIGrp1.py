####
rp1case = EnSightReader(CaseFileName='/home/dmculley/MarkT/inp_BIGrp1/trackcar_RP1.case')
rp1case.CellArrays = ['PressureCoefficient', 'TotalPressureCoefficient', 'Velocity']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

renderView1.UseTexturedBackground = 0

# Properties modified on renderView1
renderView1.Background = [0.9, 0.9, 0.9]


txt = servermanager.rendering.ImageTexture()
#txt.SourceProcess="Client"
#txt.FileName = "/Users/keritaylor/LCS/ensightfiles/logos/LCSlogo_lightbg_lhcorner.png"

#renderView1.BackgroundTexture = txt
#renderView1.UseTexturedBackground = 1

rp1caseDisplay = Show(rp1case, renderView1)
rp1caseDisplay.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'AbsolutePressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-3.0, 0.231373, 0.298039, 0.752941, -0.9496047496795654, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
rp1caseDisplay.SetScalarBarVisibility(renderView1, False)

# create a new 'Reflect'
reflect1 = Reflect(Input=rp1case)

# Properties modified on reflect1
reflect1.Plane = 'Y'

# hide data in view
Hide(rp1case, renderView1)

reflect1Display = Show(reflect1, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, False )

Hide(reflect1, renderView1)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=reflect1)
# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
# trace defaults for the display properties.
#cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'PressureCoefficient']
#cellDatatoPointData1Display.LookupTable = pressureLUT
#cellDatatoPointData1Display.GlyphType = 'Arrow'
#cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.07036986613198369
#cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'PressureCoefficient']
#cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
#cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Pressure']
#cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, False)




# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=reflect1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)
extractSurface1Display.SetScalarBarVisibility(renderView1, False)
Hide(extractSurface1, renderView1)

# get active source.
car_scalar = ExtractBlock(Input=extractSurface1)

# Properties modified on car_scalar
car_scalar.BlockIndices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145]


# show data in view
car_scalarDisplay = Show(car_scalar, renderView1)

road = ExtractBlock(Input=extractSurface1)
road.BlockIndices = [114]
roadDisplay = Show(road, renderView1)

#ColorBy(roadDisplay, Solid)
#roadDisplay.DiffuseColor = [0.4627450980392157, 0.4627450980392157, 0.4627450980392157]


# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
car_scalarDisplay.SetScalarBarVisibility(renderView1, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=car_scalar)

# set scalar coloring
ColorBy(car_scalarDisplay, ('CELLS', 'PressureCoefficient'))

# rescale color and/or opacity maps used to include current data range
car_scalarDisplay.RescaleTransferFunctionToDataRange(True)

# Rescale transfer function
pressureLUT.RescaleTransferFunction(-150.0, 250.0)

# Rescale transfer function
#pressurePWF.RescaleTransferFunction(-150.0, 250.0)

# show color bar/color legend
car_scalarDisplay.SetScalarBarVisibility(renderView1, True)


#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.0697988206012288, -0.08148098801403743, -1.7869891152526152]
renderView1.CameraFocalPoint = [1.0798208713531483, -0.6096000075340282, 0.4060007091175053]
renderView1.CameraViewUp = [0.5059647601357299, -0.31569800070552967, -0.8027044498763694]
renderView1.CameraParallelScale = 6.745505525367322


# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer1.Vectors = ['CELLS', 'Velocity']
streamTracer1.MaximumStreamlineLength = 13.411200046539307

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'FORWARD'
streamTracer1.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [-0.3, -0.9, 0.03]
streamTracer1.SeedType.Point2 = [-0.3, 0.9, 0.03]
streamTracer1.SeedType.Resolution = 30

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)


# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Velocity'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [55.946010717046455, 0.231373, 0.298039, 0.752941, 80.34874800973748, 0.865003, 0.865003, 0.865003, 104.75148530242849, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

velocityLUT.RescaleTransferFunction(-5.0, 30.0)


# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [55.946010717046455, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocityLUT.ApplyPreset('Blue to Red Rainbow', True)
velocityLUT.RescaleTransferFunction(-5.0, 30.0)

# hide color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.4878276355882836, -0.7494322110574833, 1.9095130497029669]
renderView1.CameraFocalPoint = [1.0798208713531494, -0.6096000075340253, 0.40600070911750724]
renderView1.CameraViewUp = [0.38506275983971405, 0.07009092103348225, 0.9202249365091673]
renderView1.CameraParallelScale = 6.745505525367322

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1)

# create a new 'Tube'
xtube = Tube(Input=streamTracer1)
xtube.Scalars = ['POINTS', 'AngularVelocity']
xtube.Vectors = ['POINTS', 'Normals']

# Properties modified on xtube
xtube.Radius = 0.008435356878489255

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [55.946010717046455, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# show data in view
xtubeDisplay = Show(xtube, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# show color bar/color legend
xtubeDisplay.SetScalarBarVisibility(renderView1, False)


# set active source
SetActiveSource(xtube)


# Properties modified on xtubeDisplay
xtubeDisplay.Opacity = 0.54

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.7811588882402662, -2.1068784148641444, 2.5463676072581394]
renderView1.CameraFocalPoint = [1.0798208713531479, -0.6096000075340253, 0.4060007091175068]
renderView1.CameraViewUp = [0.4969906885904914, 0.24172002704300724, 0.833409673558375]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).


#slice1 = Slice(Input=reflect1)
slice1 = Slice(Input=cellDatatoPointData1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [2.75, -1.249999998555622, 0.75]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [815, 491]

# get color transfer function/color map for 'AbsolutePressure'

# show data in view
slice1Display = Show(slice1, renderView1)
Hide3DWidgets(proxy=slice1)


# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

#slice2 = Slice(Input=reflect1)
slice2 = Slice(Input=cellDatatoPointData1)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [2.75, -1.249999998555622, 0.75]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [815, 491]

# get color transfer function/color map for 'AbsolutePressure'

# show data in view
slice2Display = Show(slice2, renderView1)


# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)
Hide3DWidgets(proxy=slice2)



# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [2.0845985899965616, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-5.0, 30.0)

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [2.0845985899965616, 0.0, 0.5, 0.0, 104.75148530242849, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-5.0, 30.0)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'Velocity'))
ColorBy(slice2Display, ('POINTS', 'Velocity'))


# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, False)
slice2Display.SetScalarBarVisibility(renderView1, False)

# create a new 'Cell Data to Point Data'
yslice = CellDatatoPointData(Input=slice1)
# show data in view
ysliceDisplay = Show(yslice, renderView1)

# create a new 'Cell Data to Point Data'
xslice = CellDatatoPointData(Input=slice2)
# show data in view
xsliceDisplay = Show(xslice, renderView1)

ColorBy(ysliceDisplay, ('POINTS', 'Velocity'))
ColorBy(xsliceDisplay, ('POINTS', 'Velocity'))

Hide(slice2, renderView1)
Hide(slice1, renderView1)


#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.4573392295426908, -3.520612042492187, 0.09447891651323534]
renderView1.CameraFocalPoint = [1.0798208713531474, -0.6096000075340253, 0.40600070911750524]
renderView1.CameraViewUp = [-0.4180256323595505, 0.2715693624604568, 0.8668936797919449]
renderView1.CameraParallelScale = 6.745505525367322

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).



# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer2.Vectors = ['CELLS', 'Velocity']
streamTracer2.MaximumStreamlineLength = 13.411200046539307


# Properties modified on streamTracer2
streamTracer2.IntegrationDirection = 'FORWARD'
streamTracer2.SeedType = 'High Resolution Line Source'

streamTracer2.SeedType.Resolution = 12

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [-0.3, -0.3, 0.03]
streamTracer2.SeedType.Point2 = [-0.3, -0.3, 0.7]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [803, 491]

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)
Hide3DWidgets(proxy=streamTracer2)

# create a new 'Tube'
ytube = Tube(Input=streamTracer2)
ytube.Scalars = ['POINTS', 'AngularVelocity']
ytube.Vectors = ['POINTS', 'Normals']

# Properties modified on ytube
ytube.Radius = 0.015

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [802, 491]

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [55.946010717046455, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0


# show data in view
ytubeDisplay = Show(ytube, renderView1)
ytubeDisplay.Opacity = 0.54
ColorBy(ytubeDisplay, ('POINTS', 'Velocity'))

# rescale color and/or opacity maps used to include current data range
ytubeDisplay.RescaleTransferFunctionToDataRange(True)

Hide(streamTracer2, renderView1)
# hide data in view

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.9282228297255046, 1.1921335145632892, 2.0378323114544195]
renderView1.CameraFocalPoint = [1.0798208713531545, -0.6096000075340238, 0.40600070911750713]
renderView1.CameraViewUp = [0.2686089945940614, -0.24596129375734, 0.9313174807746192]
renderView1.CameraParallelScale = 6.745505525367322


# create a new 'STL Reader'
org_fronttyrestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_fronttyre.stl'])

# show data in view
org_fronttyrestlDisplay = Show(org_fronttyrestl, renderView1)

# create a new 'Transform'
transform1 = Transform(Input=org_fronttyrestl)
transform1.Transform = 'Transform'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1)

# Properties modified on transform1.Transform
transform1.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform1Display = Show(transform1, renderView1)
# trace defaults for the display properties.
Hide(org_fronttyrestl, renderView1)

# change representation type

# create a new 'STL Reader'
org_frontbrakestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_frontbrake.stl'])

# show data in view
org_frontbrakestlDisplay = Show(org_frontbrakestl, renderView1)

# create a new 'Transform'
transform5 = Transform(Input=org_frontbrakestl)
transform5.Transform = 'Transform'

# Properties modified on transform5.Transform
transform5.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform5Display = Show(transform5, renderView1)

# hide data in view
Hide(org_frontbrakestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform5)

# create a new 'STL Reader'
org_frontspokestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_frontspoke.stl'])

# show data in view
org_frontspokestlDisplay = Show(org_frontspokestl, renderView1)

# create a new 'Transform'
transform6 = Transform(Input=org_frontspokestl)
transform6.Transform = 'Transform'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform6)

# Properties modified on transform6.Transform
transform6.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform6Display = Show(transform6, renderView1)

# hide data in view
Hide(org_frontspokestl, renderView1)


# create a new 'STL Reader'
org_backbrakestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_backbrake.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [957, 491]

# show data in view
org_backbrakestlDisplay = Show(org_backbrakestl, renderView1)

# create a new 'Transform'
transform3 = Transform(Input=org_backbrakestl)
transform3.Transform = 'Transform'

# Properties modified on transform3.Transform
transform3.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform3Display = Show(transform3, renderView1)
Hide(org_backbrakestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform3)



org_backspokestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_backspoke.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [957, 491]

# show data in view
org_backspokestlDisplay = Show(org_backspokestl, renderView1)

# create a new 'Transform'
transform4 = Transform(Input=org_backspokestl)
transform4.Transform = 'Transform'

# Properties modified on transform3.Transform
transform4.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform4Display = Show(transform4, renderView1)
Hide(org_backspokestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform4)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform3)

org_backtyrestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_backtyre.stl'])


# show data in view
org_backtyrestlDisplay = Show(org_backtyrestl, renderView1)

# create a new 'Transform'
transform2 = Transform(Input=org_backtyrestl)
transform2.Transform = 'Transform'

# Properties modified on transform3.Transform
transform2.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform2Display = Show(transform2, renderView1)
Hide(org_backtyrestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform2)

#reflect the wheels brakes and spokes

reflect2 = Reflect(Input=transform1)
reflect2.Plane = 'Y'
Hide(transform1, renderView1)
reflect2Display = Show(reflect2, renderView1)
reflect2Display.DiffuseColor = [0.2, 0.2, 0.2]

reflect3 = Reflect(Input=transform2)
reflect3.Plane = 'Y'
Hide(transform2, renderView1)
reflect3Display = Show(reflect3, renderView1)
reflect3Display.DiffuseColor = [0.2, 0.2, 0.2]


reflect4 = Reflect(Input=transform3)
reflect4.Plane = 'Y'
Hide(transform3, renderView1)
reflect4Display = Show(reflect4, renderView1)
reflect4Display.DiffuseColor = [0.66, 0.33, 0.0]

wr_1 = Reflect(Input=transform4)
wr_1.Plane = 'Y'
Hide(transform4, renderView1)
wr_1Display = Show(wr_1, renderView1)
wr_1Display.DiffuseColor = [0.7,0.7,0.7]

wr_2 = Shrink(Input=wr_1)
wr_2.ShrinkFactor = 1.0
wr_2Display = Show(wr_2, renderView1)
wr_2Display.DiffuseColor = [0.7, 0.7, 0.7]
wr_2Display.Orientation = [0.0,-6.0, 0.0]
wr_2Display.Origin = [3.45,-.828,.3235]
Hide(wr_2, renderView1)

wr_3 = Shrink(Input=wr_1)
wr_3.ShrinkFactor = 1.0
wr_3Display = Show(wr_3, renderView1)
wr_3Display.DiffuseColor = [0.7, 0.7, 0.7]
wr_3Display.Orientation = [0.0,-12.0, 0.0]
wr_3Display.Origin = [3.45,-.828,.3235]
Hide(wr_3, renderView1)

wr_4 = Shrink(Input=wr_1)
wr_4.ShrinkFactor = 1.0
wr_4Display = Show(wr_4, renderView1)
wr_4Display.DiffuseColor = [0.7, 0.7, 0.7]
wr_4Display.Orientation = [0.0,-18.0, 0.0]
wr_4Display.Origin = [3.45,-.828,.3235]
Hide(wr_4, renderView1)

wr_5 = Shrink(Input=wr_1)
wr_5.ShrinkFactor = 1.0
wr_5Display = Show(wr_5, renderView1)
wr_5Display.DiffuseColor = [0.7, 0.7, 0.7]
wr_5Display.Orientation = [0.0,-24.0, 0.0]
wr_5Display.Origin = [3.45,-.828,.3235]
Hide(wr_5, renderView1)


reflect6 = Reflect(Input=transform5)
reflect6.Plane = 'Y'
Hide(transform5, renderView1)
reflect6Display = Show(reflect6, renderView1)
reflect6Display.DiffuseColor = [0.66, 0.33, 0.0]


wf_1 = Reflect(Input=transform6)
wf_1.Plane = 'Y'
Hide(transform6, renderView1)
wf_1Display = Show(wf_1, renderView1)
wf_1Display.DiffuseColor = [0.7, 0.7, 0.7]

wf_2 = Shrink(Input=wf_1)
wf_2.ShrinkFactor = 1.0
wf_2Display = Show(wf_2, renderView1)
wf_2Display.DiffuseColor = [0.7, 0.7, 0.7]
wf_2Display.Orientation = [0.0, -6.0, 0.0]
wf_2Display.Origin = [0.93,-.822,.32]
Hide(wf_2, renderView1)

wf_3 = Shrink(Input=wf_1)
wf_3.ShrinkFactor = 1.0
wf_3Display = Show(wf_3, renderView1)
wf_3Display.DiffuseColor = [0.7, 0.7, 0.7]
wf_3Display.Orientation = [0.0, -12.0, 0.0]
wf_3Display.Origin = [0.93,-.822,.32]
Hide(wf_3, renderView1)

wf_4 = Shrink(Input=wf_1)
wf_4.ShrinkFactor = 1.0
wf_4Display = Show(wf_4, renderView1)
wf_4Display.DiffuseColor = [0.7, 0.7, 0.7]
wf_4Display.Orientation = [0.0, -18.0, 0.0]
wf_4Display.Origin = [0.93,-.822,.32]
Hide(wf_4, renderView1)

wf_5 = Shrink(Input=wf_1)
wf_5.ShrinkFactor = 1.0
wf_5Display = Show(wf_5, renderView1)
wf_5Display.DiffuseColor = [0.7, 0.7, 0.7]
wf_5Display.Orientation = [0.0, -24.0, 0.0]
wf_5Display.Origin = [0.93,-.822,.32]
Hide(wf_5, renderView1)


streamTracer3 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer3.Vectors = ['CELLS', 'Velocity']
streamTracer3.MaximumStreamlineLength = 8.5
streamTracer3.SeedType.NumberOfPoints = 200
streamTracer3.SeedType.Center = [-0.9, 0.0, 0.1]
streamTracer3.IntegrationDirection = 'FORWARD'
streamTracer3.SeedType.Radius = 1.5

streamTracer3Display = Show(streamTracer3, renderView1)
# trace defaults for the display properties.
#streamTracer3Display.ColorArrayName = [None, '']
#streamTracer3Display.GlyphType = 'Arrow'
#streamTracer3Display.SetScaleArray = ['POINTS', 'AngularVelocity']
#streamTracer3Display.ScaleTransferFunction = 'PiecewiseFunction'
#streamTracer3Display.OpacityArray = ['POINTS', 'AngularVelocity']
#streamTracer3Display.OpacityTransferFunction = 'PiecewiseFunction'


# transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 104.75148530242849, 1.0, 0.0, 0.0]
velocityLUT.ColorSpace = 'HSV'
velocityLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [-5.0, 0.0, 0.5, 0.0, 32.56762294791605, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocityLUT.ApplyPreset('Blue to Red Rainbow', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocityLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-5.0, 30.0)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-5.0, 30.0)



slice1Display.SetScalarBarVisibility(renderView1, False)
slice2Display.SetScalarBarVisibility(renderView1, False)
xtubeDisplay.SetScalarBarVisibility(renderView1, False)
ytubeDisplay.SetScalarBarVisibility(renderView1, False)




#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
car_scalar = FindSource('ExtractBlock1')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [993, 491]

# hide data in view
Hide(car_scalar, renderView1)

# set active source
SetActiveSource(car_scalar)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [-250.0, 0.0, 0.0, 1.0, 250.0, 1.0, 0.0, 0.0]
pressureLUT.ColorSpace = 'HSV'
pressureLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pressureLUT.ScalarRangeInitialized = 1.0

# show data in view
car_scalarDisplay = Show(car_scalar, renderView1)
# trace defaults for the display properties.
#car_scalarDisplay.ColorArrayName = ['CELLS', 'Pressure']
#car_scalarDisplay.LookupTable = pressureLUT
#car_scalarDisplay.GlyphType = 'Arrow'
#car_scalarDisplay.SetScaleArray = [None, '']
#car_scalarDisplay.ScaleTransferFunction = 'PiecewiseFunction'
#car_scalarDisplay.OpacityArray = [None, '']
#car_scalarDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
car_scalarDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-1228.5826416015625, 0.0, 0.5, 0.0, 431.5299987792969, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# find source

# hide data in view
Hide(road, renderView1)

# set active source
SetActiveSource(road)

# show data in view
roadDisplay = Show(road, renderView1)
# trace defaults for the display properties.
#roadDisplay.ColorArrayName = ['CELLS', '']
#roadDisplay.DiffuseColor = [0.4627450980392157, 0.4627450980392157, 0.4627450980392157]
#roadDisplay.GlyphType = 'Arrow'
#roadDisplay.SetScaleArray = [None, '']
#roadDisplay.ScaleTransferFunction = 'PiecewiseFunction'
#roadDisplay.OpacityArray = [None, '']
#roadDisplay.OpacityTransferFunction = 'PiecewiseFunction'



# create a new 'Contour'
bigwake = Contour(Input=cellDatatoPointData1)
bigwake.ContourBy = ['POINTS', 'Velocity']
bigwake.Isosurfaces = [4.0]
bigwakeDisplay = Show(bigwake, renderView1)
bigwakeDisplay.SetScalarBarVisibility(renderView1, False)
ColorBy(bigwakeDisplay, None)
bigwakeDisplay.DiffuseColor = [0.0, 0.3333333333333333, 1.0]
bigwakeDisplay.Opacity = 0.29

smallwake = Contour(Input=cellDatatoPointData1)
smallwake.ContourBy = ['POINTS', 'Velocity']
smallwake.Isosurfaces = [2.0]
smallwakeDisplay = Show(smallwake, renderView1)
smallwakeDisplay.SetScalarBarVisibility(renderView1, False)
ColorBy(smallwakeDisplay, None)
smallwakeDisplay.DiffuseColor = [0.0, 0.3333333333333333, 1.0]
smallwakeDisplay.Opacity = 0.50

Hide(cellDatatoPointData1, renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [5.4247661916764125, -7.748548569292719, 2.683271019460903]
renderView1.CameraFocalPoint = [3.5378151371563127, -2.8711970456090747, 0.4872959332480492]
renderView1.CameraViewUp = [-0.08137157757728883, 0.3828399179854913, 0.9202240290056795]
renderView1.CameraParallelScale = 6.745505525367322


# find source

# create a new 'Contour'
contour3 = Contour(Input=streamTracer3)
contour3.ContourBy = ['POINTS', 'IntegrationTime']
contour3.Isosurfaces = [0.0]
contour3.PointMergeMethod = 'Uniform Binning'
contour3Display = Show(contour3, renderView1)

# hide data in view
Hide(streamTracer3, renderView1)


# Properties modified on bigwakeDisplay
contour3Display.GlyphType = 'Sphere'

# Properties modified on bigwakeDisplay.GlyphType
contour3Display.GlyphType.Radius = 0.03

ColorBy(contour3Display, ('POINTS', 'Velocity'))

# change representation type
contour3Display.SetRepresentationType('3D Glyphs')

# Properties modified on bigwakeDisplay
#contour3Display.SetScaleArray = [None, 'AngularVelocity']

# Properties modified on bigwakeDisplay
#contour3Display.OpacityArray = [None, 'AngularVelocity']

# set scalar coloring

Hide(contour3, renderView1)


# create a new 'Shrink'
car = Shrink(Input=car_scalar)

# Properties modified on car
car.ShrinkFactor = 1.0
carDisplay = Show(car, renderView1)

carDisplay.SetScalarBarVisibility(renderView1, False)
#ColorBy(carDisplay, None)

# change solid color
carDisplay.DiffuseColor = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
Hide(car_scalar, renderView1)

# Properties modified on renderView1
renderView1.LightSwitch = 1

# Properties modified on renderView1
renderView1.LightIntensity = 0.1



streamTracer4 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer4.Vectors = ['CELLS', 'Velocity']
streamTracer4.MaximumStreamlineLength = 13.411200046539307
streamTracer4.IntegrationDirection = 'FORWARD'
streamTracer4.SeedType = 'High Resolution Line Source'
streamTracer4.SeedType.Point1 = [-1.5, -0.9, 0.13]
streamTracer4.SeedType.Point2 = [-1.5, 0.9, 0.13]
streamTracer4.SeedType.Resolution = 12
streamTracer4Display = Show(streamTracer4, renderView1)
ColorBy(streamTracer4Display, ('POINTS', 'Velocity'))
streamTracer4Display.RescaleTransferFunctionToDataRange(True)
streamTracer4Display.SetScalarBarVisibility(renderView1, False)

balls_1 = Contour(Input=streamTracer4)
balls_1.ContourBy = ['POINTS', 'IntegrationTime']
balls_1.Isosurfaces = [0.0]
balls_1.PointMergeMethod = 'Uniform Binning'
balls_1Display = Show(balls_1, renderView1)
Hide(streamTracer4, renderView1)
balls_1Display.GlyphType = 'Sphere'
balls_1Display.GlyphType.Radius = 0.03
ColorBy(balls_1Display, ('POINTS', 'Velocity'))
balls_1Display.SetRepresentationType('3D Glyphs')
#balls_1Display.SetScaleArray = [None, 'AngularVelocity']
#balls_1Display.OpacityArray = [None, 'AngularVelocity']
Hide(balls_1, renderView1)

secballs_1 = Contour(Input=streamTracer4)
secballs_1.ContourBy = ['POINTS', 'IntegrationTime']
secballs_1.Isosurfaces = [0.0]
secballs_1.PointMergeMethod = 'Uniform Binning'
secballs_1Display = Show(secballs_1, renderView1)
Hide(streamTracer4, renderView1)
secballs_1Display.GlyphType = 'Sphere'
secballs_1Display.GlyphType.Radius = 0.03
ColorBy(secballs_1Display, ('POINTS', 'Velocity'))
secballs_1Display.SetRepresentationType('3D Glyphs')
#secballs_1Display.SetScaleArray = [None, 'AngularVelocity']
#secballs_1Display.OpacityArray = [None, 'AngularVelocity']
Hide(secballs_1, renderView1)

thiballs_1 = Contour(Input=streamTracer4)
thiballs_1.ContourBy = ['POINTS', 'IntegrationTime']
thiballs_1.Isosurfaces = [0.0]
thiballs_1.PointMergeMethod = 'Uniform Binning'
thiballs_1Display = Show(thiballs_1, renderView1)
Hide(streamTracer4, renderView1)
thiballs_1Display.GlyphType = 'Sphere'
thiballs_1Display.GlyphType.Radius = 0.03
ColorBy(thiballs_1Display, ('POINTS', 'Velocity'))
thiballs_1Display.SetRepresentationType('3D Glyphs')
#thiballs_1Display.SetScaleArray = [None, 'AngularVelocity']
#thiballs_1Display.OpacityArray = [None, 'AngularVelocity']
Hide(thiballs_1, renderView1)

fouballs_1 = Contour(Input=streamTracer4)
fouballs_1.ContourBy = ['POINTS', 'IntegrationTime']
fouballs_1.Isosurfaces = [0.0]
fouballs_1.PointMergeMethod = 'Uniform Binning'
fouballs_1Display = Show(fouballs_1, renderView1)
Hide(streamTracer4, renderView1)
fouballs_1Display.GlyphType = 'Sphere'
fouballs_1Display.GlyphType.Radius = 0.03
ColorBy(fouballs_1Display, ('POINTS', 'Velocity'))
fouballs_1Display.SetRepresentationType('3D Glyphs')
#fouballs_1Display.SetScaleArray = [None, 'AngularVelocity']
#fouballs_1Display.OpacityArray = [None, 'AngularVelocity']
Hide(fouballs_1, renderView1)


streamTracer5 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer5.Vectors = ['CELLS', 'Velocity']
streamTracer5.MaximumStreamlineLength = 13.411200046539307
streamTracer5.IntegrationDirection = 'FORWARD'
streamTracer5.SeedType = 'High Resolution Line Source'
streamTracer5.SeedType.Point1 = [-1.5, -0.9, 0.23]
streamTracer5.SeedType.Point2 = [-1.5, 0.9, 0.23]
streamTracer5.SeedType.Resolution = 12
streamTracer5Display = Show(streamTracer5, renderView1)
ColorBy(streamTracer5Display, ('POINTS', 'Velocity'))
streamTracer5Display.RescaleTransferFunctionToDataRange(True)

balls_2 = Contour(Input=streamTracer5)
balls_2.ContourBy = ['POINTS', 'IntegrationTime']
balls_2.Isosurfaces = [0.0]
balls_2.PointMergeMethod = 'Uniform Binning'
balls_2Display = Show(balls_2, renderView1)
Hide(streamTracer5, renderView1)
balls_2Display.GlyphType = 'Sphere'
balls_2Display.GlyphType.Radius = 0.03
ColorBy(balls_2Display, ('POINTS', 'Velocity'))
balls_2Display.SetRepresentationType('3D Glyphs')
#balls_2Display.SetScaleArray = [None, 'AngularVelocity']
#balls_2Display.OpacityArray = [None, 'AngularVelocity']
Hide(balls_2, renderView1)

secballs_2 = Contour(Input=streamTracer5)
secballs_2.ContourBy = ['POINTS', 'IntegrationTime']
secballs_2.Isosurfaces = [0.0]
secballs_2.PointMergeMethod = 'Uniform Binning'
secballs_2Display = Show(secballs_2, renderView1)
Hide(streamTracer5, renderView1)
secballs_2Display.GlyphType = 'Sphere'
secballs_2Display.GlyphType.Radius = 0.03
ColorBy(secballs_2Display, ('POINTS', 'Velocity'))
secballs_2Display.SetRepresentationType('3D Glyphs')
#secballs_2Display.SetScaleArray = [None, 'AngularVelocity']
#secballs_2Display.OpacityArray = [None, 'AngularVelocity']
Hide(secballs_2, renderView1)


thiballs_2 = Contour(Input=streamTracer5)
thiballs_2.ContourBy = ['POINTS', 'IntegrationTime']
thiballs_2.Isosurfaces = [0.0]
thiballs_2.PointMergeMethod = 'Uniform Binning'
thiballs_2Display = Show(thiballs_2, renderView1)
Hide(streamTracer5, renderView1)
thiballs_2Display.GlyphType = 'Sphere'
thiballs_2Display.GlyphType.Radius = 0.03
ColorBy(thiballs_2Display, ('POINTS', 'Velocity'))
thiballs_2Display.SetRepresentationType('3D Glyphs')
#thiballs_2Display.SetScaleArray = [None, 'AngularVelocity']
#thiballs_2Display.OpacityArray = [None, 'AngularVelocity']
Hide(thiballs_2, renderView1)

fouballs_2 = Contour(Input=streamTracer5)
fouballs_2.ContourBy = ['POINTS', 'IntegrationTime']
fouballs_2.Isosurfaces = [0.0]
fouballs_2.PointMergeMethod = 'Uniform Binning'
fouballs_2Display = Show(fouballs_2, renderView1)
Hide(streamTracer5, renderView1)
fouballs_2Display.GlyphType = 'Sphere'
fouballs_2Display.GlyphType.Radius = 0.03
ColorBy(fouballs_2Display, ('POINTS', 'Velocity'))
fouballs_2Display.SetRepresentationType('3D Glyphs')
#fouballs_2Display.SetScaleArray = [None, 'AngularVelocity']
#fouballs_2Display.OpacityArray = [None, 'AngularVelocity']
Hide(fouballs_2, renderView1)

streamTracer6 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer6.Vectors = ['CELLS', 'Velocity']
streamTracer6.MaximumStreamlineLength = 13.411200046539307
streamTracer6.IntegrationDirection = 'FORWARD'
streamTracer6.SeedType = 'High Resolution Line Source'
streamTracer6.SeedType.Point1 = [-1.5, -0.9, 0.33]
streamTracer6.SeedType.Point2 = [-1.5, 0.9, 0.33]
streamTracer6.SeedType.Resolution = 12
streamTracer6Display = Show(streamTracer6, renderView1)
ColorBy(streamTracer6Display, ('POINTS', 'Velocity'))
streamTracer6Display.RescaleTransferFunctionToDataRange(True)

balls_3 = Contour(Input=streamTracer6)
balls_3.ContourBy = ['POINTS', 'IntegrationTime']
balls_3.Isosurfaces = [0.0]
balls_3.PointMergeMethod = 'Uniform Binning'
balls_3Display = Show(balls_3, renderView1)
Hide(streamTracer6, renderView1)
balls_3Display.GlyphType = 'Sphere'
balls_3Display.GlyphType.Radius = 0.03
ColorBy(balls_3Display, ('POINTS', 'Velocity'))
balls_3Display.SetRepresentationType('3D Glyphs')
#balls_3Display.SetScaleArray = [None, 'AngularVelocity']
#balls_3Display.OpacityArray = [None, 'AngularVelocity']
Hide(balls_3, renderView1)

secballs_3 = Contour(Input=streamTracer6)
secballs_3.ContourBy = ['POINTS', 'IntegrationTime']
secballs_3.Isosurfaces = [0.0]
secballs_3.PointMergeMethod = 'Uniform Binning'
secballs_3Display = Show(secballs_3, renderView1)
Hide(streamTracer6, renderView1)
secballs_3Display.GlyphType = 'Sphere'
secballs_3Display.GlyphType.Radius = 0.03
ColorBy(secballs_3Display, ('POINTS', 'Velocity'))
secballs_3Display.SetRepresentationType('3D Glyphs')
#secballs_3Display.SetScaleArray = [None, 'AngularVelocity']
#secballs_3Display.OpacityArray = [None, 'AngularVelocity']
Hide(secballs_3, renderView1)


thiballs_3 = Contour(Input=streamTracer6)
thiballs_3.ContourBy = ['POINTS', 'IntegrationTime']
thiballs_3.Isosurfaces = [0.0]
thiballs_3.PointMergeMethod = 'Uniform Binning'
thiballs_3Display = Show(thiballs_3, renderView1)
Hide(streamTracer6, renderView1)
thiballs_3Display.GlyphType = 'Sphere'
thiballs_3Display.GlyphType.Radius = 0.03
ColorBy(thiballs_3Display, ('POINTS', 'Velocity'))
thiballs_3Display.SetRepresentationType('3D Glyphs')
#thiballs_3Display.SetScaleArray = [None, 'AngularVelocity']
#thiballs_3Display.OpacityArray = [None, 'AngularVelocity']
Hide(thiballs_3, renderView1)


fouballs_3 = Contour(Input=streamTracer6)
fouballs_3.ContourBy = ['POINTS', 'IntegrationTime']
fouballs_3.Isosurfaces = [0.0]
fouballs_3.PointMergeMethod = 'Uniform Binning'
fouballs_3Display = Show(fouballs_3, renderView1)
Hide(streamTracer6, renderView1)
fouballs_3Display.GlyphType = 'Sphere'
fouballs_3Display.GlyphType.Radius = 0.03
ColorBy(fouballs_3Display, ('POINTS', 'Velocity'))
fouballs_3Display.SetRepresentationType('3D Glyphs')
#fouballs_3Display.SetScaleArray = [None, 'AngularVelocity']
#fouballs_3Display.OpacityArray = [None, 'AngularVelocity']
Hide(fouballs_3, renderView1)

streamTracer7 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer7.Vectors = ['CELLS', 'Velocity']
streamTracer7.MaximumStreamlineLength = 13.411200046539307
streamTracer7.IntegrationDirection = 'FORWARD'
streamTracer7.SeedType = 'High Resolution Line Source'
streamTracer7.SeedType.Point1 = [-1.5, -0.9, 0.43]
streamTracer7.SeedType.Point2 = [-1.5, 0.9, 0.43]
streamTracer7.SeedType.Resolution = 12
streamTracer7Display = Show(streamTracer7, renderView1)
ColorBy(streamTracer7Display, ('POINTS', 'Velocity'))
streamTracer7Display.RescaleTransferFunctionToDataRange(True)


balls_4 = Contour(Input=streamTracer7)
balls_4.ContourBy = ['POINTS', 'IntegrationTime']
balls_4.Isosurfaces = [0.0]
balls_4.PointMergeMethod = 'Uniform Binning'
balls_4Display = Show(balls_4, renderView1)
Hide(streamTracer7, renderView1)
balls_4Display.GlyphType = 'Sphere'
balls_4Display.GlyphType.Radius = 0.03
ColorBy(balls_4Display, ('POINTS', 'Velocity'))
balls_4Display.SetRepresentationType('3D Glyphs')
#balls_4Display.SetScaleArray = [None, 'AngularVelocity']
#balls_4Display.OpacityArray = [None, 'AngularVelocity']
Hide(balls_4, renderView1)

secballs_4 = Contour(Input=streamTracer7)
secballs_4.ContourBy = ['POINTS', 'IntegrationTime']
secballs_4.Isosurfaces = [0.0]
secballs_4.PointMergeMethod = 'Uniform Binning'
secballs_4Display = Show(secballs_4, renderView1)
Hide(streamTracer7, renderView1)
secballs_4Display.GlyphType = 'Sphere'
secballs_4Display.GlyphType.Radius = 0.03
ColorBy(secballs_4Display, ('POINTS', 'Velocity'))
secballs_4Display.SetRepresentationType('3D Glyphs')
#secballs_4Display.SetScaleArray = [None, 'AngularVelocity']
#secballs_4Display.OpacityArray = [None, 'AngularVelocity']
Hide(secballs_4, renderView1)


thiballs_4 = Contour(Input=streamTracer7)
thiballs_4.ContourBy = ['POINTS', 'IntegrationTime']
thiballs_4.Isosurfaces = [0.0]
thiballs_4.PointMergeMethod = 'Uniform Binning'
thiballs_4Display = Show(thiballs_4, renderView1)
Hide(streamTracer7, renderView1)
thiballs_4Display.GlyphType = 'Sphere'
thiballs_4Display.GlyphType.Radius = 0.03
ColorBy(thiballs_4Display, ('POINTS', 'Velocity'))
thiballs_4Display.SetRepresentationType('3D Glyphs')
#thiballs_4Display.SetScaleArray = [None, 'AngularVelocity']
#thiballs_4Display.OpacityArray = [None, 'AngularVelocity']
Hide(thiballs_4, renderView1)

fouballs_4 = Contour(Input=streamTracer7)
fouballs_4.ContourBy = ['POINTS', 'IntegrationTime']
fouballs_4.Isosurfaces = [0.0]
fouballs_4.PointMergeMethod = 'Uniform Binning'
fouballs_4Display = Show(fouballs_4, renderView1)
Hide(streamTracer7, renderView1)
fouballs_4Display.GlyphType = 'Sphere'
fouballs_4Display.GlyphType.Radius = 0.03
ColorBy(fouballs_4Display, ('POINTS', 'Velocity'))
fouballs_4Display.SetRepresentationType('3D Glyphs')
#fouballs_4Display.SetScaleArray = [None, 'AngularVelocity']
#fouballs_4Display.OpacityArray = [None, 'AngularVelocity']
Hide(fouballs_4, renderView1)

streamTracer8 = StreamTracer(Input=reflect1,
    SeedType='Point Source')
streamTracer8.Vectors = ['CELLS', 'Velocity']
streamTracer8.MaximumStreamlineLength = 13.411200046539308
streamTracer8.IntegrationDirection = 'FORWARD'
streamTracer8.SeedType = 'High Resolution Line Source'
streamTracer8.SeedType.Point1 = [-1.5, -0.9, 0.03]
streamTracer8.SeedType.Point2 = [-1.5, 0.9, 0.03]
streamTracer8.SeedType.Resolution = 12
streamTracer8Display = Show(streamTracer8, renderView1)
ColorBy(streamTracer8Display, ('POINTS', 'Velocity'))
streamTracer8Display.RescaleTransferFunctionToDataRange(True)

balls_5 = Contour(Input=streamTracer8)
balls_5.ContourBy = ['POINTS', 'IntegrationTime']
balls_5.Isosurfaces = [0.0]
balls_5.PointMergeMethod = 'Uniform Binning'
balls_5Display = Show(balls_5, renderView1)
Hide(streamTracer8, renderView1)
balls_5Display.GlyphType = 'Sphere'
balls_5Display.GlyphType.Radius = 0.03
ColorBy(balls_5Display, ('POINTS', 'Velocity'))
balls_5Display.SetRepresentationType('3D Glyphs')
#balls_5Display.SetScaleArray = [None, 'AngularVelocity']
#balls_5Display.OpacityArray = [None, 'AngularVelocity']
Hide(balls_5, renderView1)

secballs_5 = Contour(Input=streamTracer8)
secballs_5.ContourBy = ['POINTS', 'IntegrationTime']
secballs_5.Isosurfaces = [0.0]
secballs_5.PointMergeMethod = 'Uniform Binning'
secballs_5Display = Show(secballs_5, renderView1)
Hide(streamTracer8, renderView1)
secballs_5Display.GlyphType = 'Sphere'
secballs_5Display.GlyphType.Radius = 0.03
ColorBy(secballs_5Display, ('POINTS', 'Velocity'))
secballs_5Display.SetRepresentationType('3D Glyphs')
#secballs_5Display.SetScaleArray = [None, 'AngularVelocity']
#secballs_5Display.OpacityArray = [None, 'AngularVelocity']
Hide(secballs_5, renderView1)

thiballs_5 = Contour(Input=streamTracer8)
thiballs_5.ContourBy = ['POINTS', 'IntegrationTime']
thiballs_5.Isosurfaces = [0.0]
thiballs_5.PointMergeMethod = 'Uniform Binning'
thiballs_5Display = Show(thiballs_5, renderView1)
Hide(streamTracer8, renderView1)
thiballs_5Display.GlyphType = 'Sphere'
thiballs_5Display.GlyphType.Radius = 0.03
ColorBy(thiballs_5Display, ('POINTS', 'Velocity'))
thiballs_5Display.SetRepresentationType('3D Glyphs')
#thiballs_5Display.SetScaleArray = [None, 'AngularVelocity']
#thiballs_5Display.OpacityArray = [None, 'AngularVelocity']
Hide(thiballs_5, renderView1)

fouballs_5 = Contour(Input=streamTracer8)
fouballs_5.ContourBy = ['POINTS', 'IntegrationTime']
fouballs_5.Isosurfaces = [0.0]
fouballs_5.PointMergeMethod = 'Uniform Binning'
fouballs_5Display = Show(fouballs_5, renderView1)
Hide(streamTracer8, renderView1)
fouballs_5Display.GlyphType = 'Sphere'
fouballs_5Display.GlyphType.Radius = 0.03
ColorBy(fouballs_5Display, ('POINTS', 'Velocity'))
fouballs_5Display.SetRepresentationType('3D Glyphs')
#fouballs_5Display.SetScaleArray = [None, 'AngularVelocity']
#fouballs_5Display.OpacityArray = [None, 'AngularVelocity']
Hide(fouballs_5, renderView1)



# current camera placement for renderView1
renderView1.CameraPosition = [2.75, -8.940388107355583, 0.5389858484268188]
renderView1.CameraFocalPoint = [2.75, 0.0, 0.5389858484268188]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 4.960141706121346

Hide(xtube, renderView1)
Hide(ytube, renderView1)
Hide(yslice, renderView1)
Hide(xslice, renderView1)
Hide(bigwake, renderView1)
Hide(smallwake, renderView1)

renderView1.OrientationAxesVisibility = 0




