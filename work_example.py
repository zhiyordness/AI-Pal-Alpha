from tkinter import *
import groq

root = Tk()

root.title('AI-Pal Alpha')
root.geometry('1500x1200')

canvas = 

lbl = Label(root, text = '')

lbl.grid()
root.mainloop()


client = groq.Client(api_key="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")  # Replace with your actual API key

def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print("AI:", response)