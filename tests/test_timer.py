from graal_utils import Timer, timed
from time import sleep
import re

ansicolor = r'\x1b\[\d\d?m'

class TestTimer:
    def test_context_manager_without_options_without_exception(self, capsys):
        with Timer():
            sleep(.1)
        captured = capsys.readouterr()

        assert re.match(ansicolor + ansicolor.join([
            r'Execution started on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds',
            r'.\n',
            r'\n',
            r'\nExecution completed in ',
            r'\d.\d\ds',
            r' on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds',
            r'.\n',
            r'\n']),
                        captured.out)

    def test_context_manager_without_options_with_exception(self, capsys):
        try:
            with Timer():
                sleep(.1)
                raise RuntimeError
        except RuntimeError:
            pass

        captured = capsys.readouterr()

        assert re.match(ansicolor + ansicolor.join([
            r'Execution started on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds',
            r'.\n',
            r'\n',
            r'\nExecution terminated after ',
            r'\d.\d\ds',
            r' on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds' + ansicolor,
            r'.\n',
            r'\n']),
                        captured.out)

    def test_func_wrapper_without_options_without_exception(self, capsys):
        @Timer
        def func(a=1):
            print(a)

        func()

        captured = capsys.readouterr()

        assert re.match(ansicolor + ansicolor.join([
            r'Execution started on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds',
            r'.\n',
            r'\n',
            r'\nExecution completed in ',
            r'\d.\d\ds',
            r' on ',
            r'\d\d\d\d-\d\d-\d\d \d\dh\d\dm\d\ds',
            r'.\n',
            r'\n']),
                        captured.out)
