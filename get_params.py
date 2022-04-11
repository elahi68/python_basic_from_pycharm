#imports
import re
import os
#Globals
tuna_map ={}
debug = 1
logMeFile = ""

def trim(got_string):
    got_string = re.sub(r"\s+","",got_string)
    got_string = re.sub(r"\s+$","",got_string)
    return got_string
    #got_string =~s/\s+\\
    #got_string =~s/\s+$//;
    
    
def get_params(got_the_list):
    for x in got_the_list:
        hash = x.split("=")
        #print (hash[0])
        #print (hash[1])
        hash[0] = trim(hash[0])
        hash[1] = trim(hash[1])
        #print (hash[0])
        #print (hash[1])
        tuna_map.update ({hash[0]:hash[1]})

def logme(log_string,f):
    if debug == 1:
        print (log_string, file=f)
    else:
        print (log_string)


# Get all the parameters from file here:
list_of_params = ["logFile=logs.txt\n", "c=d\n", "e=f\n"]
get_params(list_of_params)
logMeFile = tuna_map["logFile"]
print(logMeFile)
if debug == 1:
   try:
       fd = open(logMeFile, "a")
       logme("Hello into logme file elahi.txt", fd)
   except IOError:
       print ("Error in opening logfile exiting")
       exit(0)
logme(os.path.basename(__file__), fd)



