def calcNumPeach(nDays):
    if nDays == 1:
        return 1
    
    return (calcNumPeach(nDays-1) + 1) * 2

def main():
    try:
        nDays = int(input("Enter the number of days a monkey eats peaches: "))
    
    except ValueError:
        print("Invalid input")
    
    else:
        if nDays > 0:
            print(f"n = {nDays}; initial_peaches = {calcNumPeach(nDays)}")
        
        else:
            print("Invalid input")
            
if __name__ == "__main__":
    main()