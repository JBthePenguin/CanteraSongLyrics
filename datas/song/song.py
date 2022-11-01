# python manage.py loaddata datas/song/song.json

import json

with open("song_datas.txt", "r") as f:
    datas = f.readlines()

datas_list = []
for data in datas:
    data_list = data.strip().split('\t')
    datas_list.append(
        {
            "fields": {
                "title": data_list[1],
                "author": data_list[2],
                "lyrics": data_list[3].replace("\\r\\n", "\n"),
            },
            "model": "songapp.song",
            "pk": int(data_list[0])
        }
    )

with open('song.json', 'w') as fout:
    json.dump(datas_list , fout)
