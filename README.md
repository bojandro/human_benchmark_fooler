# Human benchmark fooler

<br>

## Summary

A set of `Python` scripts with `Selenium` designed to surpass human limits in accomplishing simple tasks available on <a href='https://humanbenchmark.com/'> https://humanbenchmark.com/. </a>

<br>

## Installation

Instructions are written for `Ubuntu` and I'm not sure if they are going to work on other OS.

<br>
Create virtual environment.

```shell
$ python3 -m venv env
```

<br>
Activate virtual environment.

```shell
$ source env/bin/activate
```

<br>
Install requirements.

```shell
(env) $ pip install -r requirements.txt
```

<br>

## Running

Run scripts.
```shell
(env) .../human_benchmark_fooler$ python3 main.py
```

<br>

Some tests are theoretically infinite (like sequence memory one), so functions that are fooling those test have `goal` parameter.

Function call example is available in `main.py` file.
```python
if __name__ == '__main__':
    fooler_hof(fool_reaction_time_test)
    fooler_hof(fool_sequence_memory_test, 10)
```

<br>

## Additional Info

The `Selenium` web driver for `Firefox` is `geckodriver`, so you will need to install it.
```shell
$ export GV=v0.29.0
$ wget "https://github.com/mozilla/geckodriver/releases/download/$GV/geckodriver-$GV-linux64.tar.gz"
$ tar xvzf geckodriver-$GV-linux64.tar.gz
$ chmod +x geckodriver
$ sudo cp geckodriver /usr/local/bin/
```

<br>

## Reference

Official website
- [Human Benchmark](https://humanbenchmark.com/)
- [Firefox](https://www.mozilla.org/)
- [Geckodriver](https://github.com/mozilla/geckodriver/)
