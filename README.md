This Python project generates recipes based on a list of vegetables provided by the user, using the Groq API to generate the recipe content. The Groq API (powered by advanced language models) is used to create a recipe using the ingredients (vegetables) input by the user in the command terminal of the system.

Steps:
1. Clone the repository:
   git clone https://github.com/cloaked-carnage/Recipe-generator.git
3. Install the required dependencies:
   pip install groq gradio
4. Run the python code
   python app.py
5. The program will prompt you to enter a list of vegetables. For example:
   Enter vegetables (separate them by commas): carrot, tomato, spinach
6. The program will then call the Groq API and generate a recipe based on the input vegetables.
7. The generated recipe will be displayed on the terminal.

