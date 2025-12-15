from ray import serve
from vllm import LLM, SamplingParams

@serve.deployment(ray_actor_options={"num_gpus": 1})
class VLLMDeployment:
    def __init__(self):
        self.llm = LLM(
            model="./Llama-3.1-Nemotron-Nano-4B-v1.1",
            trust_remote_code=True,
            gpu_memory_utilization=0.90,
            max_model_len=4096,
        )

    async def __call__(self, request):
        data = await request.json()
        prompt = data.get("prompt", "Hello!")
        
        outputs = self.llm.generate(
            [prompt], 
            SamplingParams(max_tokens=data.get("max_tokens", 100))
        )
        return {"response": outputs[0].outputs[0].text}

deployment = VLLMDeployment.bind()