
from flask import Flask, render_template_string, request
import requests
import json

app = Flask(__name__)
session_data = {}

TEMPLATES = {
    "tutor": open("prototype/prompts/tutor_prompt.txt").read(),
    "quiz": open("prototype/prompts/quiz_prompt.txt").read(),
    "summary": open("prototype/prompts/summary_prompt.txt").read(),
    "evaluate": "Evaluate the following answer.\nQuestion: {question}\nStudent Answer: {answer}\nProvide correctness (Yes/No), a score (out of 10), and feedback."
}

def call_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",
                "messages": [{"role": "user", "content": prompt}]
            },
            stream=True
        )
        output = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    output += chunk.get("message", {}).get("content", "")
                except Exception as e:
                    output += f" [stream error: {e}] "
        return output or "[No response from Ollama]"
    except Exception as e:
        return f"[Error calling Ollama: {str(e)}]"

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    response = ""
    questions = []
    evaluation = []
    answers = []

    if request.method == "POST":
        task = request.form["task"]
        user_input = request.form.get("input", "")


        if task == "evaluate":
            questions = session_data.get("questions", [])
            answers = []
            for i in range(len(questions)):
                answers.append(request.form.get(f"answer_{i}", ""))
            eval_results = []
            for q, a in zip(questions, answers):
                eval_prompt = TEMPLATES["evaluate"].format(question=q.strip(), answer=a.strip())
                result = call_ollama(eval_prompt)
                eval_results.append((q, a, result))
            evaluation = eval_results
        else:
            base_prompt = TEMPLATES[task]
            prompt = f"{base_prompt}\n\n{user_input}"
            response = call_ollama(prompt)
            if task == "quiz":
                questions = [q.strip() for q in response.split("\n") if q.strip()]
                session_data["questions"] = questions

    return render_template_string('\n<!DOCTYPE html>\n<html>\n<head>\n    <title>AutoTutor AI – Study Companion</title>\n    <style>\n        body { font-family: Arial, sans-serif; background: #f1f4f9; margin: 0; padding: 0; }\n        .header { background: #4a90e2; color: white; padding: 20px; text-align: center; }\n        .container { max-width: 800px; margin: 40px auto; background: white; border-radius: 10px; padding: 30px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }\n        label, select, textarea { display: block; width: 100%; margin-bottom: 15px; }\n        textarea { height: 100px; resize: vertical; }\n        input[type="submit"] { background: #4a90e2; color: white; padding: 12px 20px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }\n        pre { background: #f4f4f4; padding: 10px; border-left: 4px solid #4a90e2; white-space: pre-wrap; }\n        .footer { text-align: center; padding: 20px; font-size: 14px; color: #666; }\n    </style>\n</head>\n<body>\n    <div class="header">\n        <h1>🤖 AutoTutor AI – Study Companion</h1>\n        <p><strong>Developed by:</strong> Nithish Reddy Gangula </p>\n    </div>\n    <div class="container">\n        <form method="post">\n            <label for="task">Choose task:</label>\n            <select name="task">\n                <option value="tutor">Tutor</option>\n                <option value="quiz">Quiz</option>\n                <option value="summary">Summary</option>\n                <option value="evaluate">Evaluate Answers</option>\n            </select>\n\n            <label for="input">Enter your question/topic:</label>\n            <textarea name="input">{{ request.form.get(\'input\', \'\') }}</textarea>\n\n            <input type="submit" value="Generate">\n        </form>\n\n        {% if prompt %}\n        <h3>🧠 Prompt Sent to Model:</h3>\n        <pre>{{ prompt }}</pre>\n        <h3>🤖 AI Response:</h3>\n        <pre>{{ response }}</pre>\n        {% endif %}\n\n        {% if questions and request.form.get(\'task\') == \'quiz\' %}\n        <hr>\n        <form method="post">\n            <input type="hidden" name="task" value="evaluate">\n            <h3>📝 Enter Your Answers Below:</h3>\n            {% for q in questions %}\n                <label>{{ q }}</label>\n                <textarea name="answer_{{ loop.index0 }}"></textarea>\n            {% endfor %}\n            <input type="submit" value="Submit Answers for Evaluation">\n        </form>\n        {% endif %}\n\n        {% if evaluation %}\n        <hr>\n        <h3>📊 Evaluation Results:</h3>\n        {% for q, a, result in evaluation %}\n            <strong>Q:</strong> {{ q }}<br>\n            <strong>Your Answer:</strong> {{ a }}<br>\n            <strong>Feedback:</strong>\n            <pre>{{ result }}</pre>\n        {% endfor %}\n        {% endif %}\n    </div>\n\n    <div class="footer">\n        <p>© 2025 AutoTutor AI | Powered by Ollama + Flask</p>\n    </div>\n</body>\n</html>\n', 
                                  prompt=prompt, response=response,
                                  questions=session_data.get("questions", []),
                                  evaluation=evaluation)

if __name__ == "__main__":
    app.run(debug=True)
