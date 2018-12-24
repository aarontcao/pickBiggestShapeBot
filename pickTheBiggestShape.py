from selenium import webdriver
import math
import time

#uses the Shoelace formula to determine the area of the polygon
def shoelaceArea(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area
    

#creates the webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://pick-the-bigger-shape.herokuapp.com/")

#creates and clicks the button on the website to start the game
python_button = driver.find_elements_by_xpath("//button[@type='button' and @id='start-button' and @class='btn btn-primary']")[0]
python_button.click()

#automates the game
n = 0
while(n <= 978):

    #finds the polygon elements
    leftClick = driver.find_element_by_id("shape0")
    rightClick = driver.find_element_by_id("shape1")
    shapes = driver.find_elements_by_tag_name("polygon")
    polygon0 = shapes[0].get_attribute("points").split()
    polygon1 = shapes[1].get_attribute("points").split()

    #makes lists of float tuples of the points
    shape0 = []
    shape1 = []
    for s in polygon0:
        temp = s.split(',')
        for i in range(len(temp)):
            temp[i] = float(temp[i])
        shape0.append(tuple(temp))
    for s in polygon1:
        temp = s.split(',')
        for i in range(len(temp)):
            temp[i] = float(temp[i])
        shape1.append(tuple(temp))

    #calculates the area
    area0 = shoelaceArea(shape0)
    area1 = shoelaceArea(shape1)
    if (area0 > area1):
        leftClick.click()
    else:
        rightClick.click()
    n += 1
