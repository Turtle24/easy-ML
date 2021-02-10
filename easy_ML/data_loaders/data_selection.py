from sklearn import datasets as df
from pick import pick

class DataSelection:
    
    def __init__(self):
        self.data_options = list()
        self.choice = None
        self.classification = [df.load_iris()]
        self.regression = [df.load_boston(return_X_y=True), df.load_diabetes(return_X_y=True)]

    def __repr__(self):
        return f"{self.classification} \n {self.regression}"

    def data_loader(self):
        title = 'Please choose the type of data you want: '
        options = ['classification', 'regression']

        # Regression Data or Classification Data

        selected = pick(options, title, min_selection_count=1)
        if selected is 'classification':
            chosen = self.classification
        else:
            chosen = self.regression

        # Choosing dataset
        follow_up = 'Now you can choose your dataset: '
        next_options = chosen
        selected_data = pick(next_options, follow_up, min_selection_count=1)
        X, y = selected_data
        # load_data = df.selected_data[0]

        return X, y

