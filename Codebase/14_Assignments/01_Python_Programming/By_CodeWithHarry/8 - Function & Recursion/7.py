# WAP function to remove a given word from a list and strip it at the same time.

def remove_strip(word_list, remove_index):
	removed_word = word_list.pop(remove_index)
	stripped = removed_word.strip()
	return stripped
my_list = ['          Hello World!  ' , '  How are you ', 'fcuk you   ', 'bad ass', 'love you', 'miss you', ' I love you', 'I missed you ']
index_to_remove = 2
result = remove_strip(my_list, index_to_remove)
print("removed word after stripping:", result)
