import re
dn='81545696567';
with open('regex_list.txt') as file:
    lines = [line.rstrip() for line in file]
file.close()

with open('dn_list.txt') as dfile:
    dlines = [dline.rstrip() for dline in dfile]
dfile.close()

ln = int(0)
for dline in dlines:
    ln=0;
    for line in lines:
        ln = ln + 1
        match = re.findall(line, dline)
        if(len(match)):
            print("Matched with regex : ",ln," : ",dline," : ",line)