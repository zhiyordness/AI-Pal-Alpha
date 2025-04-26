from tkinter import *
import groq

# GUI Setup
root = Tk()
root.geometry("700x500")
root.title("AI-Pal Alpha")

BG_GRAY = "#FFF5EE"
BG_COLOR = "#D2B48C"
TEXT_COLOR = "#000000"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Replace with your actual API key
client = groq.Client(api_key="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")

def send_message():
    global e  # Add this line
    user_input = e.get().lower()
    txt.insert(END, f"\nYou: {user_input}")
    e.delete(0, END)  # Clear the input field after sending

    if user_input in ["exit", "quit", "bye"]:
        txt.insert(END, "\nGoodbye!")
        root.destroy()  # Exit the application
        return

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        ai_response = response.choices[0].message.content
        txt.insert(END, f"\nAI: {ai_response}")
    except Exception as e:
        txt.insert(END, f"\nError: {e}")

    # Ensure the text widget scrolls to the bottom
    txt.see(END)
    root.update_idletasks()


def clear_chat():
    txt.delete(1.0, END)



# GUI Elements
welcome_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR,
                      text="Welcome to your AI chatbot! Type 'exit' to quit.",
                      font=FONT_BOLD, pady=10, width=60, height=1)
welcome_label.grid(row=0, column=0, columnspan=3)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=86, height=20)
txt.grid(row=1, column=0, columnspan=3)

# Configure Scrollbar
scrollbar = Scrollbar(root, orient="vertical", command=txt.yview)
scrollbar.grid(row=1, column=3, sticky="ns")
txt.configure(yscrollcommand=scrollbar.set)

e = Entry(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=75)
e.grid(row=2, column=0, columnspan=2)

send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                     command=send_message)
send_button.grid(row=2, column=2)

clear_button = Button(root, text="Clear", font=FONT_BOLD, bg=BG_GRAY,
                      command=clear_chat)
clear_button.grid(row=3, column=0, columnspan=2)

root.mainloop()