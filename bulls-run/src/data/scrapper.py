# github link: https://github.com/ds-praveenkumar/kaggle
# Author: ds-praveenkumar
# file: personal-project/scrapper.py/
# Created by ds-praveenkumar at 09-06-2020 23 24
# feature: scraps news and saves to data folder

import requests
from bs4 import BeautifulSoup as bs
import config
import logging
import re
import time
import os

FORMATTER = config.LOGGING['FORMATTER']

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR,format=FORMATTER,datefmt=config.LOGGING['DATEFORMAT'])
f_handler = logging.FileHandler(config.LOGGING['LOGFILE'])
s_handler = logging.StreamHandler()
formatter = logging.Formatter(FORMATTER)

f_handler.setFormatter(formatter)
s_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.ERROR)
logger.addHandler(f_handler)
logger.addHandler(s_handler)


def get_stocks_list(url):
    try:
        raw_date = requests.get(url)
        soup = bs( raw_date.content,'html.parser')
        filtered_soups = soup.find_all('div',class_='BNeawe iBp4i AP7Wnd')
        content = []
        for li in filtered_soups:
            content.append(li.getText().split('\n')[0])
        raw_set = set(content).pop().split()
        logger.info('raw set',raw_set)
        current_price = raw_set[0]
        delta = raw_set[1]
        pt_change = raw_set[2]
        print(config.stock['Stock_name'])
        print('current_price: ',current_price )
        print('delta: ',float(delta))
        if float(delta) < 0:
            print('pt_change: neg',pt_change)
        else:
            print('pt_change: pos', pt_change)
        logger.info('price scrapper for ',config.stock['Stock_name'])

        path = os.path.join(os.path.pardir,'data',config.data['file_name']+'.csv')
        ts = time.strftime(config.data['time_format'], time.localtime())

        if not os.path.exists(path):
            file = open(path,'w')
            file.write('ts'+','+'price\n')
            file.close()


        with open(path,mode='a') as file:
            file.write(ts+'\t'+current_price+'\n')
            file.close()
        logger.info('entry in ')

    except ConnectionError:
        logger.error(ConnectionError)
        raise ConnectionError
    except BufferError:
        logger.error(BufferError)
        raise BufferError
    except Exception as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)

    finally:
        logger.info('loop executed')
        file.close()

def main():
    url = config.stock['stock_url']
    while True:
        get_stocks_list(url=url)
        time.sleep(60 * 2)

if __name__ == '__main__':
    main()



