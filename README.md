# Chatbot
This project is a Customer Data Platform (CDP) Support Agent Chatbot that can answer "how-to" questions related to four popular Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot scrapes the official documentation of these platforms to retrieve relevant information and guide users on how to perform specific tasks or achieve specific outcomes.

#Features:
  Answer "How-to" Questions: Users can ask questions related to tasks in Segment, mParticle,       Lytics, and Zeotap, and the chatbot will provide relevant links or instructions from the official documentation.
  Web Scraping: The chatbot extracts relevant information from the official documentation websites of the four platforms.
  Natural Language Processing (NLP): The chatbot uses spaCy's NLP model to understand and classify user queries.
  Cross-CDP Comparison: The chatbot can provide comparisons between the platforms (e.g., how audience creation differs between Segment and Lytics).
  User-Friendly Web Interface: The chatbot is accessible through a simple web interface powered by Flask.


#Installation:
Prerequisites

Python 3.x

Install the following Python libraries:

Flask: Web framework to handle HTTP requests.

Requests: For making HTTP requests to fetch documentation.

BeautifulSoup4: For web scraping the documentation.

spaCy: For natural language processing (NLP).

#Steps to Install:

1)Clone the repository (or download the code files):

  git clone https://github.com/yourusername/cdp-support-agent-chatbot.git
  
  cd cdp-support-agent-chatbot
  
2)Install the required dependencies:

  pip install requests beautifulsoup4 spacy Flask

3)Download the spaCy NLP model:
  python -m spacy download en_core_web_sm

#Running the Application
1)Start the Flask web server:
  python chatbot.py

2)Once the server is running, the chatbot will be available at http://127.0.0.1:5000


#How to Use the Chatbot
Querying the Chatbot
You can query the chatbot by sending a GET request to the /ask endpoint with a query parameter. For example:

Example URL: http://127.0.0.1:5000/ask?query=How+do+I+set+up+a+new+source+in+Segment?
Sample Response
The chatbot will return a JSON response with the relevant documentation or an error message. For example:
{
  "answer": "Here's the link to the relevant documentation: https://segment.com/docs?ref=nav"
}
