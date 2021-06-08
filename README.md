Red Wine Quality Predictor

This wine predictor website, deployed to the web via Heroku (https://ai-sommelier.herokuapp.com/), allows a user to input variables that may determine wine quality. The output is a quality rating on a scale of 0-10. Our website should prove useful to a wine maker or sommelier, for example. 

Dataset Detail and data exploration
Our winequality-red.csv dataset includes 1599 records  and their accompanying attributes and quality rating for the Portuguese "Vinho Verde" type of red wine:Input variables (based on physiochemical tests):
    - Fixed acidity
    - Volatile acidityCitric acid
    - Residual sugarChlorides
    - Free sulfur dioxide
    - Total sulfur dioxide
    - Density
    - pH
    - sulphates
    - alcohol
    output variable (based on sensory data):
    - quality (score between 0 and 10)
    
Data source:
P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.
    
Machine Learning – Statistics and Correlation
Using JupyterNotebook, different statistical algorithms were used to come up with a higher ranking, accurate model. Random Forest, a supervised learning algorithm, is the model which yielded 72% accuracy. We then trained this model using model.predict. 

Deploy Machine Learning Model using Flask to Heroku
Please install the following packages to successfully launch our Wine Quality Predictor:  Flask, Pandas, Numpy, SKlearn, Gunicorn, Pickle.

Our files and their purpose is outlined below:
    - model.pycontains our machine learning model
    - app.pycontains our logic and it’s where we import our pickle model and flask module in our machine learning model
    - model.pklfile packages our machine learning model
    - index.html outputs our web page
    - Procfile allows us to deploy our app to Heroku
    - requirements.txt contains all our imported libraries (note: in lieu of using a requirements.txt, you can use pipfile and pipfile.lock)

Visualizations
Using Tableau, we created an interactive dashboard. The dashboard will display modelswhich indicate how the taster may rate the quality of the wine. The bar graph displays the most influential variables and their distribution with each quality score. The box and whisker plots display the most common variables and their distribution with each quality class. The bell curve represents the overall frequency of quality. Lastly, the correlation matrix describes the relationship between each variable and quality. 

![Untitled](https://user-images.githubusercontent.com/72583942/121259522-3d036800-c87e-11eb-8318-a4395da1b50c.jpg)
