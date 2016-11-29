import os
import sys
from  paraview.simple  import *
from  paraview.servermanager  import *
from fn import * 



#volume class
class	reflect_geom(object):
	def __init__(self,vol,plane):
		self.master = Reflect(Input=vol.master)
		self.master.Plane = plane
		self.master.CopyInput = 0
		self.type = vol.type
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)

class	mirror_geom(object):
	def __init__(self,vol,plane):
		self.master = Reflect(Input=vol.master)
		self.master.Plane = plane
		self.master.CopyInput = 1
		if type(vol).__name__ != 'get_stl':
			self.type = vol.type
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)


class	add_surface_points_vector(object):
	def __init__(self,arrayname,vol,scalar_x,scalar_y,scalar_z):

        	if vol.type != "POINTS":
                	cellDatatoPointData1 = CellDatatoPointData(Input=vol.master)
                	input_source=cellDatatoPointData1

        	self.master = Calculator(Input=cellDatatoPointData1)
        	self.master.ResultArrayName = arrayname
        	self.master.Function = scalar_x + '*iHat+' + scalar_y + '*jHat+' + scalar_z +  '*kHat'
		self.type = vol.type
		self.r_view = GetActiveViewOrCreate('RenderView')

class	get_stl(object):
	def __init__(self,path_to_stl_file,scale_x,scale_y,scale_z,colour):
		stl = STLReader(FileNames=[path_to_stl_file]) 
		self.master = Transform(Input=stl)
		self.master.Transform = 'Transform'
		self.master.Transform.Scale = [scale_x, scale_y, scale_z]
		Hide3DWidgets(proxy=self.master)
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if colour != '':
			self.Display.DiffuseColor = colour
			ColorBy(self.Display, None)

class	get_obj_file(object):
	def __init__(self,path_to_obj_file,scale_x,scale_y,scale_z,shift_x,shift_y,shift_z,colour):
		obj_file = WavefrontOBJReader(FileName = path_to_obj_file)
		self.master = Transform(Input=obj_file)
		self.master.Transform = 'Transform'
		self.master.Transform.Scale = [scale_x, scale_y, scale_z]
		self.master.Transform.Translate = [shift_x, shift_y, shift_z]
		Hide3DWidgets(proxy=self.master)
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if colour != '':
			self.Display.DiffuseColor = colour



class   Volume_vtu(object):
	def __init__(self,type,path_to_case_file,array_list):
		ghosts_gone = XMLPartitionedUnstructuredGridReader(FileName=[path_to_case_file])
		self.master = D3(Input=ghosts_gone)
		if type == "cell":
			self.CellArrayStatus = array_list
			self.type='CELLS'
		else:
			self.PointArrayStatus = array_list
			self.type='POINTS'
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)

	def vol_colour(self,scalar):
		ColorBy(self.Display, (self.type, scalar))


class Volume_ensight(object):
	def __init__(self,type,path_to_case_file,array_list):
		self.master = EnSightReader(CaseFileName = path_to_case_file)
		if type == "cell":
			self.master.CellArrays = array_list
			self.type='CELLS'
		else:
			self.master.PointArrays = array_list
			self.type='POINTS'
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)

	def vol_colour(self,scalar):
		ColorBy(self.Display, (self.type, scalar))

class Volume_ensight_points(object):
        def __init__(self,type,path_to_case_file,array_list):
                input_case = EnSightReader(CaseFileName = path_to_case_file)
                if type == "cell":
                	self.master = CellDatatoPointData(Input=input_case)
		else:
			self.master = input_case
                self.PointArrays = array_list
                self.type='POINTS'
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)

        def vol_colour(self,scalar):
                ColorBy(self.Display, (self.type, scalar))



class Surface(object):
	def __init__(self,vol,surfaces):
		self.master = ExtractBlock(Input=vol.master)
		self.master.BlockIndices = surfaces
		self.type = vol.type 
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)

	def sur_colour(self,scalar):
		self.Display.SetScalarBarVisibility(self.r_view, True)
		ColorBy(self.Display, (self.type, scalar))


class    pseudo_scalar(object):
	def __init__(self,scalar,lower,upper):
        	self.LUT = GetColorTransferFunction(scalar)
        	self.PWF = GetOpacityTransferFunction(scalar)
        	self.LUT.ApplyPreset('Blue to Red Rainbow', True)
        	self.LUT.RescaleTransferFunction(lower,upper)
        	self.PWF.RescaleTransferFunction(lower,upper)



class	make_stream_set(object): 	
	def __init__(self,vol,scalar,x1,y1,z1,x2,y2,z2,resolute,num_steps,delta,direction,ball_req,ball_size,num_balls):

                self.stream_list=[]

                for i in range (0, num_steps ):
                	if direction=='x':
				x1=x1 + delta
				x2=x2 + delta
                	if direction=='y':
				y1=y1 + delta
				y2=y2 + delta
                	if direction=='z':
				z1=z1 + delta
				z2=z2 + delta

                        component='num' + str(i)
                        component=line_stream(vol,scalar,x1,y1,z1,x2,y2,z2,resolute)
			ball_maker=component.master		

			if ball_req=='y':
				component.ball=[]
				for j in range (0, num_balls):
					ball_component='ball' + str(j)
					ball_component=make_ball(ball_maker,ball_size,scalar)
					component.ball.append(ball_component)

                        self.stream_list.append(component)



class   make_ball(object):
        def __init__(self,stream_layer,glyph_radius,scalar):
       	        self.master = Contour(Input=stream_layer)
                self.master.ContourBy = ['POINTS', 'IntegrationTime']
	        self.master.Isosurfaces = [0.0]
                self.master.PointMergeMethod = 'Uniform Binning'
		self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = Show(self.master, self.r_view)
                self.Display.GlyphType = 'Sphere'
                self.Display.GlyphType.Radius = glyph_radius
                ColorBy(self.Display, ('POINTS', scalar))
                self.Display.SetRepresentationType('3D Glyphs')
                self.Display.SetScaleArray = [None, 'AngularVelocity']
                self.Display.OpacityArray = [None, 'AngularVelocity']


class	line_stream(object): 	
	def __init__(self,vol,scalar,x1,y1,z1,x2,y2,z2,resolute):
		self.master = StreamTracer(Input=vol.master,
			SeedType='High Resolution Line Source')
		self.master.Vectors = [vol.type, scalar]
		self.master.IntegrationDirection = 'FORWARD'
		self.master.SeedType.Point1 = [x1,y1,z1]
		self.master.SeedType.Point2 = [x2,y2,z2]
		self.master.SeedType.Resolution = resolute
		self.r_view = GetActiveViewOrCreate('RenderView')
		Hide3DWidgets(proxy=self.master)
		self.Display = GetDisplayProperties(self.master, view=self.r_view)
		ColorBy(self.Display, ('POINTS', scalar))

	def make_tube(self,rad, opaque):
		self.tube = Tube(Input=self.master)
		self.tube.Scalars = ['POINTS', 'AngularVelocity']
		self.tube.Vectors = ['POINTS', 'Normals']
		self.tube.Radius = rad
		Hide(self.master, self.r_view)
		self.Display = GetDisplayProperties(self.tube, view=self.r_view)
		self.Display.Opacity = opaque


class	plane_slice(object):
	def __init__(self,vol,x1,y1,z1,norm,scalar):
		x2=0.0
		y2=0.0
		z2=0.0
		if norm == 'x':	
			x2=1.0
		if norm == 'y':	
			y2=1.0
		if norm == 'z':	
			z2=1.0
        	if vol.type != "POINTS":
                	cellDatatoPointData1 = CellDatatoPointData(Input=vol.master)
                	input_source=cellDatatoPointData1
			self.type="POINTS"
		else:
			input_source=vol.master
			self.type=vol.type
		self.master = Slice(Input=input_source)
		self.master.SliceType = 'Plane'
		self.master.SliceOffsetValues = [0.0]
		self.master.SliceType.Origin = [x1,y1,z1]
		self.master.SliceType.Normal = [x2,y2,z2]
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)
		ColorBy(self.Display, (self.type, scalar))
		Hide3DWidgets(proxy=self.master)


class	cut_od(object):
	def __init__(self,vol,scalar,y_sign):
		extractSurface1 = ExtractSurface(Input=vol.master)
		self.master = Clip(Input=extractSurface1)
		self.master.ClipType = 'Box'
		self.master.InsideOut = 1
		bounds_range=vol.master.GetDataInformation().GetBounds()
		print 'bounds',bounds_range
		self.master.ClipType.Bounds = bounds_range
		delta=.001
		if y_sign == 'negative':
			y_delta=delta * -1.0
		else:
			y_delta=delta
		self.master.ClipType.Position = [delta, y_delta, delta]
		self.master.ClipType.Scale = [0.98, 0.98, 0.98]
		self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		Hide(extractSurface1, self.r_view)
		Hide3DWidgets(proxy=self.master)
		ColorBy(self.Display, (vol.type, scalar))	

class   get_road(object):
        def __init__(self,vol,scalar,y_sign):
                extractSurface1 = ExtractSurface(Input=vol.master)
                self.master = Clip(Input=extractSurface1)
                self.master.ClipType = 'Box'
                self.master.InsideOut = 0
                bounds_range=vol.master.GetDataInformation().GetBounds()
                print 'bounds',bounds_range
                self.master.ClipType.Bounds = bounds_range
                delta=.001
		if y_sign == 'negative':
                	self.master.ClipType.Position = [-delta,delta,delta]
			print y_sign
		else:
                	self.master.ClipType.Position = [-delta,-delta,delta]
                self.master.ClipType.Scale = [1.1,  1.1 , 1.0 ]
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
                Hide(extractSurface1, self.r_view)
                Hide3DWidgets(proxy=self.master)
                ColorBy(self.Display, (vol.type, scalar))







class   cut_stl_box(object):
        def __init__(self,component,pos_x,pos_y,pos_z,scale_x,scale_y,scale_z,inside,colour):
                self.master = Clip(Input=component.master)
                self.master.ClipType = 'Box'
                self.master.InsideOut = inside
                bounds_range=component.master.GetDataInformation().GetBounds()
                self.master.ClipType.Bounds = bounds_range
                self.master.ClipType.Position = [pos_x,pos_y,pos_z]
                self.master.ClipType.Scale = [scale_x,scale_y,scale_z]
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
                Hide(component.master, self.r_view)
                Hide3DWidgets(proxy=self.master)
                if colour != '':
                        self.Display.DiffuseColor = colour

class 	join_stl(object):
	def __init__(self,component1,component2,colour):
		self.master=GroupDatasets(Input=[component1.master,component2.master])
		Hide(component1.master,component1.r_view)
		Hide(component2.master,component2.r_view)
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
                if colour != '':
                        self.Display.DiffuseColor = colour
		





class	surface_stream(object):
	def __init__(self,vol,surf,vector,orient,scalar):
		(centre,radius)=get_centre_radius(surf,orient)
		print centre,radius
	
		input_source=vol.master

		self.master = StreamTracer(Input=surf.master,
		    SeedType='Point Source')
		self.master.Vectors = ['POINTS', vector ]
		self.master.MaximumStreamlineLength = 1.2011880576610565
		print 'self.master.Vectors',self.master.Vectors

		self.master.SeedType.Center = centre 
		self.master.SeedType.Radius = radius 

		self.master.SurfaceStreamlines = 1

		self.master.SeedType.NumberOfPoints = 20000

		self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		ColorBy(self.Display, ('POINTS', scalar))	



class	make_rotate_set(object):
	def __init__(self,donor,origin_x,origin_y,origin_z,axis,rot_value,num_steps):
		if axis=='x':
			x_orient=rot_value
			y_orient=0.0
			z_orient=0.0
		if axis=='y':
			y_orient=rot_value
			x_orient=0.0
			z_orient=0.0
		if axis=='z':
			z_orient=rot_value
			y_orient=0.0
			x_orient=0.0

		self.rotlist=[]
		Hide(donor.master,donor.r_view)

		for i in range (0, num_steps ):
			component='num' + str(i)
			component=copy_rotate_part(donor,origin_x,origin_y,origin_z,axis,rot_value,i,x_orient,y_orient,z_orient)
			self.rotlist.append(component)

class	copy_rotate_part(object):
	def __init__(self,donor,origin_x,origin_y,origin_z,axis,rot_value,i,x_orient,y_orient,z_orient):
		self.master = Shrink(Input = donor.master)
		self.master.ShrinkFactor = 1.0
		self.r_view = GetActiveViewOrCreate('RenderView')
               	self.Display = GetDisplayProperties(self.master, view=self.r_view)
		self.Display.DiffuseColor = donor.Display.DiffuseColor
		self.Display.Orientation=[ x_orient * (i), y_orient * (i), z_orient * (i)]
		self.Display.Origin = [origin_x,origin_y,origin_z]	
		ColorBy(self.Display, None)


class	make_contour(object):
	def __init__(self,vol,scalar,level,opaque):
		self.master = Contour(Input=vol.master)
		self.master.ContourBy = ['POINTS', scalar ]
		self.master.Isosurfaces = [ level ]
		self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		self.Display.Opacity = opaque


class	make_plane(object):
	def __init__(self,origin_x,origin_y,origin_z,pt1_x,pt1_y,pt1_z,pt2_x,pt2_y,pt2_z,colour,opaque):
		self.master = Plane()
		self.master.Origin = [origin_x,origin_y,origin_z]
		self.master.Point1 = [pt1_x,pt1_y,pt1_z]
		self.master.Point2 =  [pt2_x,pt2_y,pt2_z]
		self.r_view = GetActiveViewOrCreate('RenderView')
		self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if colour != '':
			self.Display.DiffuseColor = colour
		self.Display.Opacity = opaque


class	make_plane_clip(object):
	def __init__(self,component,origin_x,origin_y,origin_z,orient_x,orient_y,orient_z,inside,colour):
		self.master=Clip(Input=component.master)
		self.master.ClipType='Plane'
		self.master.ClipType.Origin = [origin_x,origin_y,origin_z]
		self.master.ClipType.Normal = [orient_x,orient_y,orient_z]
		self.master.InsideOut=inside
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if colour != '':
			self.Display.DiffuseColor = colour
#			ColorBy(self.Display, None)
		Hide3DWidgets(proxy=self.master)


class	make_cp(object):
	def __init__(self,vol,pressure_scalar,u_inf,data_type):
		self.master=Calculator(Input=vol.master)
		self.master.ResultArrayName = 'Cp'
		self.type = vol.type
		if data_type == "cell":
			self.master.AttributeMode = 'Cell Data'
		else:
			self.master.AttributeMode = 'Point Data'
		string=str(pressure_scalar)+'/(0.5*1.2*'+str(u_inf)+'*'+str(u_inf)+')'
		print 'making Cp variable',string
#		self.master.Function = 'p/(0.5 * 1.2 * 20 * 20)'
		self.master.Function = string
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if data_type == "cell":
			ColorBy(self.Display, ('CELLS', 'Cp'))	
		else:
			ColorBy(self.Display, ('POINTS', 'Cp'))	

class	make_cp0(object):
	def __init__(self,vol,pressure_scalar,velocity_vector,u_inf,data_type):
		self.master=Calculator(Input=vol.master)
		self.master.ResultArrayName = 'Cp0'
		self.type = vol.type
		if data_type == "cell":
			self.master.AttributeMode = 'Cell Data'
		else:
			self.master.AttributeMode = 'Point Data'
		string='('+str(pressure_scalar)+'+(0.5*1.2*mag('+str(velocity_vector)+')^2))/(0.5*1.2*'+str(u_inf)+'*'+str(u_inf)+')'
		print 'making Cp0 variable',string
		self.master.Function = string
                self.r_view = GetActiveViewOrCreate('RenderView')
                self.Display = GetDisplayProperties(self.master, view=self.r_view)
		if data_type == "cell":
			ColorBy(self.Display, ('CELLS', 'Cp0'))	
		else:
			ColorBy(self.Display, ('POINTS', 'Cp0'))	



