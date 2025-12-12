from step2 import Settings  # Import Settings that were configured in step2
from step4 import nodes  
from llama_index.core.llama_pack import download_llama_pack

# Download or load the Query Fusion pack
QueryRewritingRetrieverPack = download_llama_pack(
    "QueryRewritingRetrieverPack",
    "./query_rewriting_pack",
)

# Create the advanced retriever using your nodes
query_rewriting_pack = QueryRewritingRetrieverPack(
    nodes,                      # semantic chunks from Step 4
    chunk_size=256,
    vector_similarity_top_k=8,
    fusion_similarity_top_k=8,
    num_queries=6,              # number of query rewrites
)

print("🚀 Advanced Query Fusion RAG Engine Ready!")