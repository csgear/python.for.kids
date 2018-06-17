nyimport pandas as pd 

pd.set_option('max_rows', 5)

reviews = pd.read_csv('./wine_reviews/winemag-data-130k-v2.csv', index_col=0)

reviews = reviews.rename(columns={'region_1':'region', 'region_2': 'locale'})





