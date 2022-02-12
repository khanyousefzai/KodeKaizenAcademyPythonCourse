import random
import string
from os import path
import pandas as pd
import os


class PasswordGenerator:
    """ Writing a program to save and create safe passwords for the website"""

    def __init__(self, website):
        self.website = website

    def storing_password_into_csv(self):
        new_element = [{'website_name': self.website, 'Password': self.generating_password()}]
        if path.exists('Data\\Data.csv'):
            df_existing = pd.read_csv('Data\\Data.csv')
            if self.website in list(df_existing.website_name):
                self.reading_csv_data()
            else:
                df_existing = df_existing.append(new_element[0], ignore_index=True)
                print(df_existing)
                df_existing.to_csv('Data\\Data.csv', index=False)
        else:
            os.mkdir('Data')
            df = pd.DataFrame.from_dict(new_element)
            print(df)
            df.to_csv('Data\\Data.csv', index=False)

    def reading_csv_data(self):
        try:
            df = pd.read_csv('Data\\Data.csv')
        except FileNotFoundError:
            print('File does not exist')
        if self.website in list(df.website_name):
            password = list(df.loc[df['website_name'] == self.website, 'Password']).pop()
            print(f'The password of the website {self.website} is {password}')

    def generating_password(self) -> str:
        """ Merging the password from list to string """
        return ''.join(
            self.choose_random_uppercase() + self.choose_random_numbers() + self.choose_random_lowercase() + self.choose_random_punctuation())

    # ----------------------- Helping Function in Generating Password ---------------------------- #
    def choose_random_uppercase(self) -> list:
        """ This function returns 4 uppercase """
        return random.sample(string.ascii_uppercase, 4)

    def choose_random_numbers(self) -> list:
        """ This function returns 4 digit number """
        return random.sample(string.digits, 4)

    def choose_random_lowercase(self) -> list:
        """ This function returns 4 lower case """
        return random.sample(string.ascii_lowercase, 4)

    def choose_random_punctuation(self) -> list:
        """ This function returns 4 punctuation letters """
        return random.sample(string.punctuation, 4)


if __name__ == '__main__':
    p = PasswordGenerator('linkedin')
    p.storing_password_into_csv()