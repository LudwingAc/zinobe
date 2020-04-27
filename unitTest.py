import unittest
import controller


class MyTestCase(unittest.TestCase):

    def Testgetlanguages(self):
        paises = "[{'name': 'Antarctica', 'topLevelDomain': ['.aq'], 'alpha2Code': 'AQ', 'alpha3Code': 'ATA', 'callingCodes': ['672'], 'capital': '', 'altSpellings': [], 'region': 'Polar', 'subregion': '' 'population': 1000, 'latlng': [-74.65, 4.48], 'demonym': '', 'area': 14000000.0, 'gini': None, 'timezones': ['UTC-03:00', 'UTC+03:00', 'UTC+05:00', 'UTC+06:00', 'UTC+07:00', 'UTC+08:00', 'UTC+10:00', 'UTC+12:00'], 'borders': [], 'nativeName': 'Antarctica', 'numericCode': '010', 'currencies': [{'code': 'AUD', 'name': 'Australian dollar', 'symbol': '$'}, {'code': 'GBP', 'name': 'British pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'en', 'iso639_2': 'eng', 'name': 'English', 'nativeName': 'English'}, {'iso639_1': 'ru', 'iso639_2': 'rus', 'name':'Russian', 'nativeName': 'Русский'}], 'translations': {'de': 'Antarktika', 'es': 'Antártida', 'fr': 'Antarctique', 'ja': '南極大陸', 'it': 'Antartide', 'br': 'Antártida', 'pt': 'Antárctida', 'nl': 'Antarctica', 'hr': 'Antarktika', 'fa': 'جنوبگان'}, 'flag': 'https://restcountries.eu/data/ata.svg', 'regionalBlocs': [], 'cioc': ''}]"
        pais = "Antarctica"
        self.defaultTestResult(controller.getlanguages(paises, pais))

    def TestencryptLan(self):
        lan = "English"
        self.defaultTestResult(controller.encryptLan(lan))

    def Testregister(self):
        self.defaultTestResult(controller.dbRegister('3.014928', '0.502488', '0.420692', '0.62277'))


if __name__ == '__main__':
    unittest.main()
