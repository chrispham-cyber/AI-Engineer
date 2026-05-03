from ollama import chat

response = chat(
    model='qwen3-coder:30b',
    messages=[
        {'role': 'user', 'content': 'What is a neural network in one sentence?'}
    ],
    options={
	'temperature': 0.7,
        'num_predict': 512
    }
)

print(response['message']['content'])
