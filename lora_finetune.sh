formatted_time=$(date +"%Y%m%d%H%M%S")
echo $formatted_time


python finetune.py \
    --model_name_or_path /root/model/minicpm-2b \
    --output_dir output/LoRA/$formatted_time/ \
    --train_data_path train.json \
    --eval_data_path val.json \
    --learning_rate 5e-5 --per_device_train_batch_size 10 \
    --per_device_eval_batch_size 10  --model_max_length 384 --bf16 --use_lora \
    --gradient_accumulation_steps 1 --warmup_steps 100 \
    --max_steps 10000 --weight_decay 0.01 \
    --evaluation_strategy steps --eval_steps 500 \
    --save_strategy steps --save_steps 500 --seed 42 \
    --log_level info --logging_strategy steps --logging_steps 10 
