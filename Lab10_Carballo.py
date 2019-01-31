import Nation
import pickle
import operator

nations = {}

file = open("UN.txt", "r") 

for line in file: 
    line = line.split(',')
    line[3] = line[3].rstrip()
    d = Nation.Nation(line[0], line[1], line[2], line[3])
    nations[d.name] = [d.continent, d.population, d.land]

file.close()

with open('nationsDict.dat', 'wb') as f:
    pickle.dump(nations, f, pickle.HIGHEST_PROTOCOL)


#start of part B
country = input("Enter a country: ")

with open('nationsDict.dat', 'rb') as f:
    data = pickle.load(f)

if country in data:
    value = []

    for v in data[country]:
        
        value.append(v)

    value[1] = float(value[1]) * 1000000
    value[1] = int(value[1])
    value[2] = float(value[2])

    print("Continent: " + value[0])
    print("Population: {:,}".format(value[1]))
    print("Area: {:,.2f}".format(value[2]) + " square miles\n")

#start of part C
continent = input("Enter a continent: ")
DensityInfo = {}
info = []

for k,v in data.items():   
    for c in v:
        if c == continent:            
            DensityInfo[k] = v
            for p in DensityInfo[k]:
                info.append(p)
                while (len(info) == 3):                  
                    info[1] = float(info[1]) * 1000000
                    info[1] = int(info[1])
                    info[2] = float(info[2])
                    e = Nation.Nation('','', info[1], info[2])
                    DensityInfo[k] = e.popDensity(info[1], info[2])
                    info = []
           
sortDensity = sorted(DensityInfo.items(), key=lambda x: x[1], reverse = True)

for i in range(5):
    print(sortDensity[i][0])
        
        
            
    
    
    
        
            
 
