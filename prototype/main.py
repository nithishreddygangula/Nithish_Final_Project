
import requests

# Load the correct prompt template
def load_prompt(prompt_type):
    with open(f"prototype/prompts/{prompt_type}_prompt.txt", "r") as f:
        return f.read()

# Corrected: Call local Ollama model using streaming chat API
def call_ollama_chat(prompt):
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
                    chunk = eval(line.decode("utf-8"))
                    output += chunk.get("message", {}).get("content", "")
                except Exception as e:
                    output += f"\n[stream error: {e}]"
        return output or "[No output from Ollama]"
    except Exception as e:
        return f"[Error calling Ollama: {str(e)}]"

def main():
    print("🤖 Welcome to AutoTutor AI")
    print("Choose task:")
    print("  1. Ask a Tutor Question")
    print("  2. Generate a Quiz")
    print("  3. Summarize Content")
    choice = input("Enter choice (1/2/3): ").strip()

    prompt_map = {"1": "tutor", "2": "quiz", "3": "summary"}
    if choice not in prompt_map:
        print("❌ Invalid choice.")
        return

    user_input = input("Enter your topic or question:\n> ").strip()
    prompt_type = prompt_map[choice]
    base_prompt = load_prompt(prompt_type)

    full_prompt = f"{base_prompt}\n\n{user_input}"

    print("\n📤 Sending prompt to Ollama...")
    ai_response = call_ollama_chat(full_prompt)

    print("\n🧠 Prompt Used:")
    print("-" * 50)
    print(full_prompt)
    print("-" * 50)

    print("\n🤖 AutoTutor AI Says:\n")
    print(ai_response)

if __name__ == "__main__":
    main()
