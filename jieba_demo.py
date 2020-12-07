# encoding=utf-8
import jieba
# 基于jieba的分词 参考: https://github.com/fxsjy/jieba
seg_list = jieba.cut("贪心学院是国内最专业的人工智能在线教育品牌", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))
# 在jieba中加入"贪心学院"关键词
jieba.add_word("贪心学院")
seg_list = jieba.lcut("贪心学院是国内最专业的人工智能在线教育品牌", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))
print(seg_list)
print(type(seg_list))

# encoding=utf-8
# import jieba
#
# # jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))