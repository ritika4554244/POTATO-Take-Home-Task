# POTATO Take Home Task

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](URL-to-build) 
[![dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](URL-to-dependencies)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🥔 Overview
This project implements a Flask-based API that queries a dataset of tweets and provides insights such as the number of tweets containing a term, the number of unique users, tweet timings, and more. The API is optimized for quick responses and is designed to be deployed in a Docker container for ease of use.

### Queries
- How many tweets were posted containing the term on each day?
- How many unique users posted a tweet containing the term?
- Average likes on tweets containing the term.
- Locations (place IDs) where the tweets came from.
- Times of day the tweets were posted.
- The user who posted the most tweets with the term.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Search tweets by terms.
- Analyze how many tweets contain a specific term each day.
- JSON file output.
- Calculate average likes for tweets containing the term.
- Identify locations from which tweets originated.
- Analyze the timing of tweets.
- Data visualization for better insights (if applicable).

---

## Libraries

This project uses the following libraries:

- **Flask**: A micro web framework for Python, used for building the API.
- **Pandas**: A powerful data manipulation and analysis library for Python, used for handling the tweet dataset.
- **NumPy**: A library for numerical computing in Python, often used with Pandas for data manipulation.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations in Python.
- **Docker**: A platform for developing, shipping, and running applications inside containers.

Make sure to install the required libraries by running:

```bash
pip install -r requirements.txt
```


## 📁 File Structure
```plaintext
📂 POTATO-Take-Home-Task
│
├── templates/
│   └── home.html             # Simple frontend for query input
├── Dataset/
│   ├── cleaned.tsv           # ETL performed tweet dataset (used for querying)
│   └── twitter.tsv           # Original dataset 
├── app.py                    # Main Flask application
├── Dockerfile                # Dockerfile to build the project image
├── requirements.txt          # Python dependencies
└── data_stats.ipynb         # Jupyter notebook for dataset analysis

```

## Installation

### Clone the Repository
```bash
git clone git@github.com:ritika4554244/POTATO-Take-Home-Task.git
cd POTATO-Take-Home-Task
```

## Set Up Python Environment
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

## Run the Application

You can run the Flask application directly:

```bash
python app.py
```
## Application Screenshot

Here’s a screenshot of the application in action:

![Screenshot of the Application](Output_Images/screenshot.png)

![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)
![Screenshot of the Application](Output_Images/screenshot.png)









