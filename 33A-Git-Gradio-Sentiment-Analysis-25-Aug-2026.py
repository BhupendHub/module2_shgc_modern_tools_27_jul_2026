import __________ as gr
from transformers import pipeline
#Fn Definition - Pass Text, Model and HF Token
def analyze_sentiment(text, model_name, hf_token):
    # Fallback to default model if input is empty
    if not model_name.strip():
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    # Clean token input
    token = hf_token.strip() if hf_token.strip() else None
    try:
        # Initialize pipeline dynamically with specified model and token
        classifier = pipeline(
            task="sentiment-analysis", model=model_name, token=token
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
    fn=analyze_sentiment,
    inputs=[
        gr.Textbox(label="Input Text",lines=3, 
            placeholder="Type your sentence here to analyze...",
        ),
        gr.Textbox(
            label="Hugging Face Model Name",
            value="distilbert-base-uncased-finetuned-sst-2-english",
            placeholder="e.g., cardiffnlp/twitter-roberta-base-sentiment",
        ),
        gr.Textbox(
            label="Hugging Face Token (Optional)",placeholder="hf_...",
            type="password",  # Hides token characters from view
        ),
    ],
    outputs=gr.Textbox(label="Analysis Result"),
    title="Dynamic HF Sentiment Analyzer",
    description="Enter text along with any Hugging Face model and access token to evaluate sentiment.",
)
# Launch the local web server
if __name__ == "__main__":
    interface.___________(prevent_thread_lock=False)
