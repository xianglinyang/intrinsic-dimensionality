# arguments for ID
import os

n_neighbors = 15
# dist_type = 'Arclength'
dist_type = 'Euclidean'
# dist_type = 'Cosine'
if_norm = False

resfolder = '/home/xianglin/projects/git_space/intrinsic-dimensionality/results'

data_filename = '/home/xianglin/projects/DVI_data/resnet18_cifar10/Model/Epoch_200/train_data.npy'
dist_table_filename = os.path.join(resfolder, 'dist_table.npy')

if_dist_table = True
if_knn_matrix = True
if_shortest_path = True
if_histogram = True

n_bins = 100
radius = -1
r_max = 0.0
r_min = -10

hist_filename = os.path.join(resfolder, 'histogram.txt')
param_filename = os.path.join(resfolder, 'params.txt')
radius_filename = os.path.join(resfolder, 'max_distance.txt')