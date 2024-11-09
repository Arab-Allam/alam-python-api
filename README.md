## Overview
This the backend code for the game, built using Python and Flask.


## Steps to Run the Flask Model

### 1. **Install Python**
   If you don’t already have Python installed, download and install Python from the official website:
   - [Download Python](https://www.python.org/downloads/)

   After installation, verify Python is installed by running the following in your terminal:
   ```bash
   python --version
   ```

### 2. **Install Flask**
   Install Flask using `pip` by running the following command:
   ```bash
   pip install flask
   ```

### 3. **Install Required Python Libraries**
   - **PyArabic**: A library for Arabic language processing.
     ```bash
     pip install pyarabic
     ```

   - **IBM Watson AI Library**: If you're using IBM Watson AI for your model.
     ```bash
     pip install ibm-watsonx-ai
     ```

### 4. **Run the Flask API**
   To start the Flask API, run the following command in the directory where your `flask_api.py` file is located:
   ```bash
   python flask_api.py
   ```

### 5. **Get the Flask Server IP**
   After starting the Flask server, you'll see something like this in the terminal:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

   Take note of the IP address (in this case, `http://127.0.0.1:5000`). This will be used for sending API requests.
