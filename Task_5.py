import json

# 수정할 json 파일 경로 입력
with open('./2023_2-4.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 삭제하면 안되는 키 배열
for i in range(len(json_data)):

    try:
        splitRoomName = json_data[i]["tempTime"].split(')')
        if splitRoomName[1] != "":
            del json_data[i]["tempTime"]
            json_data[i]["startTime"] = "temp"
            json_data[i]["endTime"] = "temp"
            json_data[i]["courseDay"] = "temp"
        elif splitRoomName[0].find(" ") >= 0:
            del json_data[i]["tempTime"]
            json_data[i]["startTime"] = "temp"
            json_data[i]["endTime"] = "temp"
            json_data[i]["courseDay"] = "temp"
        else:
            json_data[i]["tempTime"] = splitRoomName[0]

        print(json_data[i]["tempTime"])
    except:
        json_data[i]["startTime"] = "temp"
        json_data[i]["endTime"] = "temp"
        json_data[i]["courseDay"] = "temp"



# 수정된 json 파일 저장 경로 입력
with open('./2023_2-5.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)

print(json.dumps(json_data, indent='\t', ensure_ascii=False))
