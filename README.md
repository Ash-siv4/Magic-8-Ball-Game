# Magic 8-Ball Web Application

This project is a simple web-based Magic 8-Ball game that provides random responses to user questions. It uses a Python Flask backend to handle the logic and a frontend built with HTML, CSS, and JavaScript for user interaction.

## Features

- **Ask Questions**: Users can type in their questions and receive random responses.
- **Interactive UI**: Simple and intuitive user interface.
- **Python Backend**: The backend logic is handled by a Python Flask server.
- **Static Frontend**: The frontend is built using HTML, CSS, and JavaScript.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/magic-8-ball.git
   cd magic-8-ball
   ```
2. **Install Dependencies**:
   ```bash
   pip install flask
   ```

## Running the Application

1. **Start the Flask Server**:
   ```bash
   python app.py
   ```
2. **Open Your Browser**:
   Navigate to `http://127.0.0.1:5000` in your web browser.

## Project Structure

```bash
/magic-8-ball
│
├── app.py             # Flask backend
└── static
    ├── index.html     # HTML file for the frontend
    ├── styles.css     # CSS file for styling
    └── script.js      # JavaScript file for frontend logic
```

## API Endpoints

- POST /shake

  - Request Body: JSON object with a `question` field.
  - Response: JSON object with a `response` field containing the Magic 8-Ball's answer.

Example:

```bash
curl -X POST http://127.0.0.1:5000/shake -H "Content-Type: application/json" -d '{"question": "Will it rain today?"}'
```

Response:

```json
{
  "response": "Outlook good."
}
```

## How It Works

1. The user types a question into the input field and clicks the "Shake" button.
2. The frontend sends a POST request to the Flask backend with the user's question.
3. The backend selects a random response from a predefined list and sends it back to the frontend.
4. The frontend displays the response to the user.

## Author

[Aswene Sivaraj](https://github.com/Ash-siv4/)
