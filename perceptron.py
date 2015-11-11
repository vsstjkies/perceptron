# -*- coding: utf-8 -*-

d = 1 # 教師信号
theta = 0.5
# k = 0.9
k = 0.8
alpha = 0.2

x_lenght = 2
x = [0, 1] # 入力
w_1 = [0, 0.2] # 重みの初期値
w = [w_1] # 重みの配列
t = 0

# ステップ関数やシグモイド関数に渡す前の値を計算
def calc_output_before():
    output = -1 * theta
    for i in range(x_lenght):
        output = output + x[i] * w[t][i]
    return output

def step_func(val):
    if val < 0:
        return 0
    return 1

def calc_output():
    return step_func( calc_output_before() )

def update_weight():
    new_w_list = []
    for i in range(x_lenght):
        delta = d - calc_output() # 学習信号
        delta_w = alpha * delta * x[i]
        new_w = k * w[t][i] + delta_w
        new_w_list.append( new_w )
    w.append( new_w_list )



for time in range(4):
    t = time
    print 't = ' + str( t )
    print '出力値(ステップ関数前) : ' + str( calc_output_before() )
    print '出力値(ステップ関数後) : ' + str( calc_output() )
    update_weight()
    print '重み(w1) : ' + str( w[t + 1][0] )
    print '重み(w2) : ' + str( w[t + 1][1] )
    print '------------------------------'

