import json

# 文件路径
output_dir = 'evidence/wikipedia'
input_file = ''
output_file = ''
import os
def read_txt_files(filenames):
    contents = []
    for filename in filenames:
        file_path = os.path.join(output_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contents.append(f.read().strip())
        except FileNotFoundError:
            contents.append(f"[Content not found: {filename}]")
    return " ".join(contents)


with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    # shot1 = data["Data"][900]
    # txt1 = read_txt_files([page["Filename"] for page in shot1["EntityPages"]])
    # message1 = txt1 + "\n\nQuestion: " + shot1["Question"] + "\n\nThe answer is: "+ shot1["Answer"]["Value"]+"\n\n"
    # print(message1)


    extracted_data = [
        {
            "messages": [
                {
                    "role": "user",
                    "content":"Please understand the given Context first and then output the answer of the question based on the Context. \n\n"+read_txt_files([page["Filename"] for page in entry["EntityPages"]])+"\n\nQuestion: "+entry["Question"]+"\n\nLet's think step by step.\n\nThe answer is in the form of a word.\n\n",

                },
                {
                    "role": "assistant",
                    "content":entry["Answer"]["Value"]
                }
            ]
        }
        for entry in data["Data"]
    ]

    # train保留前25000个条目
    limited_data = extracted_data[:25000]
    # valid保留前800个条目
    # limited_data = extracted_data[:800]

    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(limited_data, out_file, indent=4)

