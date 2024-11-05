

import textwrap
from dotenv import load_dotenv
import PIL.Image
import google.generativeai as genai
import os

from IPython.display import Markdown

load_dotenv('.env')

basedir = os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER = os.path.join(basedir, 'static/images')


# Convert text to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Selecting google model
model = genai.GenerativeModel('gemini-1.5-flash')


# Ask AI
def ask_ai(question, image):
    img = PIL.Image.open(f'{IMAGE_FOLDER}/{image}')
    response = model.generate_content([question, img], stream=True)
    response.resolve()
    return response.text


# Delete images
def delete():
    images = os.listdir(IMAGE_FOLDER)
    for image in images:
        os.remove(f'{IMAGE_FOLDER}/{image}')


if __name__ == '__main__':
    delete()