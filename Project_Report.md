#### Cryptocurrency Liquidity Prediction - Project Report.

Exploratory Data Analysis (EDA)

Dataset SummaryDescription:

* The dataset used for this project contains historical cryptocurrency price and trading volume data. It includes key features such as Symbol, Price, Market Cap, 24h Volume, and various price change metrics over different time frames (1h Price Change, 24h Price Change, 7d Price Change).Date Range: The data covers a period from 2016 to 2017.Size: The dataset consists of [State the total number of rows] rows and [State the total number of columns] columns.

* Key Findings and Visualizations
Data Distribution: Most of the key variables, such as Price, Volume, and Market Cap, exhibited a highly skewed distribution to the right. This is typical for financial data, where a few assets have extremely high values while the majority have lower values.

* Correlations: The analysis revealed a strong positive correlation between 24h Volume and Market Cap, which is intuitive as cryptocurrencies with larger market capitalizations tend to have higher trading volumes. We also found a significant relationship between 24h Volume and the target variable, Liquidity Ratio, confirming the importance of trading activity for liquidity.

Trends: Time-series analysis showed a clear upward trend in prices and volumes for major cryptocurrencies like Bitcoin and Ethereum throughout 2017, a period of significant market growth.

2. Data Processing & Feature Engineering
* Missing Values: We handled missing values by imputing them using a relevant strategy (e.g., mean imputation) to ensure data consistency and prevent model errors.

* Normalization and Scaling: Numerical features were scaled using MinMaxScaler. This method was chosen because it preserves the relationships between the original values and scales the data to a fixed range (0 to 1). This is crucial for models that are sensitive to the magnitude of the input features.

* New Features: We engineered several new features to provide the model with a richer understanding of liquidity dynamics. The most significant of these was the Liquidity Ratio, calculated by dividing 24h Volume by Market Cap. This feature directly measures how easily an asset can be traded without affecting its price, serving as our primary target variable.

3. Model Selection & Evaluation
Model Choice
* Justification: The Random Forest Regressor was selected as the final model due to its robustness and effectiveness with tabular data. Its key advantages include:

* Ability to Handle Non-linear Relationships: It can capture complex, non-linear patterns between features and the target variable.

* Robustness to Outliers: As an ensemble method, it is less sensitive to outliers, which are common in financial data.

* Feature Importance: It provides valuable insights into which features were most influential in the predictions.

* Performance Metrics
RMSE (Root Mean Squared Error):

RMSE: [Your RMSE Value]

* Explanation: The RMSE indicates that, on average, our model's predictions were off by this much from the actual liquidity values.

MAE (Mean Absolute Error):

MAE: [Your MAE Value]

* Explanation: The MAE gives us the average prediction error, making it easy to understand the model's accuracy in a more direct, interpretable way.

R² (R-squared) Score:

R² Score: [Your R² Value]

* Explanation: The R² score indicates that our model explains [Your R² Value]% of the variance in the target variable, which is a strong indicator of its predictive power.

4. High-Level Design & Pipeline Architecture
* The project's pipeline follows a standard machine learning workflow.  This ensures a clear and reproducible process from data ingestion to final deployment.

* Data Loading: The process begins by loading the raw cryptocurrency data.

* Data Preprocessing: The data is cleaned, and missing values are handled.

* Feature Engineering: New features, including the Liquidity Ratio, are created to enrich the dataset.

Model Training: The preprocessed and engineered data is used to train the Random Forest Regressor model.

Model Deployment: The trained model and encoder are saved as .pkl files and deployed within a Flask API, which is then containerized using Docker.

Prediction: The Flask API receives new data points and uses the pre-trained model to return a liquidity prediction.
