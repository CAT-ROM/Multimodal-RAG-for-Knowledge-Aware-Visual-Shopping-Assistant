import streamlit as st
from retrieval_pipeline import retrieve_documents
from generation_module import generate_answer

st.set_page_config(page_title="Visual Shopping Assistant", layout="wide")

st.title("🛍️ Multimodal RAG Visual Shopping Assistant")
st.markdown("Ask questions about products using text and images from our dataset.")

query = st.text_input("💬 Ask a question about a product (e.g., 'Are these shoes good for hiking?')")

if query:
    # Retrieve relevant multimodal documents
    retrieved_docs = retrieve_documents(query)
    
    st.subheader("🔍 Retrieved Documents")
    for doc in retrieved_docs['text_docs']:
        st.markdown(f"- {doc}")
    st.image(retrieved_docs['images'], width=200)

    # Generate answer using retrieved context
    answer = generate_answer(query, retrieved_docs)
    st.subheader("🤖 Answer")
    st.write(answer)
# Placeholder for shopping_rag_app.py
