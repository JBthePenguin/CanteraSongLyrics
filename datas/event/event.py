# python manage.py loaddata datas/event/event.json

import json

with open("event_datas.txt", "r") as f:
    datas = f.readlines()

datas_list = []
for data in datas:
    data_list = data.strip().split('\t')
    end_time = data_list[4]
    if end_time == '\\N':
        end_time = None
    datas_list.append(
        {
            "fields": {
                "title": data_list[1],
                "description": data_list[2].replace("\\r\\n", "\n"),
                "start_time": data_list[3],
                "end_time": end_time
            },
            "model": "eventapp.event",
            "pk": int(data_list[0])
        }
    )

with open('event.json', 'w') as fout:
    json.dump(datas_list , fout)
