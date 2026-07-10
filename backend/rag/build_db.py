from backend.rag.pipeline import rag_pipeline

# Build vector database from ALL PDFs
rag_pipeline.build(
    "data/medical_docs"
)

print("\n✅ Vector Database Created Successfully")

print("\n🔍 Testing Search...\n")

results = rag_pipeline.search(
    "What are the symptoms of diabetes?"
)

if not results:
    print("❌ No results found.")

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Result {i}")
    print("=" * 80)

    print(f"Category : {doc.metadata.get('category', 'Unknown')}")
    print(f"File     : {doc.metadata.get('filename', 'Unknown')}")
    print(f"Page     : {doc.metadata.get('page', 'Unknown')}")

    print("\nContent:\n")
    print(doc.page_content[:1000])
    print("\n")