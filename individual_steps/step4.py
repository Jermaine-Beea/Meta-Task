from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load the PDF as a document
documents = SimpleDirectoryReader(input_files=["/workspaces/Meta-Task/data/source.pdf"]).load_data()
print(f"📄 Loaded {len(documents)} document(s).")

# Embedding model for semantic splitting (can reuse the same model name)
semantic_embed = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Create a semantic splitter
parser = SemanticSplitterNodeParser(
    buffer_size=3,
    breakpoint_percentile_threshold=95,
    embed_model=semantic_embed,
)

# Generate semantic nodes (chunks)
nodes = parser.get_nodes_from_documents(documents)

# Add simple metadata to each chunk
for n in nodes:
    n.metadata["source"] = "/workspaces/Meta-Task/data/source.pdf"
    n.metadata["chunk_type"] = "semantic"

print(f"🔍 Created {len(nodes)} high-quality semantic nodes.")