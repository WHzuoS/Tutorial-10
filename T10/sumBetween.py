def sumBetween(start,end):
    if start == end:
        return start 
    
    if start < end:
        return 0
    
    return start + end + sumBetween(start-1,end+1)

def main():
    while True:
        try: 
            start, end = input("Enter two integers seperated by \",\": ").split(",")
            start = int(start)
            end = int(end)
        
        except ValueError:
            print("Invalid input")
        
        else:
            if start >= end:
                print(sumBetween(start, end))
                break
            
            else:
                print("Invalid input")
    
if __name__ == "__main__":    
    main()