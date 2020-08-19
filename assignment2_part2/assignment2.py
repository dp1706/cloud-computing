#1 st part


import string 
import random 

my_file = open("randon_txt.txt","w+")

for i in range(100):
   N =random.randint(1, 9)

   res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase ,k=N)) 
   my_file.write(res)
   my_file.write("\n")
   #print(str(res)+"\t") 

my_file.close()




#2nd part 

#2 part 

def readFile(filename):

  file_data=filename.read()
  return file_data

def wordCount(count_data) :
  count=0
  words=count_data.split("\n")

  for i in words:
    if i:
     count=count+1
  print("\ntotal word in the file is: "+ str(count))
  return count


def topTenWords(count_data):
    
    count=0
    words=count_data.split("\n")

    for i in range(10):
      print(words[i])

def main():

 filename= open("randon_txt.txt", "r")
 contents= readFile(filename)
 wordCountDict= wordCount(contents)
 topTenWords(contents)



if __name__ == "__main__":
  main()
