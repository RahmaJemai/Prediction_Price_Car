<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Price Prediction Project Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2 {
            color: #333;
        }
        p {
            margin: 0 0 10px 0;
        }
    </style>
</head>
<body>
    <h1>Car Price Prediction Project Overview</h1>

    <h2>1. Data Collection:</h2>
    <p>
        The first step in the project is to collect data using web scraping techniques. The data is gathered from the website 
        <a href="https://www.carsguide.com.au/buy-a-car" target="_blank">CarsGuide</a> using Selenium and web drivers. Selenium is employed 
        to automate the browsing process and extract the necessary information about cars, such as their features, specifications, 
        and prices.
    </p>

    <h2>2. Data Preprocessing:</h2>
    <p>
        Once the data is collected, it undergoes preprocessing to prepare it for modeling. This involves several key steps:
    </p>
    <ul>
        <li>
            <strong>Handling Missing Values:</strong> Identify and address any missing or null values in the dataset. This may involve 
            techniques such as imputation (replacing missing values with mean or median values) or removal of rows/columns with excessive missing data.
        </li>
        <li>
            <strong>Data Transformation:</strong> Convert categorical data into numerical format where necessary. This could involve encoding 
            categorical variables, such as car make, model, and color, into numerical values that can be used by machine learning algorithms.
        </li>
        <li>
            <strong>Normalization/Standardization:</strong> Scale numerical features to ensure that they are on a comparable scale, which helps 
            improve the performance of some machine learning algorithms.
        </li>
    </ul>

    <h2>3. Modeling:</h2>
    <p>
        After preprocessing, various machine learning models are employed to predict car prices. The models used in this project include:
    </p>
    <ul>
        <li>
            <strong>Linear Regression:</strong> A fundamental algorithm that attempts to model the relationship between the target variable (car price) 
            and one or more predictors by fitting a linear equation to the observed data.
        </li>
        <li>
            <strong>K-Nearest Neighbors (KNN):</strong> A non-parametric method used for classification and regression. For regression, KNN predicts 
            the value of a target variable based on the average of the values of its nearest neighbors.
        </li>
        <li>
            <strong>Support Vector Machine (SVM):</strong> A powerful classification and regression technique that works by finding the hyperplane 
            that best divides the data into different classes. For regression, SVM tries to fit the best line within a threshold margin while minimizing the prediction error.
        </li>
    </ul>

    <h2>4. Evaluation:</h2>
    <p>
        The performance of each model is evaluated using metrics such as Mean Squared Error (MSE) and R-squared (R²) to assess their accuracy and effectiveness 
        in predicting car prices. The model with the best performance metrics is selected for deployment.
    </p>
</body>
</html>
