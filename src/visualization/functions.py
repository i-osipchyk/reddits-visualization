import pandas as pd


def read_files(cities_, years_):
    path = '../../data/cleaned/'
    dataframes_dict = {}

    for city in cities_:
        for year in years_:
            df = pd.read_csv(path + city.capitalize() + '/' + city + '_' + year + '.csv')
            dataframes_dict[city + '_' + year] = df

    return dataframes_dict


def remove_columns(dataframes_dict):
    columns = ['author', 'author_created_utc', 'body', 'subreddit', 'Segment']
    dataframes_dict_copy = dataframes_dict
    for key, value in dataframes_dict_copy.items():
        df = value.drop(columns, axis=1)
        dataframes_dict[key] = df

    return dataframes_dict


def set_datetime_index(dataframes_dict):
    dataframes_dict_copy = dataframes_dict
    for key, value in dataframes_dict_copy.items():
        df = value
        df.set_index('utc_datetime_str', inplace=True)
        df.index = pd.to_datetime(df.index, errors='coerce')
        dataframes_dict[key] = df

    return dataframes_dict


def read_and_clean():
    dataframes_dict = read_files()
    dataframes_dict = remove_columns(dataframes_dict)
    dataframes_dict = set_datetime_index(dataframes_dict)

    return dataframes_dict
