import math
import random
import sys
import numpy as np

from joblib import load

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

## TODO:validate input strings is a valid SMILES or no
def check_smiles(smile_string):
    """
    check if the input is a valid SMILES 
    :smile_string - string
    """
    if isinstance(smile_string,str):
        m=Chem.MolFromSmiles(smile_string,sanitize=False)
        if m is None:
            print('invalid SMILES')
    else:
        print('This is not a string!')


def smiles_to_solubility(smile_strings):

    sol= load ('/home/user1/team1-predicting_molecular_properties/backend/models_plots/gradientboosting/gradientboosting.joblib')
    predictions=[]
    for smile in smile_strings: 
        x_test=mol_to_vector(smile)
        predict_sol=sol.predict([x_test])
        predictions.append(predict_sol[0])
    return predictions




def mol_to_vector(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    
    properties = rdMolDescriptors.Properties()
    # To consider: which properties are the most helpful in predicting your
    # desired properties?
    return list(properties.ComputeProperties(mol))