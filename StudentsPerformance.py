import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics

dataframe = pd.read_csv("StudentsPerformance.csv")
data_list = dataframe["reading score"].to_list()

data_mean = statistics.mean(data_list)
data_median = statistics.median(data_list)
data_mode = statistics.mode(data_list)
data_std_deviation = statistics.stdev(data_list)

data_first_std_deviation_start, data_first_std_deviation_end = data_mean - \
    data_std_deviation, data_mean+data_std_deviation
data_second_std_deviation_start, data_second_std_deviation_end = data_mean - \
    (2*data_std_deviation), data_mean+(2*data_std_deviation)
data_third_std_deviation_start, data_third_std_deviation_end = data_mean - \
    (3*data_std_deviation), data_mean+(3*data_std_deviation)

data_list_of_data_within_1_std_deviation = [
    result for result in data_list if result > data_first_std_deviation_start and result < data_first_std_deviation_end]
data_list_of_data_within_2_std_deviation = [result for result in data_list if result >
                                            data_second_std_deviation_start and result < data_second_std_deviation_end]
data_list_of_data_within_3_std_deviation = [
    result for result in data_list if result > data_third_std_deviation_start and result < data_third_std_deviation_end]

print("Mean of this data is {}.".format(data_mean))
print("Median of this data is {}.".format(data_median))
print("Mode of this data is {}.".format(data_mode))

print("{}% of data for data lies within 1 standard deviation".format(
    len(data_list_of_data_within_1_std_deviation)*100.0/len(data_list)))
print("{}% of data for data lies within 2 standard deviations".format(
    len(data_list_of_data_within_2_std_deviation)*100.0/len(data_list)))
print("{}% of data for data lies within 3 standard deviations".format(
    len(data_list_of_data_within_3_std_deviation)*100.0/len(data_list)))

fig = ff.create_distplot([data_list], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[data_mean, data_mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[data_first_std_deviation_start, data_first_std_deviation_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[data_first_std_deviation_end, data_first_std_deviation_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[data_second_std_deviation_start, data_second_std_deviation_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[data_third_std_deviation_end, data_third_std_deviation_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()
