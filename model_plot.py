
from joblib import load
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from tdc.single_pred import ADME

def mol_to_vector(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    properties = rdMolDescriptors.Properties()
    return list(properties.ComputeProperties(mol))

def make_prediction(model_path,data):
    trained_model=load(model_path)
    x_testing=[]
    true_y=[]
    split = data.get_split()
    for idx in split['test'].index:
        mol_vec = mol_to_vector(split['test']['Drug'][idx])
        if mol_vec is None:
            continue
    x_testing.append(mol_vec)
    true_y.append(split['test']['Y'][idx])
    predict_y=trained_model.predict(x_testing)
    return predict_y, true_y

def make_error_plot(predict_y, true_y):
    fig, ax = plt.subplots(1, 1)
    ax.scatter(true_y, predict_y)
    ax.set_title("Correlation")
    ax.set_xlabel("Predicted Values", fontsize=15)
    ax.set_ylabel("Ground True Values", fontsize=15)
    rsquare=r2_score(predict_y, true_y)
    ax.annotate(r"$R^2$"+ '{:.2f}'.format(rsquare), (-12,0.001))
    return fig


def main():
    data = ADME(name = 'Solubility_AqSolDB')

    trained_model_path='/home/user1/team1-predicting_molecular_properties/backend/models_plots/bayesian/solubility_model_0.joblib'

    predict_y, true_y= make_prediction(trained_model_path,data)

    make_error_plot(predict_y, true_y)
#split = data.get_split()
#trained_model=load(trained_model_path)
#x_testing=[]
#true_y=[]
#for idx in split['test'].index:
#    mol_vec = mol_to_vector(split['test']['Drug'][idx])
#    if mol_vec is None:
#        continue
#    x_testing.append(mol_vec)
#    true_y.append(split['test']['Y'][idx])
#predict_y=trained_model.predict(x_testing)
#plt.violinplot(predict_y,label='Prediction')
#plt.violinplot(true_y, label='Experiment')
#plt.savefig('model_violin.jpg')









