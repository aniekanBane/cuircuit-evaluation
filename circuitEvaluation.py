import numpy as np
# promt user inputs
print("\nEnter resistor values in ohms")
R1 = float(input("Enter R1: "))
R2 = float(input("Enter R2: "))
R3 = float(input("Enter R3: "))
Ry = float(input("Enter Ry: "))
Rz = float(input("Enter Rz: "))
print("\nEnter voltage values in volts")
V1 = float(input("Enter V1: "))
V2 = float(input("Enter V2: "))

def CircuitEval(R1,R2,R3,Ry,Rz,V1,V2):
    """Function to calculate the unknown current and voltage parameters in a simple circuit"""

    print("calculating Rx...")
    Rx = R1 + ((R2 * R3) / (R2 + R3))
    # left hand loop
    A1 = Rx + Rz
    B1 = Rz
    C1 = V1
    # right hand loop
    A2 = Rz
    B2 = Rz + Ry
    C2 = V2
    # established matrices
    m = np.array([[A1, B1],[A2, B2]])
    Dx = np.array([[C1, B1],[C2, B2]])
    Dy = np.array([[A1, C1],[A2, C2]])
    # determinants
    D = np.linalg.det(m) 
    x = np.linalg.det(Dx)
    y = np.linalg.det(Dy)
    
    print("determining Parameters...")
    # currents
    Ix = x / D
    Iy = y / D
    Iz = Ix + Iy
    # output voltage Vz
    Vz = Rz * Iz
    
    # display results
    print("\nResults:")
    print("Rx = {}Ω\nIx = {}A\nIy = {}A\nIz = {}A\nVz = {}V".format(Rx, Ix, abs(Iy), Iz, Vz))

# call function
CircuitEval(R1,R2,R3,Ry,Rz,V1,V2)
