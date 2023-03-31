import pandas as pd


def read_files():
    cities = ['sydney', 'melbourne', 'brisbane']
    years = ['2019', '2020', '2021', '2022']
    path = '../../data/cleaned/'
    dataframes_dict = {}

    for city in cities:
        for year in years:
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


def concat_same_city(dataframes_dict):
    cities = ['sydney', 'melbourne', 'brisbane']
    dataframes_concatenated = {}

    for city in cities:
        # create list which will contain all dataframes from the current city
        city_list = []
        # add all dataframes from the current city to the list
        for key, value in dataframes_dict.items():
            if key[:-5] == city:
                city_list.append(value)

        # reset index for concatenating dataframes
        # for df in city_list:
        #     df = df.reset_index()

        # concatenate all dataframes from the current city
        df = city_list[0]
        for i in range(1, len(city_list)):
            df = pd.concat([df, city_list[i]])

        # add dataframe to dictionary of concatenated dataframes
        dataframes_concatenated[city] = df

    return dataframes_concatenated
