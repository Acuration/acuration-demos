import os
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
import string

def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize words and remove punctuation
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    
    return sentences, stemmed_words

def summarize_text(text):
    sentences, words = preprocess_text(text)
    
    # Frequency distribution of words
    freq_dist = FreqDist(words)
    
    # Get the most frequent words
    most_common = freq_dist.most_common(10)  # Adjust the number of words in the summary
    
    # Generate the summary
    summary = [word[0] for word in most_common]
    
    return ' '.join(summary)

def summarize_and_save_text_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith("_extracted_text.txt"):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                # Summarize the text
                summary = summarize_text(text)
                # Save the summary to a new file in the output folder
                summary_filename = "summary_" + filename
                with open(os.path.join(output_folder, summary_filename), 'w', encoding='utf-8') as summary_file:
                    summary_file.write(summary)

# Define your input and output folders
input_folder = r'D:\Varshith\S\Acuration\Task1\acuration-demos\Code\storage'
output_folder = r'D:\Varshith\S\Acuration\Task1\acuration-demos\Code\summary_output'
  # Replace with the folder where you want to save summarized text files

# Call the function to summarize text files in the input folder and save the summaries to the output folder
summarize_and_save_text_files(input_folder, output_folder)
