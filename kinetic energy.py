def main():
    m = float(input("Enter the mass:  "))
    v = float(input("Enter the velocity:  "))
    print(kinetic_energy(m,v))




def kinetic_energy(m,v):
    KE = (1/2)*m*(v**2)
    return KE


main()
