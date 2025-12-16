# ray-local serving


If its your first time running, use

`python3 -m venv ray-local`


```
cd ~/Desktop/ray-local
source ray-local/bin/activate
serve run serve_simple:deployment
```

## Test the LLM using 

```
curl -X POST http://localhost:8000 \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is AI?", "max_tokens": 50}'
```