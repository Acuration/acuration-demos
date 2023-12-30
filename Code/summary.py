import os
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re

# Specify the input folder path
input_folder_path = r'D:\Varshith\S\Acuration\Task1\acuration-demos\Code\ext'

# Create a new folder for storing the summaries
output_folder_path = r'D:\Varshith\S\Acuration\Task1\acuration-demos\Code\summ'
os.makedirs(output_folder_path, exist_ok=True)

# Load the summarization pipeline with a model that supports long sequences
model_name = "sshleifer/distilbart-cnn-12-6"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

c = 0

# Iterate through each file in the input folder
for filename in os.listdir(input_folder_path):
    input_file_path = os.path.join(input_folder_path, filename)
    # Print the current file being processed
    print(f"Processing file: {input_file_path}")

    # Read the content of the text file
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_text = input_file.read()

    # Tokenize the input text
    input_tokens = tokenizer(input_text, truncation=True, return_tensors="pt")

    # Convert tensor to string
    input_text_str = tokenizer.decode(input_tokens["input_ids"][0], skip_special_tokens=True)

    # Set max_length dynamically based on the length of the input text
    max_len = len(input_tokens["input_ids"][0])-10

    # Generate summary using the pipeline
    summary = summarizer(input_text_str, max_length=max_len-1, min_length=0, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Extract the summary text
    summary_text = summary[0]['summary_text']

    # Write the summary to a new file in the output folder
    output_filename = f"{filename.split('.')[0]}_summary.txt"
    output_file_path = os.path.join(output_folder_path, output_filename)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        summary_text = re.sub(r'[^\x00-\x7F]+', '', summary_text)
        output_file.write(summary_text)
        c += 1

print("Summarization complete. Summaries saved in:", output_folder_path)
print(c)