def main():
    mass = float(input("m: ")) 
    c = 300_000_000  
    energy = mass * c ** 2
    print(f"E: {energy:.0f}") 

if __name__ == "__main__":
    main()
