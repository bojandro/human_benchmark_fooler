from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import os


URLS = {
    'fool_reaction_time': r'https://humanbenchmark.com/tests/reactiontime',
    'fool_memorize_the_sequence': r'https://humanbenchmark.com/tests/sequence',
    'fool_aim_trainer': r'https://humanbenchmark.com/tests/aim'
}


def check_and_create_dir(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)
    return


def fooler_hof(func):
    def wrapper(*args, **kwargs):
        global URLS

        # Print in terminal
        func_name = func.__name__
        print(f'Starting {func_name}!')

        # Initialize webdriver
        driver = webdriver.Firefox()
        driver.get(URLS[func_name])

        # Call a function
        func(driver)

        # Save screenshot
        path = f'results/{func_name}'
        check_and_create_dir(path)
        driver.save_screenshot(os.path.join(path, f'result-{datetime.now()}.png'))

        # Close tab
        driver.close()
    return wrapper


def fool_reaction_time(driver: webdriver):
    field = driver.find_element_by_class_name('view-splash')

    for i in range(5):
        field.click()

        while True:
            if 'view-go' in field.get_attribute('class'):
                field.click()
                break


def fool_memorize_the_sequence(driver: webdriver):
    field = driver.find_element_by_class_name('css-de05nr')
    field.click()

    squares = driver.find_element_by_class_name('squares')
    sequence_global_len = 0

    while True:
        sequence = []
        while sequence_global_len >= len(sequence):
            try:
                curr_square = squares.find_element_by_class_name('active')
                sequence.append(curr_square)
                print(f'Detected active square {len(sequence)} {curr_square}!')
                time.sleep(0.5)
            except NoSuchElementException:
                pass

        print('Reproducing the sequence')

        time.sleep(1)

        for el in sequence:
            el.click()

        sequence_global_len += 1


def fool_aim_trainer(driver: webdriver):
    field = driver.find_element_by_css_selector('.css-1k4dpwl')
    field.click()

    for i in range(30):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]').click()


if __name__ == '__main__':
    fooler_hof(fool_reaction_time)()
    fooler_hof(fool_aim_trainer)()
    fooler_hof(fool_memorize_the_sequence)()
    pass
