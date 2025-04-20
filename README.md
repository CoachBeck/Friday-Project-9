# AI Completion GUI Project - Setup Instructions

## How to Set Up

1. Clone or download this project from GitHub.

2. In the project folder, create a new file named `.env`

3. Inside the `.env` file, paste this line:

   OPENAI_API_KEY=your-api-key-here

   - Replace `your-api-key-here` with your own OpenAI API key.
   - Do NOT include any spaces or quotation marks.
   - Example:

     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

4. Save the `.env` file.

5. Make sure you have Python installed with the following packages:
   - openai
   - python-dotenv
   - tkinter (comes with standard Python install)

   To install missing packages, run:
    pip install openai python-dotenv


6. Finally, run the program:


Now you can enter a prompt into the app and get a response from GPT-4o!
