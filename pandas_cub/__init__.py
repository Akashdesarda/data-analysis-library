import numpy as np

__version__ = "0.1.0"

class DataFrame:
    
    def __init__(self, data):
        """
        A Dataframe holds 2-D heterogenous data. Create it by passing dict.
        
        Parameters
        ----------
        data: dict
            A dict of string mapped to numpy array. The key will become column
            name and their values will become rows.
        """
        
        # Check for correct path
        self._check_correct_path(data) 