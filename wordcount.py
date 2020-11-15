#-------------------------------------------------
# Name    : Mrunal Munot
# Program : Number of Word Counting
#-------------------------------------------------

#Taking Input of file name with extension
file_name = input("Enter file name: ") #word.txt
#Decared to store words
words = []   
                      
#Opening file
with open(file_name, 'r') as f:
	for line in f:
		#Stripping space from left and right of line
		line=line.strip()
		#Spitting by space and storing in w 
		for w in line.split(" "):
			#Appending words to list words
			words.append(w.lower())#Making each word lower case


print("Total number of words:",len(words))
#print("Words :",words)
twords=tuple(words)
swords=set(twords)
#print("Afer making Set :",swords)
print("Total number of unique words : ",len(swords))