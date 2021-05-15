# Insurance Cross-Selling Prediction
This repo contains my graduation project from Purwadhika Startup and Coding School,  entitled "Application of Data Science and Machine Learning in Insurance Cross-Selling Prediction"

## Background
In an insurance company, cross-selling is a kind of effort to ensure the sustainability of the company. Moreover, in an risk-sharing based investment, a success in the cross-selling process would deliver multiplier return that would help very much to boost company's growth. However, the worst case of cross-selling faliure will make the customer cancel all of his/her purchase, both on the initial and the offered products. That's why, the company needs a reliable and well-planned strategy to determine how likely the customer will accept the cross-selling offer.

### How Could Data Science and Machine Learning Contribute in This Kind of Situation?
1. Apply machine learning algorithm to predict the customers who are more likely to accept the offers.
2. Predict the likelihood (probability output) of an unknown customer to accept the offers.

The probability output of any classification algorithm can be used by the marketing team to determine **what kind of approach** they should choose to offer the product to the customer. For instance, if they found the likelihood is quite low, they can still gamble to offer the product to the customer by using a less-persuasive approach, without risking the initial purchase the customer agreed earlier. On the contrary, if they found the likelihood is relatively high, they can directly approach the customer through their personal contact, e.g. email, whatsapp, or phone call.

## Data
Dataset of this project can be downloaded at: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction

The dataset contains personal data of the customers of health insurance company. The marketing team would like to know if their customer also interested with their vehicle insurance product.

### Data Description
```
id :	Unique ID for the customer
Gender :	Gender of the customer
Age :	Age of the customer
Driving_License	0 : Customer does not have DL, 1 : Customer already has DL
Region_Code :	Unique code for the region of the customer
Previously_Insured : 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance
Vehicle_Age :	Age of the Vehicle
Vehicle_Damage : 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.
Annual_Premium : The amount customer needs to pay as premium in the year
PolicySalesChannel : Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
Vintage : Number of Days, Customer has been associated with the company
Response : 1 : Customer is interested, 0 : Customer is not interested
```
## Process
<p align="center"><img src="https://github.com/dioz95/final_project_purwadhika_jcdsah/blob/main/process.png" width=700/></p>

The workflow of this project can be separated into five diferent stages:
1. Exploratory Data Analysis (EDA): : Finds the hiddend pattern in the data and define the modelling strategy. See `Exploratory Data Analysis.ipynb`
2. Modelling : Applies modelling strategy to find the best combination of pre-processing techniques and ML model. See `Modelling.ipynb`
3. Evaluation : Evaluate the combination of pre-processing techniques and ML model by the most suitable metrics. See `Modelling.ipynb`
4. Interpretation : Interprets the model back into the business problem, see how feature relates to the model output. In this section I use an interesting technique to visualize the model output, called SHAP. See `Model Benchmarking and Business Interpretation.ipynb`
5. Deployment : Deploys the model into the production. See `Deployment Preparation.ipynb` and run the app to see how the model works in the real-life scenario by running,
```
python app.py
```
in your terminal, and open `localhost:5000` in your personal machine.

Example of the SHAP plot: 

<p align="center"><img src="https://github.com/dioz95/final_project_purwadhika_jcdsah/blob/main/shap.png" width=600/></p>

## Demo
To see how the model works:
1. Click the `Know Your Customer !!!` tab.
2. Input your data.
3. Click the `Predict` button.
4. You'll see the result appear in your screen.

<p align="center"><img src="https://github.com/dioz95/final_project_purwadhika_jcdsah/blob/main/result.png" width=500/></p>
