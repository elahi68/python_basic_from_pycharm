tuna_map ={}
def get_params(got_the_list):
    for x in got_the_list:
        hash = x.split("=")
        #print (hash[0])
        #print (hash[1])
        tuna_map.update ({hash[0]:hash[1][0:-1]})
    #print (tuna_map)

#Get all the parameters from file here:

list_of_params = ["a=b\n","c=d\n","e=f\n"]	
get_params(list_of_params)
print (tuna_map['a'])
print (tuna_map['e'])
print (tuna_map['c'])
