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

def hash_function_two(string):
    hashSum = 0
    for letter in string:
        number = ord(letter)
        if hashSum % 3 == 0:
            hashSum += number*number
        elif hashSum % 3 == 1:
            hashSum += number*number*number
        else:
            hashSum += number*number*number*number
    return hashSum*31

def hash_function_three_linked(string):
    prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    hashProduct = 1
    prime_list_len = len(prime_number_list)
    for letter in string:
        primeIndex = ord(letter)%prime_list_len
        hashProduct =+ hashProduct*prime_number_list[primeIndex]
    return hashProduct

def hash_function_four_linked(string):
    prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    hashProduct = 1
    for number in prime_number_list:
        if len(string) > number:
            hashProduct += ord(string[number]) * number + 300
        else:
            hashProduct = hashProduct*number
        if hashProduct % number > number/2:
            hashProduct += (hashProduct % 300 * number)
    return hashProduct

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



def add_to_hash_table_linked_list(index, data):
    if hashTable[index] == None:
        hashTable[index] = [data]
        return True, 0
    else:
        hashTable[index].append(data)
        return True, 1

# I looked up how to make it so that it doesn't seperate at every comma and Google AI gave me this
    ### AI CODE STARTS HERE ###
with open('MOCK_DATA.csv', mode='r', newline='', encoding='utf-8') as file:
    # skipinitialspace=True handles spaces after commas like: "Data 1", "Data 2, with comma"
    reader = csv.reader(file, skipinitialspace=True)
    ### AI CODE ENDS HERE ###
    startTime = time.time()
    
    for row in reader:
        movieToAdd = create_movie(row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        key = hash_function_four_linked(movieToAdd["title"])
        key = key % sizeOfArray
        successfulAddition, numberOfNewCollisions = add_to_hash_table_linked_list(key, movieToAdd)
        numberOfCollisions += numberOfNewCollisions
        if successfulAddition & numberOfNewCollisions == 0:
            currentUnusedBuckets -= 1
        print(numberOfNewCollisions)
        numberOfNewCollisions = 0
endTime = time.time()
print("Unused Buckets:", currentUnusedBuckets)
print("Number of Collisions:", numberOfCollisions)
print("Amount of time taken:", endTime-startTime)
