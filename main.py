from audio import audio_test
from mmse import mmse_test
from test_oled import display_test
from pulse import pulse_test

while(1):
    test_freq = input("choose the test with freq : ")
    if test_freq == 'one day':
        pulse_test()
    elif test_freq == 'one month':
        pulse_test()
        audio_test()
        times = input("request times = ")
        display_test(times)
    elif test_freq == 'half year':
        pulse_test()
        audio_test()
        times = input("request times = ")
        display_test(times)
        mmse_test()