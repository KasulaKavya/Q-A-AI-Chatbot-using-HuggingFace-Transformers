import re, os
from transformers import pipeline
from pdf_loader import load_pdf  # Ensure this is the correct import for your PDF loader

# Disable Hugging Face symlink warnings
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def extract_email(text):
    """
    Extract email addresses from the given text using a regular expression.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def split_into_chunks(text, chunk_size=500):
    """
    Split the text into smaller chunks of a specified size.
    """
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def find_relevant_context(context_chunks, question):
    """
    Find the most relevant chunk of text for the given question.
    """
    best_chunk = max(context_chunks, key=lambda chunk: len(set(chunk.split()) & set(question.split())))
    return best_chunk

def ask_question(context, question):
    """
    Use Hugging Face's question-answering pipeline to answer a question based on the provided context.
    """
    try:
        # Load the Hugging Face question-answering pipeline
        qa_pipeline = pipeline("question-answering", model="deepset/roberta-large-squad2")

        # Split the context into smaller chunks
        context_chunks = list(split_into_chunks(context))

        # Find the most relevant context
        relevant_context = find_relevant_context(context_chunks, question)

        # Get the answer
        result = qa_pipeline(question=question, context=relevant_context)
        return result["answer"]
    except Exception as e:
        print(f"Error in ask_question: {e}")
        return "An error occurred while processing your question."

if __name__ == "__main__":
    # Specify the path to your PDF file
    pdf_path = "c:/Users/18456/OneDrive/Desktop/Desktop/Chatbot/chat-with-pdf/.venv/resume.pdf"

    # Load the PDF and combine all pages into a single text
    pages = load_pdf(pdf_path)
    resume_text = " ".join([page.page_content.strip() for page in pages])
    resume_text = resume_text.replace("\n", " ").strip()  # Preprocess the text

    # Extract email addresses
    emails = extract_email(resume_text)
    print("Email(s) found in the resume:", emails)

   # Allow the user to ask questions dynamically 
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        answer = ask_question(resume_text, question)
        print(f"Answer: {answer}")