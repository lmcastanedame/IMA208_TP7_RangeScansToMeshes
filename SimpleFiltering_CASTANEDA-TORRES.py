# -*- coding: utf-8 -*-
"""circum_sphere

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YncydsXf5p5nAbBU8vn3qlouo82Y8f18
"""

import numpy as np
from scipy.spatial import Delaunay
from stl import mesh
from scipy.spatial import KDTree

# Open the file and read the vertices as strings
with open("bunny.xyz", "r") as f:
    vertex_strings = f.readlines()

# Convert the vertex strings to a NumPy array of shape (N, 3)
points3D = np.zeros((len(vertex_strings), 3))
for i, vertex_str in enumerate(vertex_strings):
    vertex_arr = [float(coord) for coord in vertex_str.strip().split()]
    points3D[i] = vertex_arr

tri = Delaunay(points3D)

# Each tetrahedron has 4 triangular faces
num_triangles = len(tri.simplices) * 4
stl_mesh = mesh.Mesh(np.zeros(num_triangles, dtype=mesh.Mesh.dtype))

radii = []
for tetra in tri.simplices:
    for k in range(4):  # There are 4 vertices in a tetrahedron, hence 4 triangles
        indices = [tetra[(k+1) % 4], tetra[(k+2) % 4], tetra[(k+3) % 4]]
        triangle = points3D[indices]
        
        # Calculate the distance between the 3 points
        a = np.linalg.norm(triangle[0] - triangle[1])
        b = np.linalg.norm(triangle[1] - triangle[2])
        c = np.linalg.norm(triangle[2] - triangle[0])
        
        # Calculate radius of circumcircles
        radius = (a * b * c) / np.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))

        # Save all the radius of the circumcircles
        radii.append(radius)

alpha = 1/(sum(radii) / len(radii)) # Statistical approach to find the alpha value
tetra_index = 0
for tetra in tri.simplices:
    for k in range(4):  # There are 4 vertices in a tetrahedron, hence 4 triangles
        indices = [tetra[(k+1) % 4], tetra[(k+2) % 4], tetra[(k+3) % 4]]
        triangle = points3D[indices]
        
        # Calculate the distance between the 3 points
        a = np.linalg.norm(triangle[0] - triangle[1])
        b = np.linalg.norm(triangle[1] - triangle[2])
        c = np.linalg.norm(triangle[2] - triangle[0])
        
        # Calculate radius of circumcircles
        radius = (a * b * c) / np.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
        
        if radius <= 1/alpha:
            stl_mesh.vectors[tetra_index] = triangle
            tetra_index += 1

# Write the mesh to file "output.stl"
stl_mesh.save('output_bunny.stl')

### Adapted for Bimba.xyz

# Load the point cloud data
with open("bimba.xyz", "r") as f:
    vertex_strings = f.readlines()
points3D = np.array([list(map(float, v.strip().split())) for v in vertex_strings])

# Create a KDTree for efficient nearest neighbor search
tree = KDTree(points3D)

# Calculate the local density for each point
k = 5  # number of nearest neighbors to consider
distances, _ = tree.query(points3D, k=k+1)  # k+1 because the point itself is included
local_density = distances[:, 1:].mean(axis=1)  # ignore the 0th distance (point to itself)

# Perform Delaunay triangulation
tri = Delaunay(points3D)

num_triangles = len(tri.simplices) * 4
stl_mesh = mesh.Mesh(np.zeros(num_triangles, dtype=mesh.Mesh.dtype))

tetra_index = 0
for tetra in tri.simplices:
    # Calculate the local alpha for this tetrahedron
    local_alpha = 1/ ( local_density[tetra].mean() )
    # print(local_alpha)
    
    for k in range(4):  # Each tetrahedron has 4 triangular faces
        indices = [tetra[(k+1) % 4], tetra[(k+2) % 4], tetra[(k+3) % 4]]
        triangle = points3D[indices]
        
        # Calculate the distance between the 3 points
        a = np.linalg.norm(triangle[0] - triangle[1])
        b = np.linalg.norm(triangle[1] - triangle[2])
        c = np.linalg.norm(triangle[2] - triangle[0])
        
        # Calculate radius of circumcircles
        radius = (a * b * c) / np.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
        
        if radius <= 1/local_alpha:
            stl_mesh.vectors[tetra_index] = triangle
            tetra_index += 1

# Write the mesh to file "output.stl"
stl_mesh.save('output_bimba.stl')
