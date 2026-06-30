# 🤖 Gemini AI Chatbot using Streamlit

A simple AI chatbot built with **Python**, **Streamlit**, and **Google's Gemini API**. This project provides an interactive chat interface where users can ask questions and receive AI-generated responses in real time.

---

## 🚀 Features

- 💬 Interactive chatbot interface
- 🤖 Powered by Google's Gemini AI
- 📜 Chat history support
- ⚡ Fast and responsive Streamlit UI
- 🔒 API key stored securely using environment variables
- 🖥️ Beginner-friendly project structure

---

## 🛠️ Tech Stack

- Python 3.11+
- Streamlit
- Google GenAI SDK (`google-genai`)
- Python Dotenv

---

## 📂 Project Structure

```
Gemini-Chatbot/
│
├── QA.py                # Main Streamlit application
├── .env                 # API key (Not uploaded to GitHub)
├── requirements.txt     # Project dependencies
├── README.md
└── .gitignore
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chatbot.git

cd gemini-chatbot
```

---

### 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

Command Prompt

```bash
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Get a Gemini API Key

Visit Google AI Studio

https://aistudio.google.com/apikey

Create an API Key and copy it.

Create a `.env` file in the project folder.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Example

```env
GOOGLE_API_KEY=AIzaSy************************
```

> **Never commit your API key to GitHub.**

---

## ▶️ Run the Application

```bash
streamlit run QA.py
```

The application will open automatically in your browser.

---

## 📸 Screenshot

Add screenshots here after running the application.

```
assets/
    chatbot.png
```

---

## 📚 Dependencies

Example `requirements.txt`

```txt
streamlit
google-genai
python-dotenv
```

---

## 💡 Future Improvements

- Conversation memory
- Markdown rendering
- Streaming responses
- File upload support
- PDF Question Answering
- Image understanding
- Voice input/output
- Dark mode
- Multiple Gemini models
- Export chat history
- Authentication system

---

## 🐞 Common Issues

### API Authentication Error

Make sure your `.env` file contains

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### Module Not Found

Install all dependencies

```bash
pip install -r requirements.txt
```

---

### Streamlit Command Not Found

```bash
pip install streamlit
```

Run

```bash
streamlit run QA.py
```

---

## 📖 Learning Outcomes

This project demonstrates:

- Working with Google's Gemini API
- Building AI-powered applications
- Streamlit basics
- Environment variable management
- Python project organization
- Chatbot implementation

---

## 👨‍💻 Author

**Kartik Singh Rautela (Rocky)**

B.Tech CSE (AI & ML)

Passionate about AI, SaaS, Machine Learning, and Full Stack Development.

GitHub:
https://github.com/scorpioEve

LinkedIn:
(Add your LinkedIn profile)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀