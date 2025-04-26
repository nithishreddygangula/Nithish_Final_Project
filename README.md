
# 🎯 AutoTutor AI – Study Companion

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📚 Project Overview

**AutoTutor AI – Study Companion** is a Generative AI-powered application designed to enhance learning through:

- 🧑‍🏫 Tutor Mode
- 📝 Quiz Generation
- 📖 Intelligent Summarization
- 📊 Evaluation of Quiz Responses

It integrates **Flask** with **Ollama** (local LLM inference) to provide a private, fast, and fully automated educational companion.

---

## 👨‍💻 Developed By

- **Nithish Reddy Gangula**  
  (ngangula2023@fau.edu)  
  Florida Atlantic University (FAU)  
  **COT6930 – Generative AI and Software Development Lifecycles**  
  **Instructor:** Dr. Fernando Koch

---

## 🚀 Features

| Feature | Status |
|:--------|:------:|
| Tutor Mode | ✅ |
| Quiz Mode | ✅ |
| Summary Mode | ✅ |
| Evaluation Mode | ✅ |
| Score Dashboard | ✅ |
| Ollama Integration (Local Models) | ✅ |
| Single-Click Interaction | ✅ |
| Automation Coverage | ~90% of SDLC |

---

## 🛠 Technology Stack

- **Frontend:** HTML5, CSS3 (Flask Templates)
- **Backend:** Python 3.10, Flask
- **Language Model:** Ollama (local server, e.g., Mistral model)
- **Visualization:** Basic score graphs
- **Hosting:** Localhost (Flask server)

---

## 🛠 Installation Instructions

1. **Install Python Libraries**
   ```bash
   pip install flask requests
   ```

2. **Ensure Ollama Server is Running**
   - Local Ollama server should be active at: `http://localhost:11434`

3. **Run the Application**
   ```bash
   python3 app.py
   ```

4. **Access Web App**
   Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 📁 Project Structure

```
AutoTutorAI/
│
├── webapp/
│   ├── app.py
│   ├── static/
│   │   └── score_dashboard.png
│   ├── prototype/
│   │   └── prompts/
│   │       ├── tutor_prompt.txt
│   │       ├── quiz_prompt.txt
│   │       ├── summary_prompt.txt
│
├── README.md
└── requirements.txt (optional)
```

---

## 🧠 How It Works

| Step | Description |
|:----:|:------------|
| 1 | Select a task (Tutor, Quiz, Summary, Evaluate) |
| 2 | Enter your question/topic |
| 3 | Backend sends prompt to Ollama API |
| 4 | AI Model processes and generates the response |
| 5 | Output shown on the web app including score visualization (if quiz) |

---

## 📈 Future Enhancements (Optional Ideas)

- Session History / Save Past Quizzes
- PDF Export of Tutor Sessions and Summaries
- Advanced Dashboard (Interactive Graphs)
- Multi-Agent Learning Assistants
- UI Improvements (e.g., Bootstrap-based design)

---

## 🤝 Acknowledgements

- **Professor:** Dr. Fernando Koch
- **Course:** COT6930 – Generative AI and Software Development Lifecycles
- **Institution:** Florida Atlantic University (FAU)

---

# ✨ Empower Your Learning Journey with AutoTutor AI ✨
# Nithish_Final_Project
