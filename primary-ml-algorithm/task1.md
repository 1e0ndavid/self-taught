### 1. 机器学习的一些概念：
- 有监督：从标记的训练数据来推断一个功能的机器学习任务。
- 无监督：根据类别未知(没有被标记)的训练样本解决模式识别中的各种问题。
- 泛化能力：是指机器学习算法对新鲜样本的适应能力。
- 过拟合：为了得到一致假设而使假设变得过度严格。

解决方法：（1）在神经网络模型中，可使用权值衰减的方法，即每次迭代过程中以某个小因子降低每个权值。
（2）选取合适的停止训练标准，使对机器的训练在合适的程度；
（3）保留验证数据集，对训练成果进行验证；
（4）获取额外数据进行交叉验证；
（5）正则化，即在进行目标函数或代价函数优化时，在目标函数或代价函数后面加上一个正则项，一般有L1正则与L2正则等。

- 欠拟合：指模型拟合程度不高，数据距离拟合曲线较远，或指模型没有很好地捕捉到数据特征，不能够很好地拟合数据。

解决方法：（1）增加新特征，可以考虑加入进特征组合、高次特征，来增大假设空间；
（2）添加多项式特征，这个在机器学习算法里面用的很普遍，例如将线性模型通过添加二次项或者三次项使模型泛化能力更强；
（3）减少正则化参数，正则化的目的是用来防止过拟合的，但是模型出现了欠拟合，则需要减少正则化参数；
（4）使用非线性模型，比如核SVM 、决策树、深度学习等模型；
（5）调整模型的容量(capacity)，通俗地，模型的容量是指其拟合各种函数的能力。

- 交叉验证：在给定的建模样本中，拿出大部分样本进行建模型，留小部分样本用刚建立的模型进行预报，并求这小部分样本的预报误差，记录它们的平方加和。

### 2. 线性回归的原理：
线性回归是利用称为线性回归方程的最小平方函数对一个或多个自变量和因变量之间关系进行建模的一种回归分析。这种函数是一个或多个称为回归系数的模型参数的线性组合。只有一个自变量的情况称为简单回归,大于一个自变量情况的叫做多元回归。

### 3. 线性回归损失函数、代价函数、目标函数：
- 线性回归损失函数：计算的是一个样本的误差。它是用来估量你模型的预测值 f(x)与真实值 Y的不一致程度，通常用 L(Y,f(x))来表示。
- 代价函数：是整个训练集上所有样本误差的平均。本质上看，和损失函数是同一个东西。
- 目标函数：代价函数+正则化项

### 4. 优化方法(梯度下降法、牛顿法、拟牛顿法等)：
- 梯度下降法：梯度下降的整体思路是通过的迭代来逐渐调整参数使得损失函数达到最小值。

梯度下降方法的问题： 每一步走的距离在极值点附近非常重要，如果走的步子过大，容易在极值点附近震荡而无法收敛。

解决办法：将alpha设定为随着迭代次数而不断减小的变量，但是也不能完全减为零。

- 牛顿法：牛顿法是为了求解函数值为零的时候变量的取值问题的。

优点： 牛顿法收敛速度相比梯度下降法很快，而且由于海森矩阵的的逆在迭代中不断减小，起到逐渐缩小步长的效果。

缺点： 牛顿法的缺点就是计算海森矩阵的逆比较困难，消耗时间和计算资源。因此有了拟牛顿法。

- 拟牛顿法：牛顿法需要求海森矩阵，这个矩阵需要计算二阶偏导数，比较复杂。为了改良这个问题，提出了拟牛顿法。

基本idea是：不求二阶偏导数，构造出一个近似的海森矩阵。

### 5. 线性回归的评估指标：
均方误差 MSE（Mean Squared Error），均方根误差 RMSE（Root Mean Squared Error），平均绝对误差 MAE（Mean Absolute Error），R方值（R2_score）

### 6. sklearn参数详解：
from sklearn.linear_model import LinearRegression
LinearRegression(fit_intercept=True,normalize=False,copy_X=True,n_jobs=1)

参数含义：
1. fit_intercept:布尔值，指定是否需要计算线性回归中的截距，即b值。如果为False,
那么不计算b值。
2. normalize:布尔值。如果为False，那么训练样本会进行归一化处理。
3. copy_X：布尔值。如果为True，会复制一份训练数据。
4. n_jobs:一个整数。任务并行时指定的CPU数量。如果取值为-1则使用所有可用的CPU。
返回值：
5. coef_:权重向量
6. intercept_:截距b值
 
方法：
1. fit(X,y)：训练模型。
2. predict(X)：用训练好的模型进行预测，并返回预测值。
3. score(X,y)：返回预测性能的得分。计算公式为：score=(1 - u/v)
其中u=((y_true - y_pred) ** 2).sum()，v=((y_true - y_true.mean()) ** 2).sum()
score最大值是1，但有可能是负值(预测效果太差)。score越大，预测性能越好。
