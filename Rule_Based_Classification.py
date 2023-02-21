import pandas as pd

import warnings

warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv('persona.csv')


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df.columns

agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': 'mean'}).sort_values('PRICE', ascending=False)

agg_df = agg_df.reset_index()
agg_df

agg_df['AGE'] = agg_df['AGE'].astype('category')
# agg_df.info()

agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=[0, 18, 23, 30, 40, 70],
                           labels=['0_18', '19_23', '24_30', '31_40', '41_70'])

agg_df['customer_level_based'] = [row[0].upper() + '_' +
                                  row[1].upper() + '_' +
                                  row[2].upper() + '_' +
                                  row[5].upper()
                                  for row in agg_df.values]

agg_df.head(100)

agg_df = agg_df.groupby('customer_level_based')['PRICE'].mean().reset_index()

agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=["D", "B", "C", "A"])

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df['customer_level_based'] == new_user]

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df['customer_level_based'] == new_user]
