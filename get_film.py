import requests
films = []
for i in range(1, 7):
    films.append('https://swapi.dev/api/films/'+str(i)+'/')


headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

with open('films.csv', 'w') as file:
    for film in films:
        print(film)
        r = requests.get(film, headers=headers)
        r.encoding = 'utf-8'
        file.write(r.text+"\n")
