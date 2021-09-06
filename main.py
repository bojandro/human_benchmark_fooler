from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def fool_reaction_time():
    url = r'https://humanbenchmark.com/tests/reactiontime'

    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(1)

    field = driver.find_element_by_class_name('view-splash')

    field.click()

    while True:
        try:
            driver.find_element_by_class_name('view-waiting')
        except Exception:
            field.click()
            break

    driver.save_screenshot(f'results/reaction_time/result-{time.time()}.png')

    time.sleep(3)

    driver.close()


def fool_memorize_the_sequence():
    url = r'https://humanbenchmark.com/tests/sequence'

    driver = webdriver.Firefox()
    driver.get(url)
    print('Connection established!')

    time.sleep(1)

    print('Starting benchmark!')
    field = driver.find_element_by_class_name('css-de05nr')
    field.click()

    squares = driver.find_element_by_class_name('squares')

    sequence_global = []

    while True:
        sequence = []
        while len(sequence_global) >= len(sequence):
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

        sequence_global.append(sequence[-1])


def fool_aim_trainer():
    url = r'https://humanbenchmark.com/tests/aim'

    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(1)

    print('Started shooting')
    field = driver.find_element_by_css_selector('.css-1k4dpwl')
    print(field)
    field.click()

    for i in range(30):
        field = driver.find_element_by_css_selector('div.css-17nnhwz:nth-child(6)')
        print(field)
        field.click()


if __name__ == '__main__':
    # fool_reaction_time()
    fool_memorize_the_sequence()
    # fool_aim_trainer()
