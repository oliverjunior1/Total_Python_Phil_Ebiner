# Replace in the following sentence:
#
# "If the implementation is hard to explain, it might be a bad idea."
#
# the following pairs of words:
#
# "hard" --> "easy"
#
# "bad" --> "good"
#
# and display the sentence with both words modified.

phrase ='If the implementation is hard to explain, it might be a bad idea.'

first_change = phrase.replace('hard', 'easy')
second_change = first_change.replace('bad', 'good')

print(second_change)