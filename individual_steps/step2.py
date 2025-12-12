
import os
from getpass import getpass
import nest_asyncio

nest_asyncio.apply()

from llama_index.core import Settings
from llama_index.llms.openrouter import OpenRouter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Ask for your OpenRouter API key (input is hidden like a password)
os.environ["OPENROUTER_API_KEY"] = getpass("Enter your OpenRouter API key: ")

# Configure the LLM (Meta Llama via OpenRouter)
llm = OpenRouter(
    api_key=os.environ["OPENROUTER_API_KEY"],
    model="meta-llama/llama-3.3-70b-instruct:free",
    max_tokens=512,
    temperature=0.1,  # Low = more precise, less “creative”
    timeout=60,
    system_prompt=(
        "You are an expert RAG system that answers ONLY using the provided context. "
        "Never hallucinate. Never guess. If the answer is not in the context, say so. "
        "Provide short, clear, factual responses with 2–4 evidence bullets."
    ),
)

# Configure the embedding model
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Register both with LlamaIndex settings
Settings.llm = llm
Settings.embed_model = embed_model

print("✅ AI model and settings are ready to use")