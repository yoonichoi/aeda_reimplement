#user inputs

#dataset folder
datasets = ['cr', 'sst2', 'subj', 'trec', 'pc']
dataset_folders = ['experiments/addratio_experiment/data/' + dataset for dataset in datasets] # (A4)

#number of output classes
num_classes_list = [2, 2, 2, 6, 2]

#num_aug increments
# 1 to 50 in 5 increments
num_augs = [1,3,6,9,12] + [i for i in range(15, 51, 5)]

#number of words for input
input_size_list = [50, 50, 40, 25, 25]

#word2vec dictionary
huge_word2vec = 'word2vec/glove.840B.300d.txt'
word2vec_len = 300