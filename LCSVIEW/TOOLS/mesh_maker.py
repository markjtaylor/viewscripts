from firedrake import *

# Minimum and maximum values in each direction
x_range = [-13.0, 17.0]
y_range = [-2.5,  0.0]
z_range = [0.0,   5.0]

# Number of divisions per unit length in each direction
resolution_x = 1
resolution_y = 1
resolution_z = 1

# Length of the domain in each direction
Lx = x_range[1] - x_range[0]
Ly = y_range[1] - y_range[0]
Lz = z_range[1] - z_range[0]

# Number of divisions in total in each direction
Nx = int(Lx * resolution_x)
Ny = int(Ly * resolution_y)
Nz = int(Lz * resolution_z)

# Number of cells in the domain
tets_per_cube = 6
number_elements = Nx * Ny * Nz * tets_per_cube

# Make the mesh
mesh = BoxMesh(Nx, Ny, Nz, Lx, Ly, Lz)

# Shift from the origin to the correct location
x = mesh.coordinates.vector().dat.data[:]
x[:,0] += x_range[0]
x[:,1] += y_range[0]
x[:,2] += z_range[0] 

# Create the function and write it out
V = FunctionSpace(mesh, 'CG', 1)
u = Function(V, name='new_mesh_function')
File('mesh_function.pvd').write(u)













































print '\nCongratulations, something has worked.\n'
