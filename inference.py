import time
from langchain_community.llms import VLLM

llm = VLLM(
    #model="mistralai/Mistral-7B-Instruct-v0.2",
    model="Viet-Mistral/Vistral-7B-Chat",
    trust_remote_code=True,  # mandatory for hf models
    max_new_tokens=128,
    top_k=10,
    top_p=0.95,
    temperature=0.8,
)

start_time = time.time()
print(llm("Thủ đô của Việt Nam là gì ?"))
print("--- %s seconds ---" % (time.time() - start_time))
