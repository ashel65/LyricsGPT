from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='/tmp/test-clm')
set_seed(42)
print(generator("My name is Eminem, and I'm", max_length=30, num_return_sequences=5))