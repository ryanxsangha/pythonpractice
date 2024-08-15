import time

phrase = 'The quick brown fox jumps over the lazy dog'

word_count = len(phrase.split())

begin = input('Please type: ' + phrase + '\n' + 'Press enter when ready and again when finished.')

t0 = time.time()
attempt = input('\n')
t1 = time.time()
attempt_time = (t1 - t0)/60
wpm = str(round(word_count / attempt_time, 2))

if attempt == phrase:
    print('\n' + 'Your WPM: ' + wpm)
else:
    print('\n' + 'Typed incorrectly, please try again.')