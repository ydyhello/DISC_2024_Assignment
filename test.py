import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


path = "/root/ydy/MiniCPM/finetune/output/LoRA/20240516152256/checkpoint-10000"
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(
    path, torch_dtype=torch.bfloat16, device_map="cuda", trust_remote_code=True
)
print(model)

import json 
count =0 
with open("valid.json") as file:
    data = json.load(file)
    print(len(data))
    sum=len(data)
    for item in data:
        res, history = model.chat(tokenizer, query=item["messages"][0]["content"], max_length=100000, top_p=0.5)
        ("--------------------------------------")
        print("res:",res)
        print("true:",item["messages"][1]["content"])
        print("___________________________")
        if res == item["messages"][1]["content"]:
            count +=1
print("acc: ",count/sum)