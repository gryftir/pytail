import unittest
import os
import subprocess

#helper functions


def get_program_dir():
    current = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(current, '..'))


def get_program_name():
    return get_program_dir() + '/./pytail.py'


def get_test_file_name():
    return get_program_dir() + '/test_file'




class pytail_external_Test(unittest.TestCase):
    prog = get_program_name()
    test_file = get_test_file_name()
    test_string = subprocess.check_output(['cat', test_file])

    def line_end_file_test(self):
        tail_arr = ['tail', '-n 3', self.test_file]
        pytail_arr = [self.prog, '-n 3', self.test_file]
        self.assertEqual(subprocess.check_output(tail_arr),
                         subprocess.check_output(pytail_arr))

    def line_end_stdin_test(self):
        tail_arr = [ 'tail', '-n 3']
        pytail_arr = [ self.prog, '-n 3']
        tailp = subprocess.Popen(tail_arr, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
        pytailp = subprocess.Popen(pytail_arr,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        self.assertEqual(tailp.communicate(self.test_string),
                         pytailp.communicate(self.test_string))

    def line_begin_file_test(self):
        tail_arr = ['tail', '-n +3', self.test_file]
        pytail_arr = [self.prog, '-n +3', self.test_file]
        self.assertEqual(subprocess.check_output(tail_arr),
                         subprocess.check_output(pytail_arr))
        pass

    def line_begin_stdin_test(self):
        tail_arr = ['tail', '-n +3']
        pytail_arr = [ self.prog, '-n +3']
        tailp = subprocess.Popen(tail_arr, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
        pytailp = subprocess.Popen(pytail_arr,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        self.assertEqual(tailp.communicate(self.test_string),
                         pytailp.communicate(self.test_string))
        pass

    def binary_end_file_test(self):
        tail_arr = ['tail', '-c 3', self.test_file]
        pytail_arr = [self.prog, '-c 3', self.test_file]
        self.assertEqual(subprocess.check_output(tail_arr),
                         subprocess.check_output(pytail_arr))
        pass

    def binary_end_stdin_test(self):
        tail_arr =  ['tail', '-c 3']
        pytail_arr = [ self.prog, '-c 3']
        tailp = subprocess.Popen(tail_arr, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
        pytailp = subprocess.Popen(pytail_arr,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        self.assertEqual(tailp.communicate(self.test_string),
                         pytailp.communicate(self.test_string))
        pass

    def binary_begin_file_test(self):
        tail_arr = ['tail', '-c +3', self.test_file]
        pytail_arr = [self.prog, '-c +3', self.test_file]
        self.assertEqual(subprocess.check_output(tail_arr),
                         subprocess.check_output(pytail_arr))
        pass

    def binary_begin_stdin_test(self):
        tail_arr = ['tail', '-c +3']
        pytail_arr = [ self.prog, '-c +3']
        tailp = subprocess.Popen(tail_arr, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
        pytailp = subprocess.Popen(pytail_arr,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        self.assertEqual(tailp.communicate(self.test_string),
                         pytailp.communicate(self.test_string))
        pass


if __name__ == '__main__':
    unittest.main()
