import pandas as pd 
import statistics
import csv

df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)
height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)

print("Mean, median and mode of height is {}, {} and {}".format(height_mean, height_median, height_mode))
print("Mean, median and mode of weight is {}, {} and {}".format(weight_mean, weight_median, weight_mode))

height_first_std_deviation_start, height_first_std_deviation_end= height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end= height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end= height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end= weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end= weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end= weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)

height_list_of_data_within_one_std_deviation=[result for result in height_list if result>height_first_std_deviation_start and result<height_first_std_deviation_end]
height_list_of_data_within_two_std_deviation=[result for result in height_list if result>height_second_std_deviation_start and result<height_second_std_deviation_end]
height_list_of_data_within_three_std_deviation=[result for result in height_list if result>height_third_std_deviation_start and result<height_third_std_deviation_end]

weight_list_of_data_within_one_std_deviation=[result for result in weight_list if result>weight_first_std_deviation_start and result<weight_first_std_deviation_end]
weight_list_of_data_within_two_std_deviation=[result for result in weight_list if result>weight_second_std_deviation_start and result<weight_second_std_deviation_end]
weight_list_of_data_within_three_std_deviation=[result for result in weight_list if result>weight_third_std_deviation_start and result<weight_third_std_deviation_end]

print("{}% of data for height lie within 1 standard deviation".format(len(height_list_of_data_within_one_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lie within 2 standard deviation".format(len(height_list_of_data_within_two_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lie within 3 standard deviation".format(len(height_list_of_data_within_three_std_deviation)*100.0/len(height_list)))

print("{}% of data for weight lie within 1 standard deviation".format(len(weight_list_of_data_within_one_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lie within 2 standard deviation".format(len(weight_list_of_data_within_two_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lie within 3 standard deviation".format(len(weight_list_of_data_within_three_std_deviation)*100.0/len(weight_list)))