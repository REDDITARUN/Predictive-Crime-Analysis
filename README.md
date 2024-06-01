# 👁️ Crimson Eye: Data-Driven Approach to Crime Analysis

## Team Members
- **Charvi Kusuma** [GitHub](https://github.com/kcharvi)
- **Tarun Reddi** [GitHub](https://github.com/REDDITARUN)

## 📋 Project Overview
This project aims to leverage data analysis and machine learning to enhance predictive policing efforts. By analyzing crime data from the City of Los Angeles, we identify patterns, predict potential crime hotspots, and optimize the allocation of law enforcement resources.

<p align="center">
  <img src="https://github.com/REDDITARUN/Predictive-Crime-Analysis/assets/53268025/4f7d1c22-abe3-4e16-abfd-ce5b986fd2bd" alt="image">
</p>


### ❓ Problem Statement
Understanding the multifaceted challenges of crime data analysis is crucial for:
1. **Prioritizing Public Safety**: Identifying areas with elevated crime rates to allocate law enforcement resources efficiently.
2. **Efficient Resource Allocation**: Guiding the allocation of limited resources to areas with the highest need, reducing response times and increasing efficiency.
3. **Rooting Out Crime Causes**: Delving into historical crime patterns to understand the origins of criminal activities and crafting effective prevention strategies.
4. **Adapting to Emerging Trends**: Understanding evolving criminal behaviors and responding adeptly.
5. **Optimizing Resource Efficiency**: Identifying and rectifying inefficiencies in resource allocation.

## 📊 Data Overview
The dataset used in this project is sourced from the City of Los Angeles Open Data portal, covering crime incidents from 2020 to the present. It includes 811,663 rows and 28 columns, providing comprehensive insights into crime trends and patterns within the city.



### 📁 Phase 1: Data Collection and Preprocessing
In this phase, we focused on understanding and preparing the crime data for further analysis. This included data collection, cleaning, processing, and initial exploratory data analysis to gain insights into the dataset's structure and characteristics.

#### Tasks Performed:
1. **Understanding the Data**: 
   - Loaded the dataset and examined its structure using methods like `info()`, `describe()`, and checking for missing values.
2. **Data Cleaning**:
   - **Dropping Unnecessary Columns**: Removed columns like 'DR_NO' and 'Mocodes' due to high uniqueness or missing values.
   - **Handling Missing Values**: Applied strategies like filling numerical columns with mean values and categorical columns with mode.
   - **Removing Duplicates**: Identified and removed duplicate rows to ensure data quality.
   - **Standardizing Column Names**: Ensured consistency in column names by converting to lowercase and replacing spaces with underscores.
3. **Data Type Conversion**: 
   - Converted 'Date_Reported' and 'Date_Occurred' columns to datetime format for proper date handling.
4. **Handling Low-Frequency Values**: 
   - Managed rare categories in columns like 'Victim_Sex' and 'Victim_Descent' by grouping them under 'Other'.
5. **Cleaning Textual Columns**: 
   - Standardized and cleaned columns such as 'Crime_Code_Description' and 'Location'.
6. **Handling Outliers**: 
   - Applied Interquartile Range (IQR) method to cap outliers in numerical columns.
7. **Encoding Categorical Columns**: 
   - Used label encoding for categorical columns to convert them into numerical format.
8. **Data Normalization**: 
   - Applied Min-Max scaling to numerical columns for normalization.
9. **Redundant Columns Removal**: 
   - Removed columns like 'Crime_Code_1' and 'Status' after encoding to avoid redundancy.

#### Exploratory Data Analysis (EDA):
- **Univariate Analysis**: Examined individual features like 'Area_Name', 'Victim Sex', and 'Victim Age'.
- **Bivariate Analysis**: Explored relationships between pairs of variables.
- **Crime Trends**: Identified trends over time and geographical distribution of crimes.
- **Visualizations**: Created bar plots, heatmaps, word clouds, scatter plots, and correlation maps to visualize data insights.

### 🧠 Phase 2: Model Development and Evaluation
In this phase, we developed and evaluated various machine learning models to predict crime-related outcomes. The goal was to leverage different algorithms to understand their predictive power and suitability for our dataset.

#### Tasks Performed:
1. **Importing Required Libraries**: 
   - Imported libraries for data manipulation, visualization, and machine learning such as Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn.
2. **Preparing the Dataset**: 
   - Loaded the cleaned dataset and selected relevant features for modeling.
3. **Model Implementation**:
   - **Linear Regression**: Predicted 'Area' based on 'Latitude' and 'Longitude'.
   - **Logistic Regression**: Classified crimes as vehicle-related or not.
   - **Naive Bayes**: Predicted crime areas based on various features.
   - **K-Nearest Neighbors (KNN)**: Predicted 'Status_Description' of reported incidents.
   - **Decision Tree**: Classified crime descriptions into the top 5 categories.
4. **Model Evaluation**: 
   - Evaluated models using metrics such as accuracy, precision, recall, F1 score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
   - Visualized model performance using confusion matrices, ROC curves, precision-recall curves, and feature importance plots.

### Algorithms and Results

| Algorithm                | Objective                                                                                      | Results                                                                                 |
|--------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Linear Regression**    | Predict 'Area' based on 'Latitude' and 'Longitude'.                                            | - Mean Absolute Error: 4.61<br>- Mean Squared Error: 27.15<br>- R-squared: 0.24         |
| **Logistic Regression**  | Classify crimes as vehicle-related or not based on selected features.                          | - Accuracy: 0.84<br>- Precision: 0.81<br>- Recall: 0.49<br>- F1 Score: 0.61             |
| **Naive Bayes**          | Perform multiclass classification to predict crime areas based on various features.             | - Accuracy: 0.90<br>- Detailed classification report provided                          |
| **K-Nearest Neighbors**  | Predict 'Status_Description' of reported incidents.                                            | - Accuracy: 0.76<br>- Precision, Recall, F1-score varied across classes                 |
| **Decision Tree**        | Classify crime descriptions into the top 5 categories based on specific features.              | - Accuracy: 0.64<br>- Detailed classification report provided                          |
| **XGBoost**              | Predict 'Location_Type' based on several features.                                             | - Accuracy: 0.70<br>- Detailed classification report provided<br>- Confusion Matrix     |

For detailed explanations on why we used these specific algorithms, please check out our comprehensive report contained in the repository.

### 🌐 Phase 3: Deployment and Visualization
In this phase, we focused on deploying the predictive models and creating visualizations to present our findings effectively. This included building a user interface for interacting with the models and summarizing the results.

#### Tasks Performed:
1. **Model Deployment**:
   - Developed scripts and frameworks for deploying the trained models, making them accessible for real-time predictions.
2. **User Interface Development**:
   - Created HTML and Python files to build a user-friendly interface for crime prediction and visualization.
   - Implemented features such as crime status prediction tools and crime forecasting.
3. **Visualization and Reporting**:
   - Developed comprehensive visualizations to present the results of our models and the insights gained from the data.
   - Created dashboards and reports to summarize the key findings and their implications for predictive policing.

| Feature | Functionality | User Learning | Police Learning |
| --- | --- | --- | --- |
| Vehicle Theft Prediction Tool | Utilizes regression models to predict likelihood of vehicle theft | Identifying high-risk areas for vehicle theft | Efficiently deploying resources for targeted patrolling |
| Crime Difficulty Estimation Tool | Uses KNN to assess complexity of crimes based on multiple parameters | Understanding complexity levels of different crime instances | Allocating resources for handling more challenging cases |
| Crime Status Prediction Tool | Predicts potential crime types based on geographical and premise data | Anticipating probable crime types in specific areas | Strategically allocating resources for proactive crime prevention |
| Additional Reporting Form | Captures details of prevented/thwarted crime incidents | Contributing to a comprehensive safety landscape understanding | Gathering data on thwarted incidents for better crime analysis |

### Glimpse of the web application
![image](https://github.com/REDDITARUN/Predictive-Crime-Analysis/assets/53268025/91ee667e-fef9-4c4e-a547-c23b17eace71)
![image](https://github.com/REDDITARUN/Predictive-Crime-Analysis/assets/53268025/33527c7a-bc4c-400f-acd7-cd76f458ecfd)
![image](https://github.com/REDDITARUN/Predictive-Crime-Analysis/assets/53268025/2f0b3acd-a13e-426f-8c02-e8d7250996b5)



## 💻 Running the Project Locally

To demonstrate the project locally, follow the steps below:

1. **Change to phase3 directory where the entry point to application is present:**
    ```bash
    cd \src\phase3
    ```

2. **Install the necessary requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application using:**
    ```bash
    python3 main.py
    ```

4. **Open any browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

   You will be on the Landing Page!

### 🚨Academic Integrity Disclaimer🚨

This project in this repository is intended solely as an inspiration for your future projects and should be referenced accordingly. It is not meant for students to fulfill their academic project requirements. If a student uses this project for such purposes, the creators are not responsible. The student will be solely accountable for violating academic integrity. We explicitly state that this repository should not be used to meet academic requirements. Therefore, any academic integrity issues should be addressed with the student, not the creators.


This README file provides an overview of the project, detailing the problem statement, data handling, exploratory analysis, and the algorithms used along with their results. It showcases the importance and potential impact of the project on predictive policing and community safety.
