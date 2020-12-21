import json

fr = open("film_characters.csv", "r")
fw = open("stat_characters.csv", "w")

fw.write("name,height,mass,gender,homeworld" + "\n")

for line in fr:
    print(line.strip("\n"))
    temp = json.loads(line.strip("\n"))
    if temp["height"] == "unknown":
        temp["height"] = "-1"
    if temp["mass"] == "unknown":
        temp["mass"] = "-1"
    if temp["gender"] == "n/a":
        temp["gender"] = "none"
    fw.write(temp["name"] + "," + temp["height"] + "," + temp["mass"] +
             "," + temp["gender"].strip() + "," + temp["homeworld"] + '\n')

fw.close()
fr.close()
