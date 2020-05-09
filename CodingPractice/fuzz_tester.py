####################################################################################
## Author: Akash Siddharth
## This program has been specifically designed to fulfill the requirements of
## project 2 of CAP-6135
####################################################################################
import subprocess as sp
import pickle
import os
import sys
import logging as log

test_data = "total_test_data.pickle"

def save_test_data(t_data):
    with open(test_data, 'wb') as p_handle:
        pickle.dump(t_data, p_handle)

def load_test_data():
    if not os.path.exists(test_data):
        return {'t_ctr': 0, 'bugs': [0] * 8}
    else:
        with open(test_data, 'rb') as p_handle:
            return pickle.load(p_handle)

def get_dht_markers(buffer):
    import re

    d_index = []
    dht_marker = b'\xff\xc4'
    regex = re.compile(dht_marker)

    for reg_obj in regex.finditer(buffer):
        offset = reg_obj.end() - 1
        d_index.append(offset)
    return d_index

def get_report(num_test, t_data):
    if sys.version_info[0] < 3:
        print 'Total tests executed this session: ' + repr(num_test)
        print 'Total tests executed in lifetime:' + repr(t_data['t_ctr'])
        print '{0:6} {1}'.format('Bugs', 'Frequency')
        print '-' * 20
        for i in range(len(t_data['bugs'])):
            print 'Bug {0}: {1:5d}'.format(i+1, t_data['bugs'][i])
    else:
        print('Total tests executed this session:', num_test)
        print('Total tests executed in lifetime:', t_data['t_ctr'])
        print('{0:6} {1}'.format('Bugs', 'Frequency'))
        print('-' * 20)
        for i in range(len(t_data['bugs'])):
            print('Bug {0}: {1:5d}'.format(i+1, t_data['bugs'][i]))

def fuzzer(buffer):
    import random as r

    # Fuzzing factor
    fuzz_factor = 50

    # to maintain the level of fuzzing we want
    ## fuzzing dictates how many bytes we modify at a time
    num_modifies = r.randrange(len(buffer) // fuzz_factor) + 1

    for _ in range(num_modifies):
        # generate random index and value to change
        ## The random index will be of the range within the length of the buffer
        rand_index = r.randrange(len(buffer))

        ## The random value to change should be within 0 - 255 (ascii range)
        rand_value = r.randrange(256)

        buffer[rand_index] = rand_value
    return buffer

def generate_mutant(buffer, ctr):
    file_name = '_'.join(('tester', str(ctr)))

    # Get mutated buffer using the fuzzer
    mutant_buff = fuzzer(buffer)

    with open('.'.join((file_name, 'jpg')), 'wb') as out_file:
        out_file.write(mutant_buff)

    log.debug("Mutant file created: %s", '.'.join((file_name, 'jpg')))
    return file_name

def run_test(t_data, *popen_args):
    # For python version 2.X
    if sys.version_info[0] < 3:
        ## Create subprocess
        test_obj = sp.Popen(*popen_args, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
        try:
            stdout, stderr = test_obj.communicate()
        except:
            test_obj.kill()
            test_obj.wait()
            raise
        return_code = test_obj.poll()
    else:
        # For python version 3.X
        test_obj = sp.run(*popen_args, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
        stdout = test_obj.stdout
        stderr = test_obj.stderr
        return_code = test_obj.returncode

    # Output
    log.debug("Test returncode: %s", return_code)
    log.debug("Test err: %s", stderr)
    log.debug("Test stdout: %s", stdout)

    if 'Bug' in stderr:
        # Check the bug number
        bug_no = int(stderr.split()[1][-1])
        # Check the dictionary state and change the state
        if t_data['bugs'][bug_no - 1] == 0:
            log.info('Test %d: Bug %d triggered',t_data['t_ctr'], bug_no)

            # Change the state of the index
            t_data['bugs'][bug_no - 1] += 1

            # Change the file name
            rename_file = '.'.join(('_'.join(('test',str(bug_no))), 'jpg'))
            os.rename(popen_args[0][1], rename_file)
            log.info('%s remaned to %s', popen_args[0][1], rename_file)
        else:
            # the bug is already visited, increment the counter
            t_data['bugs'][bug_no - 1] += 1

            # delete the file
            log.debug('Bug %d has already been found, removing file: %s', bug_no, popen_args[0][1])
            os.remove(popen_args[0][1])
    else:
        # Otherwise delete the jpeg file and the bmp file (if exists)
        log.debug('Bug not found. Removing file: %s', popen_args[0][1])
        if os.path.exists(popen_args[0][1]):
            os.remove(popen_args[0][1])

        bmp_file = '.'.join((popen_args[0][1].split('.')[0], 'bmp'))
        if os.path.exists(bmp_file):
            log.debug('bmp file found for %s, deleting %s', popen_args[0][1], bmp_file)
            os.remove(bmp_file)

if __name__ == "__main__":
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)

    t_data = load_test_data()

    # Number of tests to perfom
    num_test = 1000

    log.debug('Bug Register %s', t_data['bugs'])

    # Read the jpeg file
    with open('cross.jpg', 'rb') as in_file:
        # Generate random numbers
        for itr in range(num_test):
            # Load test counter
            log.debug("Test: %d", t_data['t_ctr'])

            buff = bytearray(in_file.read())
            log.debug("Buffer Length: %d", len(buff))

            # Write the mutant file
            out_file = generate_mutant(buff, t_data['t_ctr'])

            # Once the file is generated, run the test
            test_args = ["./jpg2bmp", '.'.join((out_file, 'jpg')), '.'.join((out_file, 'bmp'))]
            run_test(t_data, test_args)

            # Restart the file pointer back to zero
            in_file.seek(0)

            # increment test counter
            t_data['t_ctr'] += 1

    # Bug trigger report
    get_report(num_test, t_data)

    # save_test counter state
    save_test_data(t_data)
