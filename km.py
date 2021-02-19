
def main():
    km = float(input("Enter the distances in km:  "))
    miles = convert(km)
    print(miles)

    
def convert(km):
    miles = km * 0.6214
    return miles
main()
