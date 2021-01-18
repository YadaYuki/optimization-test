import numpy as np
from scipy.stats import norm
ball_weight_pattern_arr = [8,3,6,5,7,3,6,4]
Pa = 1/2
Pb = 1/2

# TODO: to Class

# TODO:型付け
Ma = {"m":6,"sigma":1}
Mb = {"m":4,"sigma":1}

def get_ball_propbability_tsubo(ball_weight,tsubo_param):
    return norm.pdf(ball_weight,tsubo_param["m"],tsubo_param["sigma"])

def get_tsubo_conditional_probability_by_ball_weight(ball_weight,tsubo_param,P):
    return  P * get_ball_propbability_tsubo(ball_weight,tsubo_param) / (Pa * get_ball_propbability_tsubo(ball_weight,Ma) + Pb * get_ball_propbability_tsubo(ball_weight,Mb))

def get_conditional_propbability_sum(ball_weight_pattern_arr,tsubo_param,P):
    return sum([get_tsubo_conditional_probability_by_ball_weight(ball_weight,tsubo_param,P) for ball_weight in ball_weight_pattern_arr])

def get_updated_probability_to_choose(ball_weight_pattern_arr,tsubo_param,P):
    n = len(ball_weight_pattern_arr)
    return get_conditional_propbability_sum(ball_weight_pattern_arr,tsubo_param,P) / n

def get_updated_tsubo_average(ball_weight_pattern_arr,tsubo_param,P):
    return sum([get_tsubo_conditional_probability_by_ball_weight(ball_weight,tsubo_param,P) * ball_weight for ball_weight in ball_weight_pattern_arr]) / get_conditional_propbability_sum(ball_weight_pattern_arr,tsubo_param,P)

def get_updated_tsubo_sigma(ball_weight_pattern_arr,tsubo_param,P):
    average = get_updated_tsubo_average(ball_weight_pattern_arr,tsubo_param,P)
    return sum([get_tsubo_conditional_probability_by_ball_weight(ball_weight,tsubo_param,P) * (ball_weight - average) ** 2 for ball_weight in ball_weight_pattern_arr]) / get_conditional_propbability_sum(ball_weight_pattern_arr,tsubo_param,P)

def get_updated_tsubo_param(ball_weight_pattern_arr,tsubo_param,P):
    return {"m":get_updated_tsubo_average(ball_weight_pattern_arr,tsubo_param,P),"sigma":get_updated_tsubo_sigma(ball_weight_pattern_arr,tsubo_param,P)}    


# T1
print('P(X = 4|MA) = {:.2f}'.format(get_ball_propbability_tsubo(4,Ma)))
print('P(X = 4|MB) = {:.2f}'.format(get_ball_propbability_tsubo(4,Mb)))

print('P(Y = A|X = 4,M) = {:.2f}'.format(get_tsubo_conditional_probability_by_ball_weight(4,Ma,Pa)))
print('P(Y = B|X = 4,M) = {:.2f}'.format(get_tsubo_conditional_probability_by_ball_weight(4,Mb,Pb)))

print('P(X = 5|MA) = {:.2f}'.format(get_ball_propbability_tsubo(5,Ma)))
print('P(X = 5|MB) = {:.2f}'.format(get_ball_propbability_tsubo(5,Mb)))

print('P(Y = A|X = 5,M) = {:.2f}'.format(get_tsubo_conditional_probability_by_ball_weight(5,Ma,Pa)))
print('P(Y = B|X = 5,M) = {:.2f}'.format(get_tsubo_conditional_probability_by_ball_weight(5,Mb,Pb)))


print(get_updated_probability_to_choose(ball_weight_pattern_arr,Ma,Pa))
print(get_updated_probability_to_choose(ball_weight_pattern_arr,Mb,Pb))

print(get_updated_tsubo_average(ball_weight_pattern_arr,Ma,Pa))
print(get_updated_tsubo_average(ball_weight_pattern_arr,Mb,Pb))

print(get_updated_tsubo_sigma(ball_weight_pattern_arr,Ma,Pa))
print(get_updated_tsubo_sigma(ball_weight_pattern_arr,Mb,Pb))


MAX_ITER = 10

def round_dict_val(dict,round_on=2):
    round_dict = {}
    for item in dict:
        round_dict[item] = round(dict[item],round_on)
    return round_dict

for i in range(MAX_ITER):
    print("----------{}-----------".format(i))
    print("Ma:{}".format(Ma))
    print("Mb:{}".format(Mb))
    print("Pa:{}".format(Pa))
    print("Pb:{}".format(Pb))
    print("-----------------------".format(i))
    Ma_temp = get_updated_tsubo_param(ball_weight_pattern_arr,Ma,Pa)
    Mb_temp = get_updated_tsubo_param(ball_weight_pattern_arr,Mb,Pb)
    Pa_temp = get_updated_probability_to_choose(ball_weight_pattern_arr,Ma,Pa)
    Pb_temp = get_updated_probability_to_choose(ball_weight_pattern_arr,Mb,Pb)
    Ma,Mb = round_dict_val(Ma_temp,2),round_dict_val(Mb_temp,2)
    Pa,Pb = round(Pa_temp,2),round(Pb_temp,2)