import os
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",  # Directly using the key for this example
)

# Function to get a recipe from Groq API based on the user's vegetable input
def generate_recipe(vegetables):
    # Convert the list of vegetables to a comma-separated string for the prompt
    vegetables_str = ", ".join(vegetables)
    
    # Create the prompt for recipe generation
    prompt = f"Create a recipe using the following vegetables: {vegetables_str}"

    # Call the Groq API to generate the recipe
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    # Extract the recipe from the response
    recipe = chat_completion.choices[0].message.content
    return recipe

# Main program to take user input for vegetables
if __name__ == "__main__":
    # Ask the user to input vegetables separated by commas
    user_input = input("Enter vegetables (separate them by commas): ")
    
    # Convert the input string to a list of vegetables
    vegetables_list = [veg.strip() for veg in user_input.split(",")]
    
    # Generate the recipe
    recipe = generate_recipe(vegetables_list)
    
    # Print the generated recipe
    print("\nGenerated Recipe:")
    print(recipe)
