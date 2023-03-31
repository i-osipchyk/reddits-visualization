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
