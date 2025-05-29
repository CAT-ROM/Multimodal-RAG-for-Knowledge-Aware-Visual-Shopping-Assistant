# 🛍️ Multimodal RAG for Knowledge-Aware Visual Shopping Assistant

## 🎯 Project Overview

This project implements a **Multimodal Retrieval-Augmented Generation (RAG)** system designed to answer user queries about products by combining information from both **textual data** and **product images**. The system retrieves relevant multimodal documents — including product reviews, Q&A threads, specifications, and images — from a curated knowledge base and uses a large language model (LLM) to generate context-aware, grounded, and natural language answers.

This approach enhances traditional text-only search by incorporating visual content, allowing for more comprehensive and user-friendly responses.

---

## 💡 Motivation

E-commerce platforms provide vast amounts of product data and images. Users often have specific questions such as:

- 🥾 “Are these shoes good for hiking?”
- 🎧 “Do these headphones work well on flights?”
- 🔋 “What do people say about the battery life?”

Answering these questions requires understanding multiple types of data: product descriptions, user reviews, and images. This project builds a system that leverages multimodal data retrieval and generation to assist users effectively.

---

## 📁 Project Structure

bioinformatics-rag-app/
├── data/ # 🗂️ Product metadata CSV and images folder
├── embeddings/ # 💾 (Optional) Precomputed embeddings for faster retrieval
├── shopping_rag_app.py # 🖥️ Streamlit app frontend
├── retrieval_pipeline.py # 🔍 Retrieval logic for text and images
├── generation_module.py # 🤖 Answer generation logic using retrieved info
├── requirements.txt # 📦 Python dependencies
└── README.md # 📄 This detailed project documentation

markdown
Copy
Edit

- **data/** — Contains the scraped dataset with product metadata CSV and corresponding images.  
- **embeddings/** — Optional folder where precomputed vector embeddings are stored to speed up similarity search.  
- **shopping_rag_app.py** — The Streamlit frontend to input queries and display generated answers.  
- **retrieval_pipeline.py** — Code that handles embedding creation and retrieving relevant multimodal documents.  
- **generation_module.py** — Module to format prompts and generate answers using an LLM like OpenAI GPT.  
- **requirements.txt** — List of all Python libraries needed to run the app.  
- **README.md** — This file explaining the project details.  

---

## 🛠️ Features

- **Multimodal Data Retrieval**: Combines text (reviews, specs, Q&A) and images for rich context.  
- **Vector Search**: Uses embeddings to find the most relevant product documents.  
- **LLM Integration**: Generates grounded answers referencing both text and images.  
- **User-Friendly Interface**: Streamlit-based frontend for easy interaction.  

---

## 🚀 How to Run

1. **Clone the repo**:

```bash
git clone https://github.com/CAT-ROM/bioinformatics-rag-app.git
cd bioinformatics-rag-app
