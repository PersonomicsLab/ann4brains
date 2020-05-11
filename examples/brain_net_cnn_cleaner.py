#!/usr/bin/env python
# coding: utf-8

# In[27]:


# get all pkgs
import os
import sys
import numpy as np
import pickle
import caffe
from sklearn.model_selection import StratifiedKFold


# To import ann4brains if not installed.
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..')))
from ann4brains.synthetic.injury import ConnectomeInjury
from ann4brains.nets import BrainNetCNN, load_model


# In[28]:


#get FNET data
import helpers_cluster as help
import importlib


#%% updating help
help = importlib.reload(help)

#%% create training data sets
siteB_file = "FNETs_siteB.txt"
siteH_file = "FNETs_siteH.txt" 
num_regions = 10

# read data from files
site_B_data = help.read_data(siteB_file)
site_H_data = help.read_data(siteH_file)

# create training data
x,y = help.connectomes_to_data(site_B_data, site_H_data, num_regions)

#%% set up for splitting into k train and val
seed = 7
# np.random.seed(seed)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
x_hold = np.zeros(x.shape[0])
y_hold = np.zeros(y.shape[0])
all_training_indices = np.array(range(x.shape[0]))

n_injuries = 2
h = x.shape[2]
w = x.shape[3]
os.environ["HDF5_USE_FILE_LOCKING"] = 'FALSE'


for train, val in kfold.split(x_hold, y_hold):
    

