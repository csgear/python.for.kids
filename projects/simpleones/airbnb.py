
import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf


tf.logging.set_verbosity(tf.logging.FATAL)

used_features = ['property_type','room_type','bathrooms','bedrooms','beds','bed_type','accommodates','host_total_listings_count'
                ,'number_of_reviews','review_scores_value','neighbourhood_cleansed','cleaning_fee','minimum_nights','security_deposit',
                'host_is_superhost', 'instant_bookable', 'price']

boston = pd.read_csv('boston_listings.csv', usecols = used_features)

print(boston.shape)

print(boston.head(2))



