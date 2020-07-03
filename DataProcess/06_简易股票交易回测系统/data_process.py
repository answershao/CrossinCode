import pandas as pd


def read_data(file_name):
    """
    :param file_name:
    :return: DataFrame: name price date
    """
    data = pd.read_csv(file_name, parse_dates=True, index_col=0)
    # print(data.shape)
    return data


def read_and_sample_data(file_name, mode):
    """
    DataFrame 格式读取csv 并对工作日进行重采样
    ffill方式填充数据，## 使用ffill方法，必须的
    """
    return read_data(file_name).resample(mode).ffill()