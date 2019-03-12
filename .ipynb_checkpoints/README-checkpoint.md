# Competition 1 ReadMe File

In this file we outline our group's Pipeline and Results for Competition One. More detailed explanations for what we did and why we did it can be found in our [Final Notebook File](FinalNoteBook.ipynb). 

## 1. Overview of Our Pipeline
The steps we took for our Pipeline are as follows:

1. Input the Data and run EDA on our Data
    - basic EDA on our data to understand the data we will be working with. We looked at numerical and visual representations of our data
2. Clean and Impute the Data
    - Dropped rows that had missing values for our Predictor Variable P(IPO)
    - Created our Needed Variables/Target Variables
    - Binned our Industry Variables according to [the SEC Website](https://www.sec.gov/info/edgar/siccodes.htm)
    - Created Ratio Columns for us to use
    - Imputed the missing values in our data. The approaches for the columns are specified in the Final Notebook.
3. Normalize and Standardize our Data
    - Use Scikit-Learn's `preprocessing.normalize` function to Normalize our Data
    - Do additional Normalizing using other approaches (log, sqrt, 1/log, etc..)
    - Standardize our data using Scikit-Learn's `MinMaxScaler` function. Explanation for this approach is explained in our notebook. 
    - We then handle outliers in our dataset, shifting things if they are outisde of 3 Standard Deviations of the Mean
4. Feature Selection (RFE and PCA)
    - Use RFE for feature selection, picking 8 variables for us to use
    - PCA was attempted however it was not beneficial to our model at the end of the day so we decided not to use it. 
5. Results 
These are the results of the model we ran. We ran our test code 1000 times

|     RESULTS    | Y1           | Y2  |
| ------------- |:-------------:| -----:|
| F1      | .6093 | .7179 |
| AUC      | .6068     |  .6759 |




6. COntributions

We all worked on the project together to come up with pipelines and other processes. Once we each had pipelines to work on, we split up and came back together to compare restults. Once we decided on a pipeline, we came together to try and optimize it. 

The group leader set up a lot of the notebooks, but we worked togther a lot of the time in person. Overall, we each applied our skills to the project and believe that everyone contributed to thier best ability. 

|     Person    |    Contribution  |
| ------------- |:-------------:|
| Brian            | 40% |
| Kevin          | 30% |
| Ryan          | 30% |
