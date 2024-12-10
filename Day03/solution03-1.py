with open('Day03/input.txt', 'r') as file:
    data = file.read()


data = data.split('mul(')
compteur=0
for i in range(len(data)):
    try:
        data[i] = data[i].split(',')
        data[i][1] = data[i][1].split(')')
        if(0<int(data[i][0])<1000 and 0<int(data[i][1][0])<1000 and ' ' not in data[i][0] and ' ' not in data[i][1][0] and len(data[i][1])>1):
            compteur+=int(data[i][0])*int(data[i][1][0])
    except:
        pass
    
print(compteur) # --> 175615763