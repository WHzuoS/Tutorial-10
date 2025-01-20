def readData(filename, n):
    list = []
    counter = 1
    
    with open(filename, "r") as file:
        for line in file:
            if counter % n == 0:
                list.append(line.strip())
            counter += 1
            
    return list
    
def ageLessThan(filename, n):
    list = []
    
    with open(filename, "r") as file:
        for line in file:
            words = line.split(", ")
            
            if int(words[1]) < n:
                list.append(words[0])

    return list
    
def main():
    print(readData("sample_data.txt", 5)) # call readData()
    print(ageLessThan("sample_data.txt", 4)) # call ageLessThan()
    
if __name__ == "__main__":
    main()