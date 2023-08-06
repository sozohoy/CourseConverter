import json

# json 키값 체인지
names_key = {'timtSmryCn' : 'roomName', 'reprPrfsEnoNm' : 'professor',
'facDvnm' : 'classification', 'trgtGrdeCd' : 'num',
'subjtNm' : 'courseName', 'estbDpmjNm' : 'major', 'point' : 'credit', 'diclNo' : 'classNum'}


# 수정할 json 파일 경로 입력
with open('./2023_2-1.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 삭제하면 안되는 키 배열
for row in json_data:
    print(row)
    for k,v in names_key.items(): # k = old_name & v = new_name
        for old_name in list(row):
            if k == old_name:
                row[v] = row.pop(old_name)

# 수정된 json 파일 저장 경로 입력
with open('./2023_2-2.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)

print(json.dumps(json_data, indent='\t', ensure_ascii=False))
