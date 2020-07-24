from selenium import webdriver
from time import sleep
from random import randint
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get('https://www.instagram.com/?hl=fr')

click = 0

hashtage = ["#pythonprogramming", "#coding", "#programming", "#setup", "#inspiration", "#photography", "#frenchphotography"]


def change_and_like():
    sleep(randint(1, 5))
    like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
    like.click()
    sleep(randint(1, 5))
    change = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
    change.click()
    sleep(randint(1, 5))


def change():
    sleep(randint(1, 5))
    change = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
    change.click()
    sleep(randint(1, 5))


def follow():
    sleep(randint(1, 5))
    suivre = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
    suivre.click()


def connect():
    # connecter a instagram
    sleep(1)
    username = driver.find_element_by_name("username")
    mdp = driver.find_element_by_name("password")

    username.send_keys("your username")
    mdp.send_keys("your passeword")

    # cliquer sur ce conecter
    sleep(1)
    connect_click = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
    connect_click.click()

    sleep(5)
    driver.refresh()

    # boutons enregistrer identifiant
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button")))
    save = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    save.click()

    # boutons notification
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
    notif = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notif.click()

    # choisir le hashtag
    sleep(1)
    find = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    find.send_keys(random.choice(hashtage))

    # cliquer sur le boutons du hashtag
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div/div[1]/span")))
    hashtag_button = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div/div[1]/span")
    hashtag_button.click()

    # cliquer sur la première photo
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]")))
    first_pic = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]")
    first_pic.click()


connect()

choix = True, False

while click < 50:
    x = random.choice(choix)
    if x:
        change_and_like()
        click += 1
    else:
        change()
        if random.randint(0, 100) < 10:
            follow()
else:
    print("bye")
    driver.close()

driver.close()
