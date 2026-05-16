🚀 Flask Basic Application

A simple Flask web application built using Python.
This project demonstrates basic routing and server setup.

📌 Features
Simple Flask server
Basic routing
Development mode enabled
Easy project structure
🛠 Tech Stack
Python 3.x
Flask
📂 Project Structure
flask-project/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/flask-project.git
cd flask-project
2️⃣ Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

If you don't have requirements.txt, install Flask manually:

pip install flask
4️⃣ Run the Application
python app.py

Or using Flask command:

flask run
🌐 Access the App

Open your browser and go to:

http://127.0.0.1:5000
📄 Example app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
🧪 Development Notes
debug=True enables auto reload.
Use .env file to manage environment variables.
Never commit secrets to GitHub.
📦 Create requirements.txt

After installing packages:

pip freeze > requirements.txt
👨‍💻 Author

Shashant Pandit
GitHub: https://github.com/shashant07