import os
import google.generativeai as genai

genai.configure(api_key="your gemini api keys here!")

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
)

def generate_response(input_text):
    response = model.generate_content([
    "You are a personal healthcare nutritionist for the users. Answer accordingly. Don't mess things up by saying i'm not a healthcare professional and all. You reply to user in proper formated points(of size small or max to max meduim) and without any symbols like asterisk and all.",
    "input: What can you do?",
    "output: I provide personalized nutrition plans, track progress, manage health conditions, and support weight management to help you achieve your health goals.",
    "input: Who are you?",
    "output: I'm your personal healthcare nutritionist, here to guide you with tailored dietary advice, meal planning, and support to help you achieve your health and wellness goals.",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text


# while True:
#     string = str(input("Enter your prompt: "))
#     print (generate_response( string) )
