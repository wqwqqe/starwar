import requests
import json

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

f = open("films.csv", 'r', encoding='utf-8')
films = []

for line in f.readlines():
    print(line.strip('\n'))
    line = json.loads(line.strip('\n'))
    films.append(line)

f.close()

targets = ['characters', 'planets', 'starships', 'vehicles', 'species']

for target in targets:
    print(target)
    fw = open('film_' + target + '.csv', 'w')
    data = []
    for item in films:
        tmp = item[target]
        print(tmp)
        for t in tmp:
            if t in data:
                continue
            else:
                data.append(t)

            while 1:
                try:
                    print(t)
                    r = requests.get(t, headers=headers)
                    r.encoding = 'uft-8'
                except Exception as e:
                    continue
                else:
                    fw.write(r.text + '\n')
                    break

    print(str(len(data)), target)
    fw.close()

print("hello world")
