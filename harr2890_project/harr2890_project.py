##################################################
#
# Final Project: CP640 Machine Learning (S22)
#
# Donna J. Harris (994042890)
# - harr2890@mylaurier.ca
#
##
# 
# Also see: 
#
##################################################

import pandas as pd

# Load local file as data source
data_source = "./data/mlbbatting1901-2021.csv"
df = pd.read_csv(data_source)


df.head()