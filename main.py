import openai

openai.api_key = "YOUR_API_KEY"

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    print("\nAI Output:\n", generate_text(user_input))
