import csv
import json

csv_file = ''
json_file = ''



json_list = []

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) 
    count = 0
    for row in reader:
        if count >= 25000:
            break
        if len(row) >= 4:
            context = row[1]
            question = row[2]
            answer0 = row[3]
            answer1 = row[4]
            answer2 = row[5]
            answer3 = row[6]
            label = row[7]
            # message={ "instruction":"Answer the following multiple-choice question. Select 0, 1, 2, or 3 for the final answer. Let's think step by step.","input": str({'context':{context},'question':{question},"answer0":{answer0},"answer1":{answer1},"answer2":{answer2},"answer3":{answer3}}),"output":label}
            # "{\"messages\": [{\"role\": \"user\", \"content\": "
            json_data = {
                    "messages": [
                        {
                            "role": "user",
                            "content":(
                                # "请根据上下文回答正确的选项: \"{}\"\n\n"
                                # "问题: '{}'\n\n"
                                # "Answer0: '{}'\nAnswer1: '{}'\nAnswer2: '{}'\nAnswer3: '{}'\n\n"
                                # "一步一步思考.\n\n"
                                # "1. 找出问题中的关键信息。\n"
                                # "2. 根据关键信息评估每个答案选项。\n"
                                # "3. 剔除明显不正确的选项。\n"
                                # "4. 根据剩余的选项选择最合适的选项。\n\n"
                                # "答案格式: 0/1/2/3\n\n"

                                "Please choose the correct answer to the question: \"{}\"\n\n"
                                "Question: '{}'\n\n"
                                "Answer0: '{}'\nAnswer1: '{}'\nAnswer2: '{}'\nAnswer3: '{}'\n\n"
                                # "Example: Please choose the correct answer to the question: \"\"As I am bent over taking out the milk , I hear footsteps pass the kitchen entrance , in the living room , and then his office door open . It was latched shut and I heard what sounded like the door knob turning and then the door opened all of the way . I thought it was my husband getting up during the night as he normally does and going into his office due to his insomnia . I look into his office and do n't see any cats around in there . I go back to bed and ask if by chance he just got up , opened his door and then went back to bed .\"\" \n\nQuestion:'Why did I go back to bed ?\',\n\nAnswer0: 'Because I heard footsteps pass the kitchen entrance .'\nAnswer1: 'Because I heard footsteps in the living room'\nAnswer2:'Because I did n't find anything out of the ordinary.'\nAnswer3: 'None of the above choices .'\n\nThe correct answer is 2.\n\n"
                                # "Let's think step by step: First, the text describes the author getting out of bed at night. The author then heard footsteps in the kitchen and living room, and the sound of her husband's office door being opened. Then, the author thought it was her husband who got up and went to the office because of insomnia. Finally, the author went back to bed and thought it was normal since he didn't notice anything unusual. So the answer is 2.\n\n"
                                
                                # "Example: Please choose the correct answer to the question: \"\"Dig in before it gets cold ! \"\" Akira places a good amount on his plate , as does Kouyou . I feel so out of place when I grab a few pancakes , rather than the heaping amount they did .\"\"\n\nQuestion: 'Why did the writer feel out of place ?'\n\nAnswer0: 'Because they were n't hungry .'\nAnswer1: 'None of the above choices .'\nAnswer2: 'Because they do n't like pancakes .'\nAnswer3: 'Because they took less food than everyone else .'\n\nThe correct answer is 3.\n\n"
                                # "Let's think step by step: First, the text mentions the author having breakfast with others. Then, the author felt that he was different from others when taking food and worried that he was taking too little. Ultimately, this feeling leaves the author feeling out of place or out of place. So the answer is 3.\n\n"
                                
                                # "Example: Please choose the correct answer to the question: \"\"Moving on .... Today Robin and I went to the local farmers market , the library ( where I realized I have absolutely no idea where my library card is ) , and then drove around looking for garage sales . She feel asleep in the car on the way home so I have a little time to myself . Where 's the hubs ?\"\n\nQuestion: 'How did Robin feel at the library ?'\n\nAnswer0: 'Robin was let down .'\nAnswer1: 'None of the above choices .'\nAnswer2: 'Robin was excited .'\nAnswer3: 'Robin was happy .'\n\nThe correct answer is 0.\n\n"
                                # "Let's think step by step: First, the text mentions that the author went to the library with Robin. Then, the author may feel anxious or disappointed when he realizes that he cannot find his library card. Finally, by inferring that Robin was disappointed in the library, possibly because the author couldn't find the card. So the answer is 0.\n\n"

                                # "Example: Please choose the correct answer to the question: \"\"He can see him self being smiled upon and he can look himself pointing at him . He was just portrayed that he has been loved , he has been cared and he has been pampered . All good things must come to an end so was them ! \"\"\n\nQuestion:'Why can he see himself being smiled upon ?'\n\nAnswer0: 'None of the above choices .'\nAnswer1: 'He feels loved or blessed .'\nAnswer2: 'He can look himself pointing at him .'\nAnswer3: 'All good things must come to an end .'\n\nThe correct answer is 1.\n\n"
                                # "Let's think step by step: First, the text describes a situation in which a person is loved, cared for, and pampered. Then he felt loved or blessed, a feeling that made him feel like he was being smiled at. Finally, this feeling leads him to the emotional state of being blessed or loved. So the answer is 1.\n\n"
                                # "Let's think step by step.\n\n"
                                # "1. Identify the key information in the question.\n"
                                # "2. Evaluate each answer option based on the key information.\n"
                                # "3. Eliminate the obviously incorrect options.\n"
                                # "4. Choose the most appropriate option based on the remaining choices.\n\n"
                                "Answer format: 0/1/2/3!!! \n\n"
                            ).format(
                                context,
                                question,
                                answer0,
                                answer1,
                                answer2,
                                answer3
                            ),
                        },
                        {
                            "role": "assistant",
                            "content":label,
                        },
                    ]
                }
            
            json_list.append(json_data)
            count += 1


with open(json_file, 'w', encoding='utf-8') as file:

    file.write(json.dumps(json_list, ensure_ascii=False, indent=4))
        