import ollama from 'ollama';

async function main() {
  const response = await ollama.chat({
    model: 'qwen3-coder:30b',
    messages: [
      { role: 'user', content: 'What is a neural network in one sentence?' }
    ],
    options: {
      num_predict: 512
    }
  });

  console.log(response.message.content);
}

main();
