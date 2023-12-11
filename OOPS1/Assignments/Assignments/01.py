import logging

# Shared function for logging configuration


class BaseLogger:
    def __init__(self, logger_name, level):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
        file_handler = logging.FileHandler(f'{logger_name}.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

# Creating a class for dealing problems related only to lists:


class MyList(BaseLogger):
    def __init__(self, data1):
        super().__init__(__name__, self.logger.info)
        self.data1 = data1
        self.all_234_instances = []
        self.all_456_instances = []
    """
    Problem statements
    # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """
    # 1.Try to reverse a list
    def reverse_list(self):
        try:
            if isinstance(self.data1, list):
                return self.data1[::-1]
            else:
                raise ValueError(" is not a list")
        except Exception as e:
            self.logger.error(f'Error in reverse_list method: {str(e)}')
            return None

    """
       Problem statements
       # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 2.  try to access 234 out of this list

    def access_234_instances(self):
        try:
            for item in self.data1:
                if item == 234:
                    self.all_234_instances.append(item)
                elif isinstance(item, (list, tuple)):
                    for i in item:
                        if i == 234:
                            self.all_234_instances.append(i)
                elif isinstance(item, dict):
                    if 234 in item:
                        self.all_234_instances.append(234)
                    for value in item.values():
                        if isinstance(value, (list, tuple)):
                            for v in value:
                                if v == 234:
                                    self.all_234_instances.append(v)
                        else:
                            if value == 234:
                                self.all_234_instances.append(value)

            # Logging the successful completion of the process:
            self.logger.info(f"All instances of the 234 accessed successfully.")
            return self.all_234_instances

        except Exception as e:
            # Log any exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None

    """
           Problem statements
           # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 3 . try to access 456

    def access_456_instances(self):
        try:
            for item in self.data1:
                if item == 456:
                    self.all_456_instances.append(456)
                elif isinstance(item, (list, tuple)):
                    for i in item:
                        if i == 456:
                            self.all_456_instances.append(i)
                elif isinstance(item, dict):
                    for key in item.keys():
                        if isinstance(key, int):
                                if key == 456:
                                    self.all_456_instances.append(key)
                        elif isinstance(key, (list, tuple)):
                            for k in key:
                                if k == 456:
                                    self.all_456_instances.append(k)
                    for value in item.values():
                        if isinstance(value, int):
                            if value == 456:
                                self.all_456_instances.append(value)
                            elif isinstance(value, (list, tuple)):
                                for v in value:
                                    if v == 456:
                                        self.all_456_instances.append(v)

            # Logging the successful completion of the process:
            self.logger.info(f'All instances of the 456 accessed successfully')
            return self.all_456_instances
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred in method access_456_instances: {str(e)}')
            return None

    """
           Problem statements
           # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 4 . Try to extract only a list collection form list l
    def extract_list(self):
        try:
            extracted_lists = [item for item in self.data1 if isinstance(item, list)]

            # Logging info of the successful extraction:
            self.logger.info(f'List(s) from the "main" list')
            return extracted_lists
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred in the method extract_list: {str(e)}')
            return None

    """
           Problem statements
           # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 5 . Try to extract "sudh"

    def extract_sudh(self):
        try:
            exctracted_sudh = self.data1[-1]["key1"]
            # Log info of successful extraction of 'sudh':
            self.logger.info(f"Extraction of sudh successfully done")
            return exctracted_sudh
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f"Exception occurred in method 'extract_sudh': {str(e)}")
            return None

    """
           Problem statements
           # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 6 . Try to list all the key in dict element available in list

    def list_dict_keys_in_list(self):
        try:
            list_dict_keys = []
            for item in self.data1:
                if isinstance(item, dict):
                    for key in item.keys():
                        list_dict_keys.append(key)
            # Log info for successful listing of keys into the list
            self.logger.info('Keys successfully listed to the list_dict_keys')
            return list_dict_keys
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred in method list_dict_in_list: {str(e)}')
            return None

    """
           Problem statements
           # l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    """

    # 7 . Try to extract all the value element form dict available in list

    def list_dict_values_in_list(self):
        try:
            list_dict_values = [value for item in self.data1 if isinstance(item, dict) for value in item.values()]
            # Log info of successful insertion of values into the list
            self.logger.info(f'Values successfully extracted to the list')
            return list_dict_values
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred in method list_dict_values_in_list: {str(e)}')
            return None

    # 8.  Try to write a function which is a replica of list append , extend and pop function

    def mylistappend(self, element):
        try:
            self.data1 += [element]
            # Log an info of successful insertion of an element at the last index of the list
            self.logger.info(f'Elements successfully appended')
            return self.data1
        except Exception as e:
            # Log as an exception that might occur during the process
            self.logger.error(f'Exception occurred in method "custom_append": {str(e)}')
            return None

    def mylistextend(self, elements):
        try:
            self.data1 += elements
            # Log an info of successful insertion of the elements
            self.logger.info(f"Elements successfully inserted to the list")
            return self.data1
        except Exception as e:
            # Log as an exception that might occur during the process
            self.logger.error(f"Exception occurred in method 'custom_extend': {str(e)}")
            return None

    def mylistpop(self, index):
        try:
            if not isinstance(index, int) or index < 0:
                # Log an error for invalid input
                logging.error('Invalid index provided')
                return None

            if self.data1:
                popped_element = self.data1.pop(index)
                # Log the successful pop and the popped element
                self.logger.info(f'Successful pop at index {index}. Popped element: {popped_element}')
                return popped_element
            else:
                # Log an info of an empty list
                self.logger.info('List is empty')
                return None
        except IndexError as e:
            # Log an Exception if the index is out of range
            logging.error(f'Index out of range: {str(e)}')
            return None
        except Exception as e:
            # Log an Exception that might occur during the process
            logging.error(f'Exception occurred in method "custom_pop": {str(e)}')
            return None

    # 9.  Try to write a lambda function which can return a concatenation of all the string that we will pass

    def concat_strings(self, *args):
        try:
            result = ''.join(args)
            # Logging info of concatenation:
            self.logger.info(f'Concatenation successfully done')
            return result
        except Exception as e:
            # Log as an exception that might occur during the process
            self.logger.error(f'Exception occurred in method "concat_strings: {str(e)}"')
            return None


# This class will handle strings related problems

class MyString(BaseLogger):
    def __init__(self, data2):
        self.data2 = data2
        super().__init__(__name__, self.logger.info)

    # s = "this is My First Python programming class and i am learNING python string and its function"

    # 1 . Try to extract from index one to index 300 with a jump of 3
    def extract_with_jumps(self):
        try:
            result = self.data2[1:301:3]
            # Log an info about successful extraction with the desired jump
            self.logger.info(f'Data successfully extracted with the desired jump')
            return result
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None

    # s = "this is My First Python programming class and i am learNING python string and its function"

    # 2. Try to reverse a string without using reverse function

    def rev_string(self):
        try:
            result = self.data2[::-1]
            # Log an info that data successfully reversed without reverse function
            self.logger.info(f'Data successfully reversed without the reverse function')
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None

    # s = "this is My First Python programming class and i am learNING python string and its function"

    # 3. Try to split a string after conversion of entire string in uppercase

    def split_and_upper(self):
        try:
            # Split the string with the space and then convert each element with the uppercase
            split_string = self.data2.split()
            uppercase_split = [word.upper() for word in split_string]
            # Log an info that strings have split and then converted each element with the uppercase
            self.logger.info(f'Strings have been successfully spilt and then converted into the uppercase')
            return uppercase_split
        except Exception as e:
            # Log an exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None

    # s = "this is My First Python programming class and i am learNING python string and its function"

    # 4. try to convert the whole string into lower case

    def lower_string(self):
        try:
            # Log an info that strings converted to lower successfully
            self.logger.info(f'Strings have been converted to lower successfully')
            return self.data2.lower()

        except Exception as e:
            # Log as an exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None

    # s = "this is My First Python programming class and i am learNING python string and its function"

    # 5 . Try to capitalize the whole string

    def capitalize(self):
        try:
            # Log an info that strings capitalized successfully
            self.logger.info(f'Strings have been capitalized successfully')
            return self.data2.capitalize()
        except Exception as e:
            # Log as an exception that might occur during the process
            self.logger.error(f'Exception occurred: {str(e)}')
            return None


# Test your classes with the provided data(s)
l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]

# For List

mylist = MyList(l)
print("1. Reversed List:", mylist.reverse_list())
print("2. Access Element 234:", mylist.access_234_instances())
print("3. Access Element 456:", mylist.access_456_instances())
print("4. Extracted Lists:", mylist.extract_list())
print("5. Extracted String:", mylist.extract_sudh())
print("6. List of Dict Keys:", mylist.list_dict_keys_in_list())
print("7. List of Dict Values:", mylist.list_dict_values_in_list())

# Testing custom append, extend, and pop
print("8a After Custom Append:", mylist.mylistappend(99))
print("8b After Custom Extend:", mylist.mylistextend([10, 20, 30]))
print("8c After Custom Pop:", mylist.mylistpop(4))

# Testing lambda function
concatenate = mylist.concat_strings
print("9. Concatenated Strings:", concatenate("Hello", " ", "World"))

# For String

s = "this is My First Python programming class and i am learNING python string and its function"

mystring = MyString(s)
print(f'Data successfully extracted with the desired jump: {mystring.extract_with_jumps()}')
print(f'Data successfully reversed without the reverse function: {mystring.rev_string()}')
print(f'Strings have been successfully spilt and then converted into the uppercase: {mystring.split_and_upper()}')
print(f'Strings have been converted to lower successfully: {mystring.lower_string()}')
print(f'Strings have been capitalized successfully: {mystring.capitalize()}')