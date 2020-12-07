from lxml import etree
import re
import jieba
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression


train_comments = []
train_labels = []
test_comments = []
test_labels = []
train_comments_cleaned = []
test_comments_cleaned = []

def process_data(file, str):
    with open(file, 'r') as fp:
        text = fp.read()

    comment_text = etree.HTML(text)
    comments = comment_text.xpath('//review/text()')
    for comment in comments:
        comment = comment.strip()
        # 存入测试集
        train_comments.append(comment)
        # 清理特殊字符
        comment = clean_symbols(comment)
        #分词并做停用词过滤
        comment = clean_stopword(comment, 'data/stopwords.txt')
        # 存入过滤测试集
        train_comments_cleaned.append(comment)
        train_labels.append(str)

    fp.close()

def process_test_data(file):
    with open(file, 'r') as fp:
        text = fp.read()

    comment_text = etree.HTML(text)
    comments = comment_text.xpath('//review/text()')
    labels = comment_text.xpath('//review/@label')
    for comment in comments:
        comment = comment.strip()
        # 存入测试集
        test_comments.append(comment)
        # 清理特殊字符
        comment = clean_symbols(comment)
        # 分词并做停用词过滤
        comment = clean_stopword(comment, 'data/stopwords.txt')
        test_comments_cleaned.append(comment)

    for label in labels:
        test_labels.append(label)

    fp.close()

def clean_symbols(text):
    """
        对特殊符号做一些处理，此部分已写好。如果不满意也可以自行改写，不记录分数。
        """
    text = re.sub('[!！]+', "!", text)
    text = re.sub('[?？]+', "?", text)
    text = re.sub("[a-zA-Z#$%&\'()*+,-./:;：<=>@，。★、…【】《》“”‘’[\\]^_`{|}~]+", " OOV ", text)
    text = re.sub("[0-9]+","NUM", text)
    return re.sub("\s+", " ", text)

def clean_stopword(comment,filename):
    # 分词
    comment = jieba.cut(comment)
    # 加载停用词
    stopwords = stopwordslist(filename)
    outer_comment = ''
    for word in comment:
        if word not in stopwords:
            if word != '\t':
                outer_comment += word
                outer_comment += ' '

    return outer_comment


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords

def main():
    train_pos_file = "data/train_positive.txt"
    train_neg_file = "data/train_negative.txt"
    test_comb_file = "data/test_combined.txt"
    stopwords_file = 'data/stopwords.txt'
    process_data(train_pos_file,'0')
    process_data(train_neg_file, '1')
    process_test_data(test_comb_file)
    vector = TfidfVectorizer()
    X_train = vector.fit_transform(train_comments_cleaned)
    y_train = train_labels


    clf = MultinomialNB(alpha=0.2)









if __name__ == '__main__':
    main()