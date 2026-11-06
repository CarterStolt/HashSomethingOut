# hash something out
import csv
import time

sizeOfArray = 15000 # no wasted space!
sizeOfArray = 15013 # prime

currentUnusedBuckets = sizeOfArray
numberOfCollisions = 0

hashTable = [None]*sizeOfArray


def hash_function(string):
    sumOfString = 0
    for letter in string:
        sumOfString += ord(letter) # found ord() on stackoverflow.com
    return sumOfString

def create_movie(movie_title,genre,release_date,director,box_office_revenue,rating,duration_minutes,production_company,quote):
    movie = {
        "title":movie_title,
        "genre":genre,
        "release date":release_date,
        "director":director,
        "box office revenue":box_office_revenue,
        "rating":rating,
        "length":duration_minutes,
        "production_company":production_company,
        "quote":quote
    }
    return movie

def add_to_hash_table_linear_probing(index, data):
    graveyard = "___~~~___"
    if hashTable[index] == None or hashTable[index] == graveyard:
        hashTable[index] = data
        return True, 0
    else:
        origanal_index = index
        collisionNumber = 0
        foundEmpty = False
        while not foundEmpty:
            index += 1
            collisionNumber += 1
            if index == origanal_index: # did we loop?
                return False, collisionNumber
            if index == sizeOfArray: # is the index out of the array?
                index = 0
            if hashTable[index] == None or hashTable[index] == graveyard:
                hashTable[index] = data
                foundEmpty = True
                return True, collisionNumber




# I looked up how to make it so that it doesn't seperate at every comma and Google AI gave me this
    ### AI CODE STARTS HERE ###
with open('MOCK_DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    # skipinitialspace=True handles spaces after commas like: "Data 1", "Data 2, with comma"
    reader = csv.reader(file, skipinitialspace=True)
    ### AI CODE ENDS HERE ###
    startTime = time.time()
    
    for row in reader:
        movieToAdd = create_movie(row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        key = hash_function(movieToAdd["title"])
        key = key % sizeOfArray
        successfulAddition, numberOfNewCollisions = add_to_hash_table_linear_probing(key, movieToAdd)
        if successfulAddition:
            currentUnusedBuckets -= 1
        numberOfCollisions += numberOfNewCollisions
endTime = time.time()
print("Unused Buckets:", currentUnusedBuckets)
print("Number of Collisions:", numberOfCollisions)
print("Amount of time taken:", endTime-startTime)
