from sklearn import datasets as df
from pick import pick

class DataSelection:
    
    def __init__(self):
        self.data_options = list()
        self.choice = None
        self.classification = ['load_iris()']
        self.regression = ['load_boston()']

    def __repr__(self):
        return f"{self.classification} \n {self.regression}"

    def data_loader(self):
        title = 'Please choose the type of data you want: '
        options = ['classification', 'regression']
        # option, index = pick(options, title)
        selected = pick(options, title, multiselect=True, min_selection_count=1)
        # follow_up = 'Now choose your dataset: '
        # next_options = option
        # selection = 
        # load data
        # print('loading')
        # choice = df.selection

        return selected

