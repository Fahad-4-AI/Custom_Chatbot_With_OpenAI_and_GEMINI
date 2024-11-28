# custom_data_chat_with_openai_and_gemini
# Flask Chatbot Project

This project is a Flask-based chatbot application that utilizes language models from various sources to provide responses to user queries. The chatbot supports multiple collection names and can switch between different language models, including OpenAI and Google Generative AI.

## Features

- User-friendly web interface for interacting with the chatbot.
- Supports different collection names for querying specific datasets.
- Integration with OpenAI and Google Generative AI for generating responses.
- Seamless switching between different language models.

## Project Structure

- `app.py`: Main Flask application file containing routes for handling user requests and responses.
- `index.html`: HTML file defining the structure of the web interface for the chatbot.
- `static/`: Directory containing static assets like CSS and JavaScript files.
- `templates/`: Directory containing HTML templates for Flask application rendering.
- `langchain/`: Directory containing modules for integrating with language models.
- `langchain_experimental/`: Directory containing experimental agent toolkits.
- `langchain_google_genai/`: Directory containing modules for integrating with Google Generative AI.
- `requirements.txt`: File listing the Python dependencies required for running the project.

## Usage

1. Install the required dependencies listed in `requirements.txt`.
2. Set up environment variables for API keys (e.g., `OPENAI_API_KEY`, `GOOGLE_API_KEY`).
3. Run the Flask application using `python app.py`.
4. Access the chatbot interface through the browser and interact with it by entering queries.

## Configuration

- `app.py`: Update environment variables for API keys and adjust parameters for language models.
- `index.html`: Modify the HTML structure or styles for the chatbot interface if needed.

## Dependencies

Ensure you have Python installed. Use `pip` to install the required dependencies:

```bash
- pip install -r requirements.txt
- python app.py
```
# Tools and Technologies Used:
- **Python 3.11.10:** Programming language for compatibility.
- **OpenAI API Key:** Enables OpenAI ChatBot integration.
- **GEMINI API Key:** Facilitates Gemini model integration.
- **Meta Account:** Required for Facebook/WhatsApp integration.
- **FAISS DB:** Stores data embeddings efficiently.
- **Flask:** Creates APIs for client access.
- **SQLite3 Database:** Stores historical data.
- **Mobile Number:** Links WhatsApp with ChatBot.
- **HTML, CSS, Jinja 2 Template:** Designs frontend interface.
- **Ngrok:** Interfaces with Meta account and demonstrates demo to client.
- **MongoDB:** Fetches data from database.


## Acknowledgments
This project is inspired by the capabilities of OpenAI's GPT-3.5 model and aims to demonstrate how it can be utilized in email-based conversational systems.

## License
This project is licensed under the ML1




