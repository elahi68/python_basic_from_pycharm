
str = '''
set heading off;
set pagesize 50000;
set feedback off;
set verify off;
set newpage 0;
spool \'E:\\Spool\\pedlinux_load_{}.txt\';
SELECT
    \'46|\'
    || iccid
    || \'|20|2\'
FROM
    ni_sim
WHERE
    sim_pk BETWEEN {} AND {};
spool off;
'''
#print(str)
j=1
cnt=0
#initial,final,step = 1,3000000,100000
#<initial_value>,<latest ud pk from ni_sim>,<step_size>
initial,final,step = 1,79625,10000

for i in range(initial,final,step):
    prev = j
    cnt = cnt+1
    if (i!=1):
        #print (prev,i-1)
        tmp = str.format(cnt-1,prev,i-1)
        print(tmp)
    j = i
cnt = cnt+1;
#print ("final ",i,final)
tmp = str.format(cnt-1,i,final)
print(tmp)
#print (cnt)