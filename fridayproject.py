import tkinter as tk
from tkinter import scrolledtext
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def get_completion():
    user_prompt = prompt_entry.get()
    if not user_prompt.strip():
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Please enter a prompt!")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150
        )
        completion_text = response.choices[0].message.content.strip()

        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, completion_text)

    except Exception as e:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, f"Error: {e}")

# Set up GUI
window = tk.Tk()
window.title("AI Completion Generator")

# Prompt Label and Entry
prompt_label = tk.Label(window, text="Enter your prompt:")
prompt_label.pack(pady=5)

prompt_entry = tk.Entry(window, width=70)
prompt_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(window, text="Submit", command=get_completion)
submit_button.pack(pady=5)

# Output Box
output_label = tk.Label(window, text="Completion Output:")
output_label.pack(pady=5)

output_box = scrolledtext.ScrolledText(window, height=15, width=80)
output_box.pack(pady=5)

# Run the application
window.mainloop()
