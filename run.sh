python run_clm.py \
    --model_name_or_path gpt2 \
    --dataset_name alshelt/rap_lyrics \
    --dataset_config_name alshelt/rap_lyrics \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --do_train \
    --do_eval \
    --output_dir /tmp/test-clm