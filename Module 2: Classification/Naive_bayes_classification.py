"""
先验概率：

事件发生前的预判概率。可以是基于历史数据的统计，可以由背景常识得出，也可以是人的主观观点给出。一般都是单独事件概率，如P(x),P(y)。Eg: 明天堵车的概率为二分之一，是根据生活经验得出的。

后验概率：

事件发生后求的反向条件概率；或者说，基于先验概率求得的反向条件概率。概率形式与条件概率相同。Eg: 已知堵车，求车祸导致的堵车的概率。

条件概率：

一个事件发生后另一个事件发生的概率。一般的形式为P(x|y)表示y发生的条件下x发生的概率。

朴素贝叶斯公式为：

P(Y|X) = P(X)P(Y)/P(X) = P(X|Y)P(Y)/P(X)

我们可以计算出不同条件下的后验概率，再从中挑选出最大的概率，从而进行分类。

即：

max(P(Y|X)) = max(P(X|Y)P(Y)/P(X)) = max(P(X|Y)P(Y))/P(X)

不同条件下的P(Y)非常容易获得，
而：贝叶斯假设X是条件独立的

所以：

P(X|Y) = P(X1|Y)*P(X2|Y)*P(X3|Y)...P(Xn|Y)

所以可以知道“后验概率P(Y|X)” 可以通过 P(X|Y)、P(Y)、P(X)计算得出。而P(X|Y)、P(Y)和P(X)又可以通过大量的数据计算得到（P(Y)和P(X)也可以是先验概率）。

即：后验概率 = 先验概率 + 数据

"""