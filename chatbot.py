import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import spacy

# Initialize spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)

# Function to search the documentation of Segment
def search_segment(query):
    url = 'https://segment.com/docs/?ref=nav'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find relevant links or sections based on the query
    links = soup.find_all('a', string=lambda text: query.lower() in text.lower() if text else False)

    if links:
        return links[0].get('href')
    return "No relevant information found in Segment documentation."

# Function to search the documentation of mParticle
def search_mparticle(query):
    url = 'https://docs.mparticle.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', string=lambda text: query.lower() in text.lower() if text else False)

    if links:
        return links[0].get('href')
    return "No relevant information found in mParticle documentation."

# Function to search the documentation of Lytics
def search_lytics(query):
    url = 'https://docs.lytics.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', string=lambda text: query.lower() in text.lower() if text else False)

    if links:
        return links[0].get('href')
    return "No relevant information found in Lytics documentation."

# Function to search the documentation of Zeotap
def search_zeotap(query):
    url = 'https://docs.zeotap.com/home/en-us/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', string=lambda text: query.lower() in text.lower() if text else False)

    if links:
        return links[0].get('href')
    return "No relevant information found in Zeotap documentation."

# Function to classify the query and route it to the right documentation
def handle_query(query):
    # Use NLP model to understand the query
    doc = nlp(query.lower())
    
    if 'segment' in query.lower():
        return search_segment(query)
    elif 'mparticle' in query.lower():
        return search_mparticle(query)
    elif 'lytics' in query.lower():
        return search_lytics(query)
    elif 'zeotap' in query.lower():
        return search_zeotap(query)
    else:
        return "Sorry, I can only answer questions related to Segment, mParticle, Lytics, and Zeotap."

# Define Flask route for handling user queries
@app.route('/ask', methods=['GET'])
def ask_question():
    query = request.args.get('query')  # Get the user's query from URL parameters
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Handle the query and get the answer
    answer = handle_query(query)
    return jsonify({"answer": answer})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
