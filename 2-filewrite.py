# Write mode of file which replace the entire content

# file = open('arjun.txt', 'w')

# file.write("I am not working now...\n")

#-------------------------------------------------------

# Now Append mode 

file = open('arjun.txt', 'a')
file.write("\n I live in india...\n")

file = open('arjun.txt', 'r')
content = file.read()
print(content)

file.close()



