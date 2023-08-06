import json



# 수정할 json 파일 경로 입력
with open('./2023_2-2.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 삭제하면 안되는 키 배열
for i in range(len(json_data)):
    json_data[i]["courseDay"] = ""
    json_data[i]["startTime"] = ""
    json_data[i]["endTime"] = ""


# 수정된 json 파일 저장 경로 입력
with open('./2023_2-3.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)

print(json.dumps(json_data, indent='\t', ensure_ascii=False))
