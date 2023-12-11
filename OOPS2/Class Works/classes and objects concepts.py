import logging

class AnimalKingdom:
    def __init__(self, head, nose, heart, legs, arms=0):
        self.head = head
        self.nose = nose
        self.heart = heart
        self.arms = arms
        self.legs = legs

        # Setting up logging
        logging.basicConfig(filename='animal_kingdom.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def human(self):
        try:
            # Logic for human characteristics
            logging.info(f'This is a human with {self.head} head, {self.nose} nose, {self.heart} heart, {self.legs} legs, and a stomach')
        except Exception as e:
            logging.error(f'Error in human(): {str(e)}')

    def dog(self):
        try:
            # Logic for dog characteristic
            logging.info(f'This a dog with {self.head} head, {self.nose} nose, {self.heart} heart, {self.legs} legs, and a stomach')
        except Exception as e:
            logging.error(f'Error in dog(): {str(e)}')

    def snake(self):
        try:
            # Logic for snake characteristic
            logging.info(f'This is a snake')
        except Exception as e:
            logging.error(f'Error in snake(): {str(e)}')

# Example usage:
try:
    human_instance = AnimalKingdom(head=1, nose=1, heart=1, legs=2, arms=2)
    human_instance.human()

    dog_instance = AnimalKingdom(head=1, nose=1, heart=1, legs=4)
    dog_instance.dog()

    snake_instance = AnimalKingdom(head=0, nose=0, heart=0, legs=0)
    snake_instance.snake()

except Exception as e:
    logging.error(f'Error in Example usage: {str(e)}')

