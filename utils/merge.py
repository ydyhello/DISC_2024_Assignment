import json

file1_path = ''
file2_path = ''
merged_file_path = ''

with open(file1_path, 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)


with open(file2_path, 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)


merged_data = []
len1, len2 = len(data1), len(data2)
max_len = max(len1, len2)
print(len1)
print(len2)
for i in range(max_len):
    if i < len1:
        merged_data.append(data1[i])
    if i < len2:
        merged_data.append(data2[i])


with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
    json.dump(merged_data, merged_file, ensure_ascii=False, indent=4)

print(f"合并后的JSON数据已写入 {merged_file_path}")
