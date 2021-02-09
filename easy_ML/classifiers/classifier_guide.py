from sklearn import linear_model
from alive_progress import alive_bar

class FitHelper(LinearRegression):
    
    self.reg_fit = fit
        

    def __repr__(self):

        return "fit_helper"

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