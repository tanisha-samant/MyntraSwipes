# Myntra Swipes
MyntraSwipes is a web application that combines the functionalities of Myntra and Tinder. Users can swipe through different outfits and get personalized recommendations based on their preferences. The application features a React.js frontend, a Flask API backend, and a machine learning model to provide recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)


## Introduction

MyntraSwipes is designed to enhance the shopping experience by allowing users to swipe through various outfits, similar to how users swipe on Tinder. The app utilizes a machine learning model to offer personalized outfit recommendations based on user preferences.

## Features

- Swipe functionality to browse outfits.
- Personalized recommendations based on user swipes.
- Responsive design for optimal viewing on different devices.
- Easy-to-navigate interface.

## Technologies Used

- **Frontend:** React.js, react-tinder-card
- **Backend:** Flask, Flask-CORS
- **Machine Learning:** Python, Scikit-learn
- **Others:** Node.js, Axios

## Installation

### Prerequisites

- Node.js and npm installed
- Python and pip installed

### Backend Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/myntra-swipes.git
   cd myntra-swipes/backend
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   .\venv\Scripts\activate   # For Windows
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```sh
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd ../frontend
   ```

2. Install the required packages:
   ```sh
   npm install
   ```

3. Start the React application:
   ```sh
   npm start
   ```

## Usage

1. Ensure the backend server is running.
2. Open your web browser and navigate to `http://localhost:3000`.
3. Swipe through the outfits and get personalized recommendations.


## Contributors
-Rithika Malve
-Tanisha Samant

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
