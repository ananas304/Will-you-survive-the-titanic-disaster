# Will you survive the Titanic Disaster 
This project is based on the famous Titanic disaster dataset from [Kaggle](https://www.kaggle.com/competitions/titanic). The dataset contains demographic and travel-related information about the passengers aboard the Titanic, with the goal of predicting who would survive the tragedy. This project implements a Machine Learning (ML) model to predict survival based on user inputs, such as:
1. Number of children/parents aboard
2. Number of spouses/siblings aboard
3. Fare
4. Title
5. Sex
6. port
7. Passenger class (Pclass)

### Dataset Overview
The Titanic dataset provides key features that help determine survival outcomes. These include socio-economic status (class), gender, and family presence on board. For more detailed information on the dataset, refer to the official [Kaggle Titanic page](https://www.kaggle.com/competitions/titanic).

### Machine Learning Model
A Random Forest classifier is used as the ML model to predict whether a passenger would survive based on the input features. The model was chosen due to its effectiveness in handling categorical and numerical data, making it ideal for this task.
#### Key features considered in the model:
1. Family composition (children, parents, spouses, siblings)
2. Socio-economic indicators (fare, class, embarked port)
3. Personal attributes (title, sex)
The Random Forest model leverages multiple decision trees to improve accuracy and reduce overfitting, providing a robust prediction of survival.

### Django Integration
The project uses Django to create an interactive web interface where users can input relevant details such as the number of children/parents and fare, and receive predictions on survival. The integration between Django and the ML model ensures that the backend processes the input, runs the model, and delivers the result in real-time.

### Workflow:
1. User Input: The user submits relevant data via a web form.
2. Prediction: The Django backend processes the inputs and passes them to the Random Forest model.
3. Result: The model predicts the survival outcome, and Django displays the result.

## Conclusion
This mini-project was a valuable learning experience, combining Django for user interaction and Machine Learning to generate predictions. The clean integration of these technologies allowed me to develop both web development and machine learning skills in a practical context.
