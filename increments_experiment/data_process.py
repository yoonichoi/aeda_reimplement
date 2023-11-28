from methods import *
from config import *

if __name__ == "__main__":

	#generate the augmented data sets
	for dataset_folder in dataset_folders:

		#pre-existing file locations
		train_orig = dataset_folder + '/train_orig.txt'

		# EDA augmentation
		train_eda = dataset_folder + '/train_eda.txt'
		gen_eda_aug(train_orig, train_eda)	# creates train+eda

		# AEDA augmentation
		train_aeda = dataset_folder + '/train_aeda.txt'
		gen_punc_aug(train_orig, train_aeda)	# creates train+aeda

		# NUM augmentation (A4)
		train_num = dataset_folder + '/train_num.txt'
		gen_num_aug(train_orig, train_num)	# creates train+num

		# APLHA augmentation (A4)
		train_alpha = dataset_folder + '/train_alpha.txt'
		gen_alpha_aug(train_orig, train_alpha)	# creates train+alpha

		# HYBRID augmentation (A4)
		train_hybrid = dataset_folder + '/train_hybrid.txt'
		gen_hybrid_noise_aug(train_orig, train_hybrid)	# creates train+hybrid



		#generate the vocab dictionary
		word2vec_pickle = dataset_folder + '/word2vec.pkl' # don't want to load the huge pickle every time, so just save the words that are actually used into a smaller dictionary
		gen_vocab_dicts(dataset_folder, word2vec_pickle, huge_word2vec)
