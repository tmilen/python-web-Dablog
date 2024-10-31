# Da Blog 🐼

[Visit the live website](https://dablog.onrender.com/)

**Da Blog** is a simple web application where users can add and view blog entries. This project demonstrates basic CRUD functionality and serves as a mini blog platform using Flask, MongoDB, HTML, and CSS.

## 🌟 Features

- **Add New Entries**: Users can create and submit new blog entries.
- **View Recent Posts**: All recent blog entries are displayed on the main page.
- **Responsive Layout**: The layout adjusts for better usability on various screen sizes.

## ⚙️ Tech Stack

### Backend
- **Flask**: Used as the web framework to handle routes and server-side logic.
- **MongoDB Atlas**: MongoDB is the database used for storing blog entries. MongoDB Atlas provides a fully managed cloud database.
- **MongoDB Compass**: Connected to MongoDB Atlas cluster for easy data management and monitoring.

### Frontend
- **HTML & CSS**: Simple HTML and CSS for creating a clean and user-friendly interface.

- ## 📂 Project Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tmilen/python-web-Dablog.git
   cd python-web-Dablog

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Set up MongoDB Atlas**:
    - Create a MongoDB Atlas account and set up a cluster.
    - Connect MongoDB Compass to your Atlas cluster for easier management.
    - Create `.env` file and create `MONGODB_URI` variable and set its value to the connection string.
    
4. **Run the application: First, set the Flask application environment variable**:
    - On Windows:
      ```bash
      set FLASK_APP=app.py
      
    - On MacOS/Linux:
      ```bash
      exports FLASK_APP=app.py

    Then, run the application:
     ```bash
     flask run
