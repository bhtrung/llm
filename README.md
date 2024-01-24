# Install
```
conda create -n vllm python=3.9 -y
conda activate vllm
pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu121
pip install langchain -q
```
# Test LLM inference
python inference.py
