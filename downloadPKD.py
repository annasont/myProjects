#! /usr/bin/python3
'''downloadPKD.py: on Tuesdays to Fridays downloads current PKD reports as Excel spreadsheets and moves them to the chosen folder.
On Mondays downloads in addition reports from Saturday and Sunday.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, pyautogui, os, shutil, datetime

def openPage():
    # Opens webbrowser on the webpage with PKD reports
    browser = webdriver.Firefox()
    browser.get('https://www.pse.pl/dane-systemowe/plany-pracy-kse/plan-koordynacyjny-dobowy-pkd/wielkosci-podstawowe')
    return browser

def downloadExcel(browser):
    # Chooses Excel-format and clicks download
    try:
        reportInExcel = browser.find_element_by_link_text('Excel')
        reportInExcel.click()
    except:
        print('not found')

def findWeekendExcel(browser, day):
    # Changes date
    try:
        parameters = browser.find_element_by_link_text('Parametry')
        parameters.click()
        input = browser.find_element_by_id('__param__VisioPortlet_WAR_visioneoportlet_INSTANCE_oyPkFYlXjRRu_data')
        input.clear()
        input.send_keys(day.strftime(r'%Y-%m-%d'))
        confirm = browser.find_element_by_xpath('//button[normalize-space()="Zatwierdź"]')
        confirm.click()
    except:
        print('not found')

def saveFile(ax, ay, bx, by):
    # When using linux window with options “Open with” and “Save file” shows up. 
    # Function uses pyautogui to choose the option “Save file” and “OK”. Adjust coordinates to your screen.
    for i in range(5):
        time.sleep(1)
    pyautogui.click(ax, ay)
    time.sleep(2)
    pyautogui.click(bx, by)

def moveToFolder(sourceFolder, destinationFolder):
    # Moves files to given destination
    for filename in os.listdir(sourceFolder):
        if filename.startswith('PL_PKD'):
            source = os.path.join(sourceFolder, filename)
            destination = os.path.join(destinationFolder, filename)
            if not filename in os.listdir(destinationFolder):
                shutil.move(source, destination)
                print('File %s moved to destination folder.' % filename )
            else:
                print('Did not move file %s. File was already in the destination folder.' % filename)


if datetime.datetime.today().weekday() != 0:
    browser = openPage()
    downloadExcel(browser)
    saveFile(506, 470, 910, 540)
    moveToFolder('/home/ania/Downloads', '/home/ania/Documents/PKD')
else:
    browser = openPage()
    downloadExcel(browser)
    saveFile(506, 470, 910, 540)
    moveToFolder('/home/ania/Downloads', '/home/ania/Documents/PKD')

    Monday = datetime.datetime.now()
    oneDay = datetime.timedelta(days=1)
    Sunday = Monday - oneDay
    Saturday = Sunday - oneDay

    findWeekendExcel(browser, Saturday)
    downloadExcel(browser)
    saveFile(506, 470, 910, 540)
    moveToFolder('/home/ania/Downloads', '/home/ania/Documents/PKD')

    findWeekendExcel(browser, Sunday)
    downloadExcel(browser)
    saveFile(506, 470, 910, 540)
    moveToFolder('/home/ania/Downloads', '/home/ania/Documents/PKD')

