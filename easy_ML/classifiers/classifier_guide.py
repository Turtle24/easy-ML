from sklearn import linear_model
from alive_progress import alive_bar

class Guide:
    self.model = None
    self.next = None
    self.more_info = ""
    self.steps = {'step 1': 'Select data', 'step 2': 'Choose Model', 'step 3': 'Train test split', 'step 4': 'Fit data to model', 'step 5': 'Predict'}    

    def __repr__(self):

        return 'guides you through the ML process'

    # Brief Explaination of model 
    def explain_fit(self):
        return "fits to model >_>"

    def explain_fit(self):
            return "fits to model >_>"

    # Show Progress of fit        
    def progress(self):

        # Progress Bar
        with alive_bar(self.fit) as bar:
            bar()