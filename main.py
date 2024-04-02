import tkinter as tk
import re

# Define patterns and corresponding responses
patterns = {
    r'.*(hi|hello).*': 'Hello! How can I assist you today?',
    r'.*(how are you|how are you doing).*': 'I am doing well, thank you for asking. How can I help you?',
    r'.*(help|support).*': 'Sure, what do you need help with?',
    r'.*(order|place an order).*': 'To place an order, please visit our website or call our customer service.',
    r'.*(delivery|shipping).*': 'For information about delivery or shipping, please visit our website or contact customer service.',
    r'.*(return|refund).*': 'To initiate a return or request a refund, please check our return policy on our website.',
    r'.*(product|item).*': 'We offer a wide range of products. What specific product are you interested in?',
    r'.*(contact|customer service).*': 'You can contact our customer service department at 1-800-123-4567.',
    r'.*(bye|goodbye).*': 'Goodbye! Have a great day!',
}

def chatbot_response(user_input):
    # Iterate over patterns to find a match
    for pattern, response in patterns.items():
        if re.match(pattern, user_input.lower()):
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def send_message():
    user_input = entry.get()
    response = chatbot_response(user_input)
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, "You: " + user_input + "\n", 'user_msg')
    text_area.insert(tk.END, "Bot: " + response + "\n\n", 'bot_msg')
    text_area.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create GUI
root = tk.Tk()
root.title("ChatBot")
root.configure(bg='lightgray')

frame = tk.Frame(root, bg='lightgray')
frame.pack(padx=10, pady=10)

text_area = tk.Text(frame, height=20, width=50, bg='pink')
text_area.tag_config('user_msg', foreground='blue')
text_area.tag_config('bot_msg', foreground='green')
text_area.pack(side=tk.LEFT, fill=tk.Y)
text_area.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message, bg='blue', fg='white')
send_button.pack()

root.mainloop()
