import random
import string
from os import path
import pandas as pd

PATH = 'C:\\Users\\saadh\\PycharmProjects\\KK2\\Data\\Data.csv'


class PasswordGenerator:
    """ Writing a program to save and crete passwords for the website """

    def __init__(self, website):
        self.website = website

    def storing_password_into_csv(self):
        """

        I need a password created here
        if the path is already there
            read csv
            if the name already exist in the csv file
             print it out the name and password
            otherwise
                write into csv file
        """
        password = self.generating_password_all_combinations()
        new_element = [{'website_name': self.website, 'Password': password}]
        try:
            df_existing = pd.read_csv(PATH)
        except:
            df_existing = pd.DataFrame.from_dict(new_element)
            df_existing.to_csv(PATH)

        if self.website in list(df_existing['website_name']):
            print(f'the name of the website is {self.website} and the password is {password}')
        else:
            df_existing = df_existing.append(new_element[0], ignore_index=True)
            print(df_existing)
            # df_existing.to_csv(PATH)

    def generating_password_all_combinations(self):
        """ Merging the password from the list to string """
        return ''.join(self.choose_random_uppercase() + self.choose_random_numbers() + self.choose_random_lowercase() \
                       + self.choose_random_punctuation())

    # ----------------- Helping Functions to generate password -------------- #
    @staticmethod
    def choose_random_uppercase() -> list:
        """ This function returns uppercase letters
        :return list of upper case letters
        """
        return random.sample(string.ascii_uppercase, 4)

    @staticmethod
    def choose_random_lowercase():
        return random.sample(string.ascii_lowercase, 4)

    @staticmethod
    def choose_random_numbers():
        return random.sample(string.digits, 4)

    @staticmethod
    def choose_random_punctuation():
        return random.sample(string.punctuation, 4)


if __name__ == '__main__':
    p = PasswordGenerator('linkedin')
    p.storing_password_into_csv()
