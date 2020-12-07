import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from lxml import etree
import jieba

length_of_comments = []

with open('data/train_positive.txt', 'r') as fp:
    text = fp.read()

comment_text = etree.HTML(text)
comments = comment_text.xpath('//review/text()')
for comment in comments:
    comment = comment.strip()
    seg_list = jieba.lcut(comment, cut_all=False) #使用lcut返回一个list
    length_of_comment = len(seg_list)
    length_of_comments.append(length_of_comment)

plt.hist(length_of_comments, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("number of character")
# 显示纵轴标签
plt.ylabel("number of positive comments")
# 显示图标题
plt.title("Histogram of character number and positive comment")
plt.show()

length_of_neg_comments = []

with open('data/train_negative.txt', 'r') as fp:
    text = fp.read()

neg_comment_text = etree.HTML(text)
neg_comments = neg_comment_text.xpath('//review/text()')
for neg_comment in neg_comments:
    neg_comment = neg_comment.strip()
    neg_seg_list = jieba.lcut(neg_comment, cut_all=False) #使用lcut返回一个list
    length_of_neg_comment = len(neg_seg_list)
    length_of_neg_comments.append(length_of_neg_comment)

plt.hist(length_of_neg_comments, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("number of character")
# 显示纵轴标签
plt.ylabel("number of negative comments")
# 显示图标题
plt.title("Histogram of character number and negative comment")
plt.show()
