from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import os

# Urls for the tests
URLS = {
    'fool_reaction_time_test': r'https://humanbenchmark.com/tests/reactiontime',
    'fool_sequence_memory_test': r'https://humanbenchmark.com/tests/sequence',
    'fool_aim_trainer': r'https://humanbenchmark.com/tests/aim',
    'fool_number_memory_test': r'https://humanbenchmark.com/tests/number-memory',
    'fool_verbal_memory_test': r'https://humanbenchmark.com/tests/verbal-memory',
    'fool_chimp_test': r'https://humanbenchmark.com/tests/chimp',
    'fool_visual_memory_test': r'https://humanbenchmark.com/tests/memory',
    'fool_typing_test': r'https://humanbenchmark.com/tests/typing'
}


# Service function to create missing directories for a screenshots
def check_and_create_dir(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)
    return


# Higher order function to avoid writing repeating code
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

    wrapper()
    print('Finished test!')


def fool_reaction_time_test(driver: webdriver, goal: int):
    number_of_shots = 5
    field = driver.find_element_by_class_name('view-splash')

    for i in range(number_of_shots):
        field.click()

        while True:
            if 'view-go' in field.get_attribute('class'):
                field.click()
                break


def fool_sequence_memory_test(driver: webdriver, goal: int):
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


def fool_aim_trainer(driver: webdriver, goal: int):
    number_of_shots = 30
    field = driver.find_element_by_css_selector('.css-1k4dpwl')
    field.click()

    for i in range(number_of_shots):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]').click()


def fool_number_memory_test(driver: webdriver, goal: int):
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


def fool_verbal_memory_test(driver: webdriver, goal: int):
    time.sleep(1)
    start_button = driver.find_element_by_class_name('css-de05nr.e19owgy710')
    start_button.click()

    seen_button = driver.find_element_by_css_selector('button.css-de05nr:nth-child(1)')
    new_button = driver.find_element_by_css_selector('button.css-de05nr:nth-child(3)')

    encountered_words = []

    for _ in range(goal):
        word = driver.find_element_by_class_name('word').text

        if word in encountered_words:
            seen_button.click()
        else:
            encountered_words.append(word)
            new_button.click()


def fool_chimp_test(driver: webdriver, goal: int):
    number_of_blocks = 4

    for _ in range(goal - number_of_blocks):
        start_button = driver.find_element_by_class_name('css-de05nr.e19owgy710')
        start_button.click()

        for i in range(number_of_blocks):
            block = driver.find_element_by_css_selector(f'div[data-cellnumber="{i + 1}"]')
            block.click()

        number_of_blocks += 1


def fool_visual_memory_test(driver: webdriver, goal: int):
    time.sleep(1)
    start_button = driver.find_element_by_class_name('css-de05nr.e19owgy710')
    start_button.click()

    for _ in range(goal):
        active_blocks = driver.find_elements_by_class_name('active.css-lxtdud.eut2yre1')

        time.sleep(1.5)

        for block in active_blocks:
            block.click()

        time.sleep(2)


def fool_typing_test(driver: webdriver, goal: int):
    text_field = driver.find_element_by_class_name('letters.notranslate')
    paragraph = text_field.text

    text_field.send_keys(paragraph)

    time.sleep(1)


if __name__ == '__main__':
    fooler_hof(fool_reaction_time_test)
    fooler_hof(fool_sequence_memory_test, 10)
    fooler_hof(fool_aim_trainer)
    fooler_hof(fool_number_memory_test, 7)
    fooler_hof(fool_verbal_memory_test, 100)
    fooler_hof(fool_chimp_test, 10)
    fooler_hof(fool_visual_memory_test, 8)
    fooler_hof(fool_typing_test)
