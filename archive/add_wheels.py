#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
org_backtyrestl = FindSource('org_backtyre.stl')

# find source
clip1 = FindSource('Clip1')

# find source
streamTracer1 = FindSource('StreamTracer1')

# get active source.
extractBlock1 = GetActiveSource()

# Properties modified on extractBlock1
extractBlock1.BlockIndices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145]

# find source
slice1 = FindSource('Slice1')

# find source
tube1 = FindSource('Tube1')

# find source
streamTracer2 = FindSource('StreamTracer2')

# find source
transform2 = FindSource('Transform2')

# find source
transform1 = FindSource('Transform1')

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
extractSurface1 = FindSource('ExtractSurface1')

# find source
org_backspokestl = FindSource('org_backspoke.stl')

# create a new 'STL Reader'
org_backbrakestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_backbrake.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [957, 491]

# show data in view
org_backbrakestlDisplay = Show(org_backbrakestl, renderView1)
# trace defaults for the display properties.
org_backbrakestlDisplay.ColorArrayName = [None, '']
org_backbrakestlDisplay.GlyphType = 'Arrow'
org_backbrakestlDisplay.SetScaleArray = [None, '']
org_backbrakestlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
org_backbrakestlDisplay.OpacityArray = [None, '']
org_backbrakestlDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# create a new 'Transform'
transform3 = Transform(Input=org_backbrakestl)
transform3.Transform = 'Transform'

# Properties modified on transform3.Transform
transform3.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform3Display = Show(transform3, renderView1)
# trace defaults for the display properties.
transform3Display.ColorArrayName = [None, '']
transform3Display.GlyphType = 'Arrow'
transform3Display.SetScaleArray = [None, '']
transform3Display.ScaleTransferFunction = 'PiecewiseFunction'
transform3Display.OpacityArray = [None, '']
transform3Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(org_backbrakestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform3)

# create a new 'STL Reader'
org_fronttyrestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_fronttyre.stl'])

# show data in view
org_fronttyrestlDisplay = Show(org_fronttyrestl, renderView1)
# trace defaults for the display properties.
org_fronttyrestlDisplay.ColorArrayName = [None, '']
org_fronttyrestlDisplay.GlyphType = 'Arrow'
org_fronttyrestlDisplay.SetScaleArray = [None, '']
org_fronttyrestlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
org_fronttyrestlDisplay.OpacityArray = [None, '']
org_fronttyrestlDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# create a new 'Transform'
transform4 = Transform(Input=org_fronttyrestl)
transform4.Transform = 'Transform'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform4)

# Properties modified on transform4.Transform
transform4.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform4Display = Show(transform4, renderView1)
# trace defaults for the display properties.
transform4Display.ColorArrayName = [None, '']
transform4Display.GlyphType = 'Arrow'
transform4Display.SetScaleArray = [None, '']
transform4Display.ScaleTransferFunction = 'PiecewiseFunction'
transform4Display.OpacityArray = [None, '']
transform4Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(org_fronttyrestl, renderView1)

# change representation type
transform4Display.SetRepresentationType('Surface With Edges')

# create a new 'STL Reader'
org_frontbrakestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_frontbrake.stl'])

# show data in view
org_frontbrakestlDisplay = Show(org_frontbrakestl, renderView1)
# trace defaults for the display properties.
org_frontbrakestlDisplay.ColorArrayName = [None, '']
org_frontbrakestlDisplay.GlyphType = 'Arrow'
org_frontbrakestlDisplay.SetScaleArray = [None, '']
org_frontbrakestlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
org_frontbrakestlDisplay.OpacityArray = [None, '']
org_frontbrakestlDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# create a new 'Transform'
transform5 = Transform(Input=org_frontbrakestl)
transform5.Transform = 'Transform'

# Properties modified on transform5.Transform
transform5.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform5Display = Show(transform5, renderView1)
# trace defaults for the display properties.
transform5Display.ColorArrayName = [None, '']
transform5Display.GlyphType = 'Arrow'
transform5Display.SetScaleArray = [None, '']
transform5Display.ScaleTransferFunction = 'PiecewiseFunction'
transform5Display.OpacityArray = [None, '']
transform5Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(org_frontbrakestl, renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform5)

# create a new 'STL Reader'
org_frontspokestl = STLReader(FileNames=['/Users/keritaylor/LCS/ensightfiles/stls/org_frontspoke.stl'])

# show data in view
org_frontspokestlDisplay = Show(org_frontspokestl, renderView1)
# trace defaults for the display properties.
org_frontspokestlDisplay.ColorArrayName = [None, '']
org_frontspokestlDisplay.GlyphType = 'Arrow'
org_frontspokestlDisplay.SetScaleArray = [None, '']
org_frontspokestlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
org_frontspokestlDisplay.OpacityArray = [None, '']
org_frontspokestlDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# create a new 'Transform'
transform6 = Transform(Input=org_frontspokestl)
transform6.Transform = 'Transform'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform6)

# Properties modified on transform6.Transform
transform6.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform6Display = Show(transform6, renderView1)
# trace defaults for the display properties.
transform6Display.ColorArrayName = [None, '']
transform6Display.GlyphType = 'Arrow'
transform6Display.SetScaleArray = [None, '']
transform6Display.ScaleTransferFunction = 'PiecewiseFunction'
transform6Display.OpacityArray = [None, '']
transform6Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(org_frontspokestl, renderView1)

# change representation type
transform6Display.SetRepresentationType('Surface With Edges')

# set active source
SetActiveSource(transform4)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.42806853190272065, -2.5623437690159188, 0.13444201165052516]
renderView1.CameraFocalPoint = [3.5735227664716778, 0.8493707393718299, 0.7862996303905004]
renderView1.CameraViewUp = [-0.05843826533708185, -0.12079443453480912, 0.9909559393483691]
renderView1.CameraParallelScale = 2.007917110154436

# save screenshot
SaveScreenshot('/Users/keritaylor/LCS/mjtParaScript/forMike.png', magnification=1, quality=100, view=renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.42806853190272065, -2.5623437690159188, 0.13444201165052516]
renderView1.CameraFocalPoint = [3.5735227664716778, 0.8493707393718299, 0.7862996303905004]
renderView1.CameraViewUp = [-0.05843826533708185, -0.12079443453480912, 0.9909559393483691]
renderView1.CameraParallelScale = 2.007917110154436

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).