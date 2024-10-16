from keras.models import load_model
import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
import gradio as gr

model = load_model("sentiment_analysis_model.h5")
tokenizer = joblib.load("tokenizer.pkl")

def predictive_system(review):
    sequences = tokenizer.texts_to_sequences([review])
    paded_sequences = pad_sequences(sequences,maxlen=200)
    prediction = model.predict(paded_sequences)
    sentiment = "positive" if prediction[0][0] > 0.5 else "negative"
    return sentiment  

title = "IMDB Sentiment Analysis By Krishi Devani"
app= gr.Interface(fn=predictive_system,inputs="textbox",outputs = "textbox",title=title)
app.launch(share=True)