#%% importing things
import numpy as np
import os
working_dir = '/home/oadenekan/src/cgan_norm/oyin'
os.chdir(working_dir)

#%%
# i do not have the commands
# go through hisotry for this
# get private IP and enter into putty
# sudo yum install openssh-server
# curl ifconfig.me
# sudo apt-get
# sudo systemctl enable ssh
# sudo systemctl start sshd
# sudo systemctl status sshd
# sudo systemctl enable sshd
# curl ifconfig.me
# ifconfig
# 

#%% reading in text files
siteB = "FNETs_siteB.txt"
siteH = "FNETs_siteH.txt"

with open(siteB, 'r') as f:
    siteB = [line.split('\n') for line in f]

siteB = [list_[0] for list_ in siteB]
# print(siteB)
# siteB = [list_.split('\t') for list_ in siteB]
siteB = [patient.split('\t') for patient in siteB]

# type(siteB[0].split('\t'))

#%% creating matrix
siteB_pt1 = siteB[0]
num_regions = 10
matrix = np.ones((num_regions, num_regions))

counter = 0
while 
for num in range(matrix.shape[0]):
    for num in range(matrix.shape[1]):

    

print(sum)
