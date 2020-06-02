import time
import sqlite3
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import config


URL = 'http://localhost:8000'
SLEEP_TIME = 5
PHONEBOOK_MAX_AGE = 2 * 60 * 60
SOLVED_REP_DLY = 8
submitted = {}

def query_db(query, args=[], lri=False):
    with sqlite3.connect('phonenumbers.db') as db:
        cur = db.execute(query, args)
        rv  = cur.fetchall()
        lii = cur.lastrowid
        cur.close()
        return (rv, lii) if lri else rv

def view_posts(handle, itl):
    post_ids = query_db('SELECT id, created FROM phonebooks')
    for post_id in post_ids:
        if post_id[0] in submitted:
            submitted[post_id[0]] -= 1
            if submitted[post_id[0]] > 0:
                continue
            else:
                del submitted[post_id[0]]

        if time.time() - post_id[1] > PHONEBOOK_MAX_AGE:
            logging.info(f'Phonebook {post_id[0]} is too old ({time.time() - post_id[1]} > {PHONEBOOK_MAX_AGE}), Deleting')
            query_db('DELETE FROM phonenumbers WHERE pbid=?', [post_id[0]])
            query_db('DELETE FROM phonebooks WHERE id=?' [post_id[0]])
            continue

        logging.info(f'Iteration: {itl}-{post_id[0]}')
        try:
            handle.get(URL + '/phonebook/' + str(post_id[0]))
            source = handle.page_source
            if config.FLAG in source:
                submitted[post_id[0]] = SOLVED_REP_DLY
        except Exception as e:
            logging.warning(f'Iteration {itl}-{post_id[0]} failed with exception {e}')

        time.sleep(1)

def main(driver_loc='./geckodriver'):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=driver_loc)
    driver.get(URL)
    driver.add_cookie({'name': 'flag', 'value': config.FLAG})

    upper_itl = 1
    while True:
        view_posts(driver, upper_itl)
        time.sleep(SLEEP_TIME)
        upper_itl += 1

if __name__ == '__main__':
    import sys

    loglevel = 'INFO'
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)

    main(sys.argv[1] if len(sys.argv) > 1 else './geckodriver')
