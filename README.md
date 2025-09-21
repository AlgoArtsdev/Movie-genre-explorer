# 🎬 Movie Genre Explorer

A simple desktop application built with Python that allows users to explore the MovieLens dataset. You can search for movies by genre and instantly see a list of matching titles.

This project was built as an introduction to data handling with Pandas and GUI development with PySimpleGUI.

![Screenshot of the Movie Genre Explorer application](https://i.imgur.com/I7lZve0.png)

## ✨ Features

* **Genre-Based Search:** Quickly filter thousands of movies by a specific genre (search is case-insensitive).
* **Simple Interface:** An easy-to-use graphical user interface, no command line needed.
* **Fast & Lightweight:** Loads the data once at the start and performs searches instantly.

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **Pandas:** For loading and filtering the movie data from the CSV file.
* **PySimpleGUI:** For building the simple and responsive graphical user interface.

## 🚀 How to Run the Project

To run this application on your local machine, please follow these steps:

**1. Prerequisites:**
You must have Python installed on your system.

**2. Get the Code:**
You can either clone the repository using Git or download it as a ZIP file.

* **Option A: Clone with Git (Recommended)**
    Open your terminal or command prompt and run this command:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```

* **Option B: Download ZIP**
    On the GitHub repository page, click the green "Code" button and select "Download ZIP". Unzip the file on your computer.

**3. Navigate to the Project Directory:**
Using your terminal, move into the folder you just cloned or unzipped:
```bash
cd YOUR_REPOSITORY_NAME
```

**4. Install Required Libraries:**
Run the following command to install the necessary Python libraries:
```bash
pip install pandas PySimpleGUI
```

**5. Place the Dataset:**
This application requires the movies.csv file from the MovieLens Small dataset. Download the dataset, find the movies.csv file, and place it in the same folder as the Python script.

**6. Run the Application:**
```bash
python your_script_name.py
```