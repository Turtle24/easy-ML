from sklearn import datasets as df
from pick import pick

class DataSelection:
    
    def __init__(self):
        self.data_options = list()
        self.choice = None
        self.classification = ['load_iris', 'load_breast_cancer']
        self.classification_datasets = {'load_iris': df.load_iris(return_X_y=True), 'load_breast_cancer': df.load_breast_cancer(return_X_y=True)}
        self.regression = ['load_boston', 'load_diabetes', 'load_california_housing']
        self.regression_datasets = {'load_boston': df.load_boston(return_X_y=True), 'load_diabetes': df.load_diabetes(return_X_y=True),
                                    'load_california_housing': df.fetch_california_housing(return_X_y=True)}

    def __repr__(self):
        return f"{self.classification_datasets} \n {self.regression_datasets}"

    def data_loader(self):
        title = 'Please choose the type of data you want: '
        options = ['classification', 'regression']

        # Regression Data or Classification Data

        selected = pick(options, title, min_selection_count=1)
        if selected[0] == 'classification':
            chosen = self.classification
        if selected[0] == 'regression':
            chosen = self.regression

        # Choosing dataset
        follow_up = 'Now you can choose your dataset: '
        selected_data = pick(chosen, follow_up, min_selection_count=1)
        if chosen == self.regression:
            X, y = self.regression_datasets[selected_data[0]]
        if chosen == self.classification:
            X, y = self.classification_datasets[selected_data[0]]

        return X, y

