# github link: https://github.com/ds-praveenkumar/kaggle
# Author: ds-praveenkumar
# file: personal-project/config.py/
# Created by ds-praveenkumar at 09-06-2020 23 18
# feature:

stock = dict(
    stock_url =  'https://shorturl.at/lsxMT',
    Stock_name = 'DMART',
    sleep_time = (60 * 2),
)

data = dict(
    file_name = 'dmart',
    time_format = '%Y-%m-%d %H:%M:%S',


)

LOGGING = dict(
    FORMATTER = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d]  %(message)s',
    DATEFORMAT = '%d-%b-%y %H:%M:%S',
    LOGFILE = 'bulls-run.log',
)