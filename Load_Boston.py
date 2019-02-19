"""
分类：离散型
回归：连续型

线性回归：
线性回归通过一个或者多个自变量与因变量之间之间进行建模的回归分析。
其中特点为一个或多个称为回归系数的模型参数的线性组合。
一元线性回归：涉及到的变量只有一个
多元线性回归：涉及到的变量两个或两个以上

f(x) = ∑(wi * xi) + b
w权重
b偏置项，可以理解为w0*1

通用公式：ℎ(𝑤)= w0 + w1*x1 + … = w^T(转置)*x
列矩阵w = [[w0],[w1],[w2]],
x = [[1], [x1], [x2]]

矩阵乘法numpy.muitiply(a, b)

损失函数(误差大小)：
yi为第i个训练样本的真是只
hw(xi)为第i个训练样本特征值组合预测函数
总损失定义：
𝐽(𝜃)= 〖〖(ℎ〗_𝑤 (𝑥〗_1) −𝑦_1 )^2+〖〖(ℎ〗_𝑤 (𝑥〗_2) −𝑦_2 )^2+…+〖〖(ℎ〗_𝑤 (𝑥〗_𝑚) −𝑦_𝑚 )^2

             = ∑_(𝑖=1)^𝑚▒〖(ℎ_𝑤 (𝑥_𝑖 )−𝑦_𝑖 〗 )^2
类似于标准差不开根号
误差平方和又称最小二乘法

如何使损失函数最小，求最优化的w：
1、正规方程(特征数量多时求解速度慢，所以不通用)
w = (X^T*X)^(-1)*(X^T)*Y
X特征值矩阵
Y目标值矩阵
有几个特征就有几个w
2、梯度下降(面对训练数据规模十分庞大的任务)
沿着这个损失函数下降的方向找，最后就能找到山谷的最低点，然后更新W值
学习率a越大，下降得越快。

sklearn.linear_model.LinearRegression
正规方程
sklearn.linear_model.SGDRegressor
梯度下降

回归性能评估sklearn.metrics.mean_squared_error
均方误差(Mean Squared Error)MSE) 评价机制：
MSE = (1/m)*∑i=1~m (y^i-y^—)^2
y^i预测值
y^—真实值
mean_squared_error(y_true, y_pred)
均方误差回归损失
y_true:真实值
y_pred:预测值
return:浮点数结果

线性回归器是最为简单、易用的回归模型。
从某种程度上限制了使用，尽管如此，在不知道特征之间关系的前提下，我们仍然使用线性回归器作为大多数系统的首要选择。
小规模数据：LinearRegression(不能解决拟合问题)
大规模数据：SGDRegressor


实例：波士顿房价预测
数据来源：from sklearn.datasets import load_boston

1、波士顿地区房价数据获取
2、波士顿地区房价数据分割
3、训练与测试数据标准化处理
4、使用最简单的线性回归模型LinearRegression和梯度下降估计SGDRegressor对房价进行预测
5、使用均值误差进行性能评估

"""
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def mylinear():
    """
    线性回归直接预测房价
    :return: None
    """
    # 获取数据
    lb = load_boston()

    # 分割训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    # 进行标准化处理
    # 特征值和目标值都需要进行标准化处理，因为特征值和目标值特证数不同，所以需要实例化两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 0.19版本以后要求是二维，不知道样本数，所以-1，一个特征所以1
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # estimstor预测
    # 正规方程求解方式预测结果
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    print("正规方程回归系数：", lr.coef_)

    # 预测的房价
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    print("正规方程测试集里每个房子的预测价格：", y_predict)
    print("正规方程的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_predict))

    # 梯度下降求解方式预测结果
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print("梯度下降回归系数：", sgd.coef_)

    # 预测的房价
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print("梯度下降测试集里每个房子的预测价格：", y_sgd_predict)
    print("梯度下降的均值误差：", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict))

    return None


if __name__ == '__main__':
    mylinear()
