file=open("running-config.cfg" , 'r')
config_file=file.read()
list=config_file.split()

File_con=[]
for word in list:
 if word!='172.82.255.1':
   File_con.appand(word)
 else
   word=192.168.121.254
   File_con.appand(word)

print(File_con)


