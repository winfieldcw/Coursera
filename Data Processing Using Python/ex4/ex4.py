# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:57:43 2016

@author: Winfield
"""
"""
来个小小的小实践项目吧（此处不计分，但是其实在其他地方有计分哟）。

计算MovieLens 100k数据集中男性女性用户评分的标准差并输出。

数据集下载http://files.grouplens.org/datasets/movielens/ml-100k.zip

其中u.data 表示100k条评分记录，每一列的数值含义是：

user id | item id | rating | timestamp

u.user表示用户的信息，每一列的数值含义是：

user id | age | gender | occupation | zip code

u.item文件表示电影的相关信息，每一列的数值含义是：

movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |

可能会用到的相关函数：

pandas.read_table(filepath_or_buffer, sep='\t', names=None)

pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')

pandas.merge(left, right, how='inner')

更详尽的API文档请参考http://pandas.pydata.org/pandas-docs/stable/ 。
"""
import pandas as pd
import numpy as np

#评分情况dataframe
data_fields = ['user_id','item_id ','rating','timestamp']
reatingDF = pd.read_table('ml-100k/u.data', sep='\t', names=data_fields)
print reatingDF.head(5)

#用户情况dataframe
user_fields = ['user_id','age ','gender','occupation','zip_code']
userDF = pd.read_table('ml-100k/u.user', sep='|', names=user_fields)
print userDF.head(5)

#100,000条评价的数据 只有943个用户 证明一个用户评了多次
#print len(reatingDF.user_id)
#print len(set(reatingDF.user_id))

#将两个dataframe合并   内连接 用user_id 连接
mergeDF = pd.merge(reatingDF, userDF, how='inner', on = 'user_id')
#print mergeDF.head(5)
#print len(mergeDF.user_id)
#print len(set(mergeDF.user_id))

#求标准差
print mergeDF.groupby('gender').std().rating
