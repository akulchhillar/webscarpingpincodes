from bs4 import BeautifulSoup as bs
import requests
import openpyxl
import os


os.chdir("C:\Users\Akul Chhillar\Desktop\store web scarping")

url = "https://stores.cosmoprofbeauty.com/"

page = requests.get(url)

soup = bs(page.content,'html.parser')



def pincode():
    wb = openpyxl.load_workbook('data.xlsx')

    sheet = wb.get_sheet_by_name("Sheet1")

    count = 2

    for i in soup.find_all("div", class_="mapListItemWrap"):

        soupt = bs(requests.get(i.a["href"]).content, 'html.parser')

        for x in soupt.find_all("div", class_="mapListItemWrap"):

            soupn = bs(requests.get(x.a["href"]).content, 'html.parser')

            for z in soupn.find_all("div", class_="csz"):
                sheet.cell(count, 3).value = z.text
                count = count + 1

    wb.save('data.xlsx')

pincode()


