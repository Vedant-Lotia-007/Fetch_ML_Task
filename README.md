# Fetch Rewards Machine Learning Exercise

This exercise encompasses the design and implementation of a predictive machine learning model alongside a web application, aimed at estimating the monthly volume of scanned receipts for Fetch Rewards. The model leverages historical data from 2021 to forecast trends and patterns for 2022. The web app facilitates user interaction, allowing for the visualization and retrieval of predictive insights with ease. The end-to-end solution demonstrates a practical application of machine learning techniques in a business context, emphasizing predictive analytics and user experience.

## Description

This repository is part of the Fetch Rewards Take-home Exercise for a Machine Learning Engineer position. It contains a machine learning model and a web application for predicting the monthly number of scanned receipts for Fetch Rewards, using historical data from the year 2021.

## Getting Started



### Dependencies

- Python 3.8+
- Required Python libraries as listed in `requirements.txt`


### Installing

1. Clone this repository:
   ```sh
   git clone https://github.com/Vedant-Lotia-007/Fetch_ML_Task.git
   ```
2. Navigate the repository directory:
   ```sh
   cd Fetch_ML_Task
   ```
3. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```


### Executing the program

1. Run the application:
   ```sh
   python app.py
   ```
2. Access the application through a web browser at:
   ```sh
   http://localhost:5000
   ```



### Using the application

- The web UI allows users to select a future month of 2022 and predict the number of receipts that will be scanned. One could also view the whole year prediction.
- Follow the on-screen instructions to submit your query and view the predictions.


### Docker Container 

1. Build the Docker image:
   ```sh
   docker build -t fetch-receipts-prediction-app .
   ```
2. Run the Docker container:
   ```sh
   docker run -p 5000:5000 fetch-receipts-prediction-app
   ```


### Author

- Vedant Lotia


## Contact
For any questions or clarifications, feel free to reach out at vedantlotia007@gmail.com or raise an issue on this GitHub repository.
