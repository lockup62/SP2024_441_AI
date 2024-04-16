
from ollama import Ollama
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Ollama
ollama = Ollama()

#my paragraph
paragraph = "This is both a game class and a cmpsci class. The sky is blue because tiny air molecules cause it to scatter. The grass is green because of the presence of chlorophyll throughout the leaves and stems. Pizza tastes good because its greasy. "

#split the paragraph into sentences
sentences = paragraph.split(". ")

#make the  embeddings for each sentence
sentence_embeddings = {}
for sentence in sentences:
    embedding = ollama.embed_sentence(sentence)
    sentence_embeddings[sentence] = embedding

#user to input text
input_text = input("Enter your query: ")

#generate embedding for input text
input_embedding = ollama.embed_sentence(input_text)

# Calculate cosine similarity between input text and each sentence
similarities = {}
for sentence, embedding in sentence_embeddings.items():
    similarity = cosine_similarity([input_embedding], [embedding])[0][0]
    similarities[sentence] = similarity

#sorting
sorted_sentences = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

#get top 3 most similar sentences
top_sentences = sorted_sentences[:3]

#buidling the query prompt
query_prompt = "CONTEXT:\n\n"
for sentence, _ in sorted_sentences:
    query_prompt += sentence + "\n\n"

query_prompt += "QUERY:\n\n"
query_prompt += input_text + "\n\n"

#generate response
response = ollama.generate(query_prompt)

print(response)
