## 构造数据集

先构造训练集和测试集

运行 `utils\cosmosqa_utils.py`, `utils\triviaqa_utils.py`, `utils\merge.py`

### CosmosQA

`data\CosmosQA\25k`包含一个构造好的CosmosQA25k样例

可以在utils中修改指令构造不同的数据集

### TriviaQA

TriviaQA25k 文件太大需要自行构造

可以在utils中修改指令构造不同的数据集

### SVAMP

SVAMP 数据集 分别有 CoT 和 Without CoT

SVAMP CoT: `data\SVAMP\math_10k.json`

SVAMP Without CoT: `data\SVAMP\math_10kwithoutCoT.json`

测试集: `data\SVAMP\test.json`

## 微调

- MiniCPM

运行`lora_finetune.sh`

- LLAMA

运行`LLM-Adapters-main\finetune.py`



## 测试

- MiniCPM

SVAMP

运行`test.py`

TriviaQA 

运行`python3 -m evaluation.triviaqa_evaluation --dataset_file data\TriviaQA\wikipedia-dev800.json --prediction_file result_example\triviaqa_result.json`

- LLAMA

运行`LLM-Adapters-main\evaluate.py` 


