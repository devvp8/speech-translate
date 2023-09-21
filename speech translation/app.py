from flask import Flask, request, render_template
import openai
import os
app = Flask(__name__)

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_audio():
    spokentext = request.form['spokenText']
    print(spokentext)

    prompt = f"""
        Translate the following text to English:
        ```
        {spokentext}
        ```
        """
    response=get_completion(prompt)
    print(response)
    return response

if __name__ == '__main__':
    app.run()
