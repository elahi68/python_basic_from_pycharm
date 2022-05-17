
#stmt = 'select SUBSTR(data_Value,1,1) from ni_ud_dn where dn=\'{}\' and ud_fk=7;select data_value from ni_ud_dn where dn=\'{}\' and ud_fk =4;'
#stmt = 'SELECT vanity_type || chr(10) || price_category FROM foss_msisdn_pool where msisdn_no={};'
#stmt = 'select dn,data_value from ni_ud_dn where  dn in (\'{}\') and (ud_fk=7 or ud_fk=4);'
#dn=12345
#tmp = stmt2.format(dn)

#stmt = 'select * from NI_NAMED_GROUP_RANGE where start_value = \'{}\' and end_value=\'{}\';'
stmt = 'INSERT INTO ND_OWNERSHIP VALUES(nd_ownership_seq.NEXTVAL,17,1,1,{},{},{},NULL,SYSDATE,NULL,1,NULL);'

#print (tmp)

with open('nd_list.txt') as file:
    lines = [line.rstrip() for line in file]
file.close()
i=0
print('spool \'ownership_cross_verify.txt\';')
for line in lines:
    i += 1
    words = line.split(',')
    len2 = int(words[2])
    len = int(words[2])-4
    start_val = words[0][0:len]
    end_val = words[1][0:len]
    #start_val = words[0]
    #end_val = words[1]
    #len = words[2]

    tmp = stmt.format(start_val,end_val,len)
    tmp2='{},{},{}'
    sl = tmp2.format(len2,start_val,end_val)
    #print(i,' : ',sl);
    #print (i,' : ',s1)
    print (sl)
print('EXIT;')
