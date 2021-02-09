from sklearn import datasets as df
from PyInquirer import inquirer

class DataSelection:
    
    def __init__(self):
        self.data_options = list()
        self.choice = None
        self.classification = ['load_iris()']
        self.regression = ['load_boston()']

    def __repr__(self):
        return f"{self.classification} \n {self.regression}"

    def data_loader(self, model):
        self.options = self.classification if model == 'clf' else self.regression

        selection_prompt = [inquirer.List('selection',
                                            message=f'Choose a {self.model} dataset',
                                            choices=options)]
        answer = inquirer.prompt(selection_prompt)
        selection = prompt(answer)
        # load data
        print('loading')
        choice = df.selection

        return choice

