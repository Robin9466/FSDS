from classes_and_objects_assmnts import MyList

l = [4,4.45,5,6, [5,5,6,65,4],(5,5,7,5,4,), [5,5,5,743,33,44], {'s':546456, 'f':7567567}]

# Create an instance of MyList with the provided list and the BaseLogger instance
obj1 = MyList(l)

# Call the 'extract_list' method
extracted_lists = obj1.extract_list()
print(extracted_lists)
