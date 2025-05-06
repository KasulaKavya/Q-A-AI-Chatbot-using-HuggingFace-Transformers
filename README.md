# Chat with PDFs using HuggingFace-Transformers
This is a Python-based AI chatbot that lets you upload your resume, PDF and ask dynamic questions about it — such as your name, email, phone number, skills, experience or even any other data — using cutting-edge NLP models.![Screenshot 2025-05-05 225922](https://github.com/user-attachments/assets/b801ea19-bece-41e5-ba94-7e1303272421)
![Screenshot 2025-05-05 225743](https://github.com/user-attachments/assets/c9ae79df-6960-42a5-a3c2-08596121fad0)
![Screenshot 2025-05-05 225551](https://github.com/user-attachments/assets/f35ae55f-5eeb-473a-895a-6f54498df977)
![Screenshot 2025-05-05 225501](https://github.com/user-attachments/assets/598ab3c5-e0d7-45cf-8475-12b687e57ab2)


## 🚀 Run
```bash
streamlit run app.py
```
Upload any PDF and ask questions using GPT!

## 🚀 Features
- 📄 Parse any PDF resume
- 🤖 Ask questions like:
  - "What is my email?"
  - "What programming languages do I know?"
  - "What is my current job title?"
  - Any question based on PDF you upload
- 🧠 Powered by `roberta-large-squad2` for accurate Q&A
- 🧱 Handles long documents with chunking and context matching
- ✅ Regex-based email extraction

## 🛠️ Technologies Used
| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core programming language |
| Hugging Face Transformers | Q&A model pipeline |
| LangChain | For PDF text extraction |
| PyPDFLoader | PDF parsing |
| Regex | Email extraction |
| CLI (Command Line) | Interactive chat |

## 🧠 How It Works
1. Loads your PDF resume using LangChain’s `PyPDFLoader`
2. Extracts the full text content
3. Splits text into ~500-word chunks
4. Finds the most relevant chunk for your question using word overlap
5. Feeds that chunk + question to `roberta-large-squad2`
6. Returns the most accurate answer


## 📂 Project Structure
.
├── resume_qa_bot.py # Main script
├── pdf_loader.py # PDF loading function
├── README.md # Project documentation
├── images/ # Screenshots (add your demo images)
│ ├── demo1.png
│ └── demo2.png


## 🔧 Setup
```bash
git clone https://github.com/yourusername/resume-qa-bot.git
cd resume-qa-bot

pip install -r requirements.txt
python resume_qa_bot.py

from langchain.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages

Example:
Email(s) found in the resume: ['you@example.com']
Enter your question (or type 'exit' to quit): What is my name?
Answer: John Doe

🔮 Future Enhancements
1. Streamlit web UI
2. Resume embedding + semantic search (RAG)
3. Fine-tuned Q&A model for resume data
4. Extraction of phone number, LinkedIn, GitHub

🙌 Credits
# Hugging Face Transformers
# Deepset roberta-large-squad2
# LangChain
