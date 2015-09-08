## Race condition exploit
Tool to help with the exploitation of web application race conditions

## Usage

```console
$ python rc-exploit --help
usage: rc-exploit [-h] [--threads THREADS] plugin ...

Race condition exploiter

positional arguments:
  plugin             Python module to load requests from (ie. paypal.hack will
                     load python module from paypal/hack.py)
  remainder

optional arguments:
  -h, --help         show this help message and exit
  --threads THREADS  Number of threads/connections to use
$
```

## Example plugin run

There is an example plugin you should use to write yours at `plugins/example.py`, once
you've finished that step run:

```console
$ python rc-exploit --threads 10 plugins.your_race_condition_hack
...
```