# 🚀 Simple Flask Application

A basic web application built using Flask (Python micro web framework).

------------------------------------------------------------------------

## 📌 About

This project demonstrates: - Basic Flask setup - Simple route handling -
Running a development server - Using virtual environment - Managing
dependencies

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.x
-   Flask

------------------------------------------------------------------------

## 📂 Project Structure

flask-project/ 
│ 
├── app.py 
├── requirements.txt 
├── .gitignore 
└── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/Shashant07/flask_learning_first_project.git
cd flask_learning_first_project

### 2️⃣ Create Virtual Environment

python -m venv venv

Activate virtual environment:

Windows:
.venv\Scripts\activate		//cmd
.\venv\Scripts\activate.bat 	//Power shell.


Mac/Linux: source venv/bin/activate

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available:

pip install flask

------------------------------------------------------------------------

### 4️⃣ Run the Application

python app.py

OR

flask run

------------------------------------------------------------------------

## 🌐 Access the Application

Open your browser and visit:

http://127.0.0.1:5000

------------------------------------------------------------------------

## 📄 Example app.py

``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

------------------------------------------------------------------------

## 📦 Generate requirements.txt

pip freeze \> requirements.txt

------------------------------------------------------------------------

## 🔐 Notes

-   Keep .env file in .gitignore
-   Do not commit secret keys
-   Use debug=True only in development

------------------------------------------------------------------------

## 👨‍💻 Author

Shashant pandit
GitHub: https://github.com/shashant07

------------------------------------------------------------------------

⭐ Feel free to fork, improve, and build upon this project!
