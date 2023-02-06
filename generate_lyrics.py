# from transformers import GPTNeoXForCausalLM, GPTNeoXTokenizerFast

# model = GPTNeoXForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b")
# tokenizer = GPTNeoXTokenizerFast.from_pretrained("EleutherAI/gpt-neox-20b")

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='/tmp/test-clm')
set_seed(42)
print(generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5))