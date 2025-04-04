from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Select model
model_name = "microsoft/phi-2"

# Log device info
device = "mps" if torch.backends.mps.is_available() else "cpu"
print("Torch device:", device)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model on CPU for stability
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32  # Use float32 to avoid NaNs/Infs
)
model.to("cpu")  # Force CPU

# Create text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Chat function
def chat(prompt):
    response = generator(
        prompt,
        max_new_tokens=60,        # Keep it light for fast generation
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )
    return response[0]['generated_text']
