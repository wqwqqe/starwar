import json

fr = open("films.csv", "r")

fw = open("stat_basic.csv", "w")
fw.write('titel,key,value'+'\n')

for line in fr:
    temp = json.loads(line.strip("\n"))
    fw.write(temp["title"]+','+'characters'+',' +
             str(len(temp['characters']))+'\n')
    fw.write(temp['title'] + ',' + 'planets' +
             ',' + str(len(temp['planets'])) + '\n')
    fw.write(temp['title'] + ',' + 'starships' +
             ',' + str(len(temp['starships'])) + '\n')
    fw.write(temp['title'] + ',' + 'vehicles' +
             ',' + str(len(temp['vehicles'])) + '\n')
    fw.write(temp['title'] + ',' + 'species' +
             ',' + str(len(temp['species'])) + '\n')

fr.close()
fw.close()
