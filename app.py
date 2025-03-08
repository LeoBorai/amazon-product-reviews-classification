import gradio as gr
import pickle

from sklearn.feature_extraction.text import CountVectorizer

model = pickle.load(open('model.pkl', 'rb'))

def perform(text):
  vectorizer = CountVectorizer()
  text_input = vectorizer.transform([text])
  score = model.predict(text_input)[0]

  return score

demo = gr.Interface(fn=perform,
  inputs=[gr.Textbox(label="Message")],
  outputs=gr.Textbox(label="Score"))

demo.launch()