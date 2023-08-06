import json

startArray = ["null", "9:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30", "16:30", "17:30", "18:30", "19:30", "20:30", "21:30"]
endArray = ["null", "10:20", "11:20", "12:20", "13:20", "14:20", "15:20", "16:20", "17:20", "18:20", "19:20", "20:20", "21:20", "22:20"]

# 수정할 json 파일 경로 입력
with open('./2023_2-5.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 삭제하면 안되는 키 배열
for i in range(len(json_data)):

    try:
        if len(json_data[i]["tempTime"]) > 1:
            splitData = json_data[i]["tempTime"].split(",")
            json_data[i]["startTime"] = startArray[int(splitData[0])]
            json_data[i]["endTime"] = endArray[int(splitData[-1])]
        else:
            json_data[i]["startTime"] = startArray[int(json_data[i]["tempTime"])]
            json_data[i]["endTime"] = endArray[int(json_data[i]["tempTime"])]

        print(json_data[i]["startTime"])
        print(json_data[i]["endTime"])
        del json_data[i]["tempTime"]
    except:
        json_data[i]["startTime"] = "temp"
        json_data[i]["endTime"] = "temp"
        json_data[i]["courseDay"] = "temp"



# 수정된 json 파일 저장 경로 입력
with open('./20230806-2023-2.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)

print(json.dumps(json_data, indent='\t', ensure_ascii=False))
