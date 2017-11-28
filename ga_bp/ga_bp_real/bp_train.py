'''
Created on 2017年11月21日

@author: ljs
'''
import tensorflow as tf
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import preprocessing

# 添加层
def add_layer(inputs, Weights, biases, activation_function=None):
    # add one more layer and return the output of this layer
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def bp_train(individual):
    tf.reset_default_graph()  # 重置默认图
    graph = tf.Graph()        # 新建空白图
    with graph.as_default() as g:   # 将新建的图作为默认图
        with tf.Session(graph=g):   # Session  在新建的图中运行
            # 需要运行的代码放这里，每次运行都会使用新的图
            column1 = []
            column2 = []
            with open('10790.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                for row1 in reader:
                    row = list(map(float,row1))
                    data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                    column1.append(data)
                    column2.append([row[11]])
            x = np.mat(column1)
            y = np.mat(column2)
            #正常归一化及还原，精度0.01
            scaler_x = preprocessing.MinMaxScaler()
            x_data = scaler_x.fit_transform(x)
            scaler_y = preprocessing.MinMaxScaler()
            y_data = scaler_y.fit_transform(y)
          
            xs = tf.placeholder(tf.float32, [None, 11])
            ys = tf.placeholder(tf.float32, [None, 1])
            
            w1 = []
            for i in range(11):
                a = individual[10*i:10*i+10]
                w1.append(a)
            weight = individual[110:120]
            w2 = []
            for w in weight:
                w2.append([w])
            b1 = individual[120:130]
            b2 = individual[130]
            Weights_1 = tf.Variable(tf.cast(np.mat(w1), dtype=tf.float32),name='Weights_1')
            biases_1 = tf.Variable(tf.cast(np.mat(b1), dtype=tf.float32),name='biases_1')
            Weights_2 = tf.Variable(tf.cast(np.mat(w2), dtype=tf.float32),name='Weights_2')
            biases_2 = tf.Variable(tf.cast(np.mat(b2), dtype=tf.float32),name='biases_2')
            
            # 3.定义神经层：隐藏层和预测层
            # add hidden layer 输入值是 xs，在隐藏层有 10 个神经元   
            l1 = add_layer(xs, Weights_1, biases_1, activation_function=tf.nn.relu)
            # add output layer 输入值是隐藏层 l1，在预测层输出 1 个结果
            prediction = add_layer(l1, Weights_2, biases_2, activation_function=None)
            
            # 4.定义 loss 表达式
            # the error between prediciton and real data    
            loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                             reduction_indices=[1]))
            # 5.选择 optimizer 使 loss 达到最小                   
            # 这一行定义了用什么方式去减少 loss，学习率是 0.1       
            train_step = tf.train.AdamOptimizer(0.1).minimize(loss)
            
            init = tf.initialize_all_variables()
            sess = tf.Session()
            # 上面定义的都没有运算，直到 sess.run 才会开始运算
            sess.run(init)
            # 迭代 1000 次学习，sess.run optimizer
            #for i in range(1):
            sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
            error = sess.run(loss, feed_dict={xs: x_data, ys: y_data})
            print(1/error)
            return 1/error

if __name__ == '__main__':
    pass
            