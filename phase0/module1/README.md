# API Call

## Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3-coder:30b
```

## [Python](scripts/api.py)
## [TypeScript](scripts/api.ts)
## Raw HTTP (No SDK)
```
curl -s http://localhost:11434/api/generate -d '{
  "model": "qwen3-coder:30b",
  "prompt": "Why is the sky blue?",
  "stream": false
}' | jq -r '.response'
```

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|----------------------|
| API key | "Password for the API" | A unique string that identifies your account and authorizes requests |
| Rate limit | "They're throttling me" | Maximum requests per minute/hour to prevent abuse and ensure fair usage |
| Token | "A word" (in API context) | A billing unit: input and output tokens are counted and charged separately |
| Streaming | "Real-time responses" | Getting the response word by word instead of waiting for the full response |
