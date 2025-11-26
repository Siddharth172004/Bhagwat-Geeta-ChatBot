# 🕉️ Bhagwat-Geeta AI Chatbot  
A premium conversational AI chatbot built on the timeless wisdom of the Bhagwat Geeta — powered by **RAG (Retrieval-Augmented Generation)**, **FAISS embeddings**, and a modern **Streamlit UI** for an elegant, interactive experience.

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/AI-RAG%20Pipeline-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Embeddings-FAISS-00C853?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Multi--Language-blue?style=for-the-badge" />
</p>

---

## 📂 **Project Structure**
```
📁 Bhagwat-Geeta-Chatbot
├── .devcontainer/           # Auto-generated – optional
├── Data/                    # Raw shloka dataset
├── Vector Data/             # Embeddings + FAISS index
├── StreamLit_UI.py          # Streamlit interface
├── main.py                  # RAG pipeline + backend logic
├── chunks_vector.py         # Embeddings + FAISS index generator
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ✨ **Features**
- 🗣 **Interactive chatbot** answering queries based on authentic Bhagwat Geeta shlokas  
- ⚡ **FAISS embeddings** for lightning-fast semantic search  
- 🧠 **RAG pipeline** for highly contextual and meaningful responses  
- 💻 **Clean & modern Streamlit UI**  
- 🌐 **Full multi-language support**  
- 🔄 **Easily extendable** to add more chapters/shlokas  

---

## 🛠 **Installation**

```bash
git clone https://github.com/your-username/Bhagwat-Geeta-Chatbot.git
cd Bhagwat-Geeta-Chatbot

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
# Create your .env file and add your API key
"OPENAI_API_KEY=your_api_key_here" > .env
```

---

## 🚀**Usage**

```bash
streamlit run StreamLit_UI.py
```

Open the link provided by Streamlit (usually **http://localhost:8501**)  
Ask questions in **English or Hindi** and receive deep, context-aware spiritual answers.

---

## 🔄 **Workflow Overview**

### 1️⃣ **Data Preparation**  
Raw shlokas stored inside the `Data/` folder.

### 2️⃣ **Embeddings Generation**  
`chunks_vector.py` processes shlokas → creates vector chunks → builds **FAISS index**.

### 3️⃣ **Backend Logic**  
`main.py` runs the full **RAG pipeline**, performing semantic search + response generation.

### 4️⃣ **Frontend UI**  
`StreamLit_UI.py` renders the interactive chatbot interface.
  
---

## 🚀 **Future Enhancements**
- 💡 Conversation memory for personalized responses  
- 🎨 More interactive animated UI  
- 🔗 Web deployment on Render / Vercel / AWS  

---

## 📌 **License**
Open-source and free to use.

---

Experience the **timeless wisdom of the Bhagwat Geeta** through a modern, intelligent AI chatbot.  
🕉️ *“Let knowledge light your path.”*

### 👨‍💻 Developed By  
**Siddharth Dhole**
