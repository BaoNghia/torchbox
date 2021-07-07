import os
import torch
import random
import numpy as np
import pandas as pd
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

		
# define a data class
class ClassificationDataset(torch.utils.data.Dataset):
	def __init__(self, data, transform, training = True):
		"""Define the dataset for classification problems
		Args:
			data ([dataframe]): [a dataframe that contain 2 columns: image name and label]
			data_path ([str]): [path/to/folder that contains image file]
			transform : [augmentation methods and transformation of images]
			training (bool, optional): []. Defaults to True.
		"""
		self.data = data
		self.imgs = data["file_name"].unique().tolist()
		self.training = training
		self.transform = transform

	def __getitem__(self, idx):
		image = Image.open(self.data.iloc[idx, 0]).convert('RGB')
		label = self.data.iloc[idx, 1]
		label = torch.tensor(label, dtype=torch.long)

		if self.transform is not None:
			image = self.transform(image)
		
		return image, label

	def __len__(self):
		return len(self.imgs)
