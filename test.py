#Imports
import pandas as pd
from chembl_webresource_client.new_client import new_client

#Search for target protein
target = new_client.target
target_query = target.search('Human immunodeficiency virus type 1 protease')
targets = pd.DataFrame.from_dict(target_query)
print(targets)