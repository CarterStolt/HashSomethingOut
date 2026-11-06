# hash something out


def bad_hash_function(string):
    hashSum = 0
    for letterIndex in range(len(string)):
        if letterIndex > 50:
            break
        number = int(string[letterIndex])
        if hashSum % 3 == 0:
            hashSum *= number
        elif hashSum % 3 == 1:
            hashSum += number
        else:
            hashSum -= number
    return sum





with open("MOCK_DATA.csv", "r") as dataFile:
    for line in dataFile.readlines():
        line = line.split(",")
        if line[0] == "movie_title":
            continue
        title = line[0]
        quote = line[8]

sizeOfArray = 15000 # no wasted space!
sizeOfArray = 15013 # prime

hashTable = [None]*sizeOfArray

