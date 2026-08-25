import gradio as gr
from transformers import pipeline
import os
from dotenv import load_dotenv

# 1. Load the hidden environment variables from the .env file
load_dotenv()

# 2. Retrieve the token securely
huggingface_token = os.getenv("HF_TOKEN")
#model_file="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
model_file="./bert_english_model"


def analyze_sentiment(text, model_name=model_file, hf_token=huggingface_token):
    # Fallback to default model if input is empty
    if not model_name.strip():
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    # Clean token input
    token = hf_token.strip() if hf_token.strip() else None

    try:
        # Initialize pipeline dynamically with specified model and token
        classifier = pipeline(
            task="sentiment-analysis", model=model_name, token=token, local_files_only=False
        )

        # Run inference
        prediction = classifier(text)[0]
        label = prediction["label"]
        score = round(prediction["score"], 4)

        return f"Label: {label}\nConfidence Score: {score}"

    except Exception as e:
        return f"Error initializing model: {str(e)}"


# Define the Gradio Interface layout
interface = gr.Interface(
    ______________=analyze_sentiment,
    _________=[
        gr.Textbox(
            label="Input Text",
            placeholder="Type your sentence here to analyze...",
            lines=3,
        ),
        gr.Textbox(
            label="Hugging Face Model Name",
            value=model_file,
            placeholder="e.g., cardiffnlp/twitter-roberta-base-sentiment",
        ),
        gr.Textbox(
            label="Hugging Face Token (Optional)",
            placeholder="hf_...",
            type="password",  # Hides token characters from view
            value=huggingface_token
        ),
    ],
    ________=gr.Textbox(label="Analysis Result"),
    title="Dynamic HF Sentiment Analyzer",
    description="Enter text along with any Hugging Face model and access token to evaluate sentiment.",
)

# Launch the local web server
if __name__ == "__main__":
    interface.launch(prevent_thread_lock=False)
