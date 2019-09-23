import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1.sort()
duplicates = []

# THIS IS THE STRETCH SOLUTION
for name in names_2:
    names_1_sub = names_1
    done = False
    while not done:
        midpoint = len(names_1_sub) // 2
        if names_1_sub[midpoint] == name:
            duplicates.append(name)
            done = True
        elif names_1_sub[midpoint] > name:
            if names_1_sub[0] == names_1_sub[midpoint]:
                done = True
            else:
                names_1_sub = names_1_sub[:midpoint]
        else:
            if names_1_sub[-1] == names_1_sub[midpoint]:
                done = True
            else:
                names_1_sub = names_1_sub[midpoint + 1:]

            


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

