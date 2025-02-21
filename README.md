# 🔍 AI-Powered Natural Language Search for PostgreSQL  

This project implements a **Natural Language Search Interface** using **Streamlit** and **OpenAI** to convert user queries into SQL and retrieve data from **PostgreSQL** efficiently. It also incorporates **vector search** using `pgvector` for enhanced text-based similarity searches.  

---

## 🚀 **Project Overview**  
Many business applications rely on structured databases (like PostgreSQL) but struggle to provide an intuitive way for users to query data. This project enables users to **ask questions in natural language** (e.g., *"Show me all employees in the Engineering department earning above 50,000"*), and the system **translates it into SQL** to fetch relevant results.  

### ✅ **Key Features**  
✔️ **LLM-Powered SQL Generation**: Uses OpenAI to convert user queries into SQL.  
✔️ **Hybrid Search**: Combines traditional SQL filtering with **vector similarity search** (`pgvector`).  
✔️ **Secure Execution**: Query validation to prevent SQL injection risks.  
✔️ **User-Friendly UI**: Built with Streamlit for an interactive experience.  

---

## 📌 **Tech Stack**  
- **Backend**: Python (`FastAPI`, `asyncpg`, `pgvector`, `openai`)  
- **Database**: PostgreSQL (with `pgvector` for embeddings)  
- **Frontend**: Streamlit (for interactive UI)  
- **LLM**: OpenAI (for NLP-to-SQL conversion)  

---

## 🏗️ **Project Structure**
💡 How It Works
1️⃣ User enters a natural language query in Streamlit (e.g., "Find all employees in HR").
2️⃣ The LLM converts the query into SQL (e.g., SELECT * FROM employees WHERE department = 'HR';).
3️⃣ The system executes the query securely on the PostgreSQL database.
4️⃣ Results are displayed in an interactive table on Streamlit.

🔴 Challenges Faced & Solutions
❌ Issue 1: SQL Injection Risks
💡 Solution: Used query validation techniques to prevent malicious injections.

❌ Issue 2: Poor Search Accuracy
💡 Solution: Implemented vector search (pgvector) to enhance results based on text similarity.

❌ Issue 3: Slow Query Execution
💡 Solution: Optimized database indexes & query caching to improve performance.

**## How to Run the Project 🚀**
---------------------------------------------------------------------
Add Your OpenAI API Key
This project requires an OpenAI API key for generating responses.
---------------------------------------------------------------------
Add your opnai key in .env file in the root directory of the project.
-----------------------------------------------------------------------
To start the project, run the following command in your terminal:
--------------------------------------------------------------

streamlit run streamlit_app.py
---------------------------------------

### Requirements:
- Ensure you have **Python 3.8+** installed.
- Install dependencies using:

  ```bash
  pip install -r requirements.txt
  ```
-------------------------------------------------------------------------------------
- If you face database connection issues, check **port_imp.txt** for troubleshooting.

-------------------------

This will help others understand how to execute the project easily. 🎯




🚀 Future Improvements
✅ Expand support for multiple databases (MySQL, MongoDB).
✅ Implement chatbot integration for more interactive searches.
✅ Add authentication & user management.
✅ Use fine-tuned LLM models for better query understanding.

🎯 If you find this project useful, don't forget to ⭐ the repo! 😊

