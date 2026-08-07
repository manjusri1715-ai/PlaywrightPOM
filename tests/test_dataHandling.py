
import csv
import json

from openpyxl import load_workbook
import pytest
from utils.jsonHandling import jsonHandling


def test_json():
    with open('testData/credentails.json') as data:
        finalData = json.load(data)
        print(finalData)

def test_json2():
     data = jsonHandling("testData/creds.json")

# @pytest.mark.datahandling
def test_csvHandling():
    with open('testData/credentails.csv') as data:
            finalData = csv.DictReader(data)
            output = []
            for i in finalData:
                 output.append(i)

            print(output)
            # print(finalData)



def test_csvHandling_write():
    with open('testData/credentails.csv', mode='w',newline='') as data:
            finalData = csv.DictWriter(data, fieldnames=['username','password'])
            finalData.writeheader()
            finalData.writerow({'username':"tripur123_9",'password':"1234"})


# pip install openpyxl
@pytest.mark.datahandling
def test_excel():
     workbook =load_workbook('testData\\sample_creds.xlsx')
     sheet = workbook['sheet1']
     output = []
     for i in sheet.iter_rows(min_row=2, values_only=True):
          output.append(i)

     print(output)
          



    





