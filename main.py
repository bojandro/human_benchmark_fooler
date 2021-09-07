from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os


URLS = {
    'fool_reaction_time': r'https://humanbenchmark.com/tests/reactiontime',
    'fool_memorize_the_sequence': r'https://humanbenchmark.com/tests/sequence',
    'fool_aim_trainer': r'https://humanbenchmark.com/tests/aim',
    'fool_number_memory': r'https://humanbenchmark.com/tests/number-memory',
    'fool_chimp_test': r'https://humanbenchmark.com/tests/chimp'
}


def check_and_create_dir(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)
    return


def fooler_hof(func, goal: int = 10):
    def wrapper(*args, **kwargs):
        global URLS

        # Print in terminal
        func_name = func.__name__
        print(f'Starting {func_name}!')

        # Initialize webdriver
        driver = webdriver.Firefox()
        driver.get(URLS[func_name])

        # Call a function
        func(driver, goal)

        # Save screenshot
        path = f'results/{func_name}'
        check_and_create_dir(path)
        driver.save_screenshot(os.path.join(path, f'result-{datetime.now()}.png'))

        # Close tab
        driver.close()
    return wrapper


def fool_reaction_time(driver: webdriver, goal):
    number_of_shots = 5
    field = driver.find_element_by_class_name('view-splash')

    for i in range(number_of_shots):
        field.click()

        while True:
            if 'view-go' in field.get_attribute('class'):
                field.click()
                break


def fool_memorize_the_sequence(driver: webdriver, goal):
    field = driver.find_element_by_class_name('css-de05nr')
    field.click()

    squares = driver.find_element_by_class_name('squares')
    sequence_global_len = 0

    for _ in range(goal):
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


def fool_aim_trainer(driver: webdriver, goal):
    number_of_shots = 30
    field = driver.find_element_by_css_selector('.css-1k4dpwl')
    field.click()

    for i in range(number_of_shots):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]').click()


def fool_number_memory(driver: webdriver, goal):
    time_counter = 2.0

    for _ in range(goal):
        start_button = driver.find_element_by_class_name('css-de05nr.e19owgy710')
        start_button.click()

        num = driver.find_element_by_class_name('big-number').text

        time.sleep(time_counter)

        input_field = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input')
        input_field.send_keys(num)
        input_field.submit()

        time_counter += 0.8


def fool_chimp_test(driver, goal):
    number_of_blocks = 4

    for _ in range(goal - number_of_blocks):
        start_button = driver.find_element_by_class_name('css-de05nr.e19owgy710')
        start_button.click()

        for i in range(number_of_blocks):
            block = driver.find_element_by_css_selector(f'div[data-cellnumber="{i + 1}"]')
            block.click()

        number_of_blocks += 1


if __name__ == '__main__':
    fooler_hof(fool_reaction_time, 7)()
    fooler_hof(fool_aim_trainer, 7)()
    fooler_hof(fool_memorize_the_sequence, 7)()
    fooler_hof(fool_number_memory, 7)()
    fooler_hof(fool_chimp_test, 7)()
