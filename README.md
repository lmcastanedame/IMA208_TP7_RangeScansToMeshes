## IMA208 TP7 Range Scans to Meshes

### Repository Contents
- **Bimba.xyz**: 3D scan data for the "Bimba" model.
- **Bunny.xyz**: 3D scan data for the "Bunny" model.
- **CMakeLists.txt**: CMake configuration file.
- **IMA208___Range_Scans_to_Meshes.pdf**: Project documentation.
- **Instructions.txt**: Instructions for the assignment.
- **SimpleFiltering_CASTANEDA-TORRES.py**: Python script for filtering the scan data.
- **output_bimba_CASTANEDA-TORRES.stl**: Generated STL file for the Bimba model.
- **output_bunny_CASTANEDA-TORRES.stl**: Generated STL file for the Bunny model.
- **reconstruct.cpp**: C++ source code for reconstructing the mesh.

### Getting Started
#### Prerequisites
- Python 3.x
- C++ compiler
- CMake

#### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/lmcastanedame/IMA208_TP7_RangeScansToMeshes.git
   ```
2. Navigate to the repository directory:
   ```sh
   cd IMA208_TP7_RangeScansToMeshes
   ```

### Usage
1. Build the C++ code using CMake:
   ```sh
   mkdir build
   cd build
   cmake ..
   make
   ```
2. Run the Python script for filtering:
   ```sh
   python SimpleFiltering_CASTANEDA-TORRES.py
   ```
3. Execute the compiled C++ program for reconstruction:
   ```sh
   ./reconstruct
   ```
