
#stmt = 'select SUBSTR(data_Value,1,1) from ni_ud_dn where dn=\'{}\' and ud_fk=7;select data_value from ni_ud_dn where dn=\'{}\' and ud_fk =4;'
stmt = 'SELECT vanity_type || chr(10) || price_category FROM foss_msisdn_pool where msisdn_no={};'
#dn=12345
#tmp = stmt2.format(dn)

#print (tmp)

with open('dn_list.txt') as file:
    lines = [line.rstrip() for line in file]
file.close()
for line in lines:
    #tmp = stmt.format(line,line)
    tmp = stmt.format(line)
    print (tmp)