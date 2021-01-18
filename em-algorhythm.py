#numpy,scipy.statsからnorm,math,matplotlib.pyplotをインポート！
import numpy as np
from scipy.stats import norm
ball_pattern_arr = [8,3,6,5,7,3,6,4]
PA = 1/2
PB = 1/2


Ma = {"m":6,"sigma":1}
Mb = {"m":4,"sigma":1}

def get_propbability(num,dist_param):
    return norm.pdf(num,dist_param["m"],dist_param["sigma"])

def P_num(num,Ma=Ma,Mb=Mb):
    return norm.pdf(num,Ma["m"],Ma["sigma"]) + norm.pdf(num,Mb["m"],Mb["sigma"])

def get_propbability_sum(dist_param,pattern_arr):
    probability_sum = 0.0
    for pattern in pattern_arr:
        probability_sum += get_propbability(pattern,dist_param)/P_num(pattern)
    return probability_sum

def get_updated_probability_dist(dist_param,pattern_arr):
    probability_sum = 0.0
    for pattern in pattern_arr:
        probability_sum += get_propbability(pattern,dist_param)/P_num(pattern)
    return probability_sum / len(pattern_arr)

def get_updated_probability_ave(dist_param,pattern_arr):
    probability_sum = 0.0
    for pattern in pattern_arr:
        probability_sum += get_propbability(pattern,dist_param)/P_num(pattern) * pattern
    return probability_sum / get_propbability_sum(dist_param,pattern_arr)

def get_updated_probability_sigma(dist_param,pattern_arr):
    probability_sum = 0.0
    ave = get_updated_probability_ave(dist_param,pattern_arr)
    for pattern in pattern_arr:
        probability_sum += (get_propbability(pattern,dist_param)/P_num(pattern)) * (pattern - ave) ** 2
    return probability_sum / get_propbability_sum(dist_param,pattern_arr)

    

# T1
print('P(X = 4|MA) = {:.2f}'.format(norm.pdf(4,Ma["m"],Ma["sigma"])))
print('P(X = 4|MB) = {:.2f}'.format(norm.pdf(4,Mb["m"],Mb["sigma"])))
print(get_propbability(4,Ma))

print('P(Y = A|X = 4,M) = {:.2f}'.format((norm.pdf(4,Ma["m"],Ma["sigma"]) )/P_num(4)))
print('P(Y = B|X = 4,M) = {:.2f}'.format((norm.pdf(4,Mb["m"],Mb["sigma"]) )/P_num(4)))

print('P(X = 5|MA) = {:.2f}'.format(norm.pdf(5,Ma["m"],Ma["sigma"])))
print('P(X = 5|MB) = {:.2f}'.format(norm.pdf(5,Mb["m"],Mb["sigma"])))

print('P(Y = A|X = 5,M) = {:.2f}'.format((norm.pdf(5,Ma["m"],Ma["sigma"]))/P_num(5)))
print('P(Y = B|X = 5,M) = {:.2f}'.format((norm.pdf(5,Mb["m"],Mb["sigma"]))/P_num(5)))


print(get_updated_probability_dist(Ma,ball_pattern_arr))
print(get_updated_probability_dist(Mb,ball_pattern_arr))
print(get_updated_probability_ave(Ma,ball_pattern_arr))
print(get_updated_probability_ave(Mb,ball_pattern_arr))
print(get_updated_probability_sigma(Ma,ball_pattern_arr))
print(get_updated_probability_sigma(Mb,ball_pattern_arr))

# for 分で回せたら、幸せ



