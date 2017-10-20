file1=open("Book1.txt" , 'r')
file2=open("Book2.txt" , 'r')
file3=open("Book3.txt" , 'r')
#read Book1 , book2 , book3
read1=file1.read()
readword1=read1.split()
read2=file2.read()
readword2=read2.split()
read3=file3.read()
readword3=read3.split()

maxlen=0
def findA(readword)
 for word in  readword:
  if len(word)>maxlen:
    maxlen=len(word)
    maxlength_world=word
  else:
    pass
 return maxlength_world

max_word=find(readword1)

def findB(readword)
 for word in  readword:
  if len(word)>len(max_world):
    max_word=word
  else:
   pass
 return max_world

max_max_word=findB(readword2)

def findc(readword):
 for word in  readword:
  if len(word)>len(max_max_word):
    max_max_word=word
  else:
   pass
 return max_max_word

Maximumlengthword=findc(readword3)
print(maximumlengthword)
