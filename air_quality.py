from bs4 import BeautifulSoup
import requests
import datetime
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

def scraping():
    """Sopron"""
    recourse_sp = requests.get("http://aqicn.org/city/hungary/sopron/", headers=headers)
    soup_sp = BeautifulSoup(recourse_sp.content, "lxml")

    citydiv_sp = soup_sp.find(id="citydivmain")

    air_poll_sp = citydiv_sp.find(id="aqiwgtvalue").get_text()

    air_info_sp = citydiv_sp.find(id="aqiwgtinfo").get_text()
    measurement_time_sp = citydiv_sp.find(id="aqiwgtutime").get_text()

    print(f"Current air quality in Sopron: {air_poll_sp} PM2.5, {air_info_sp}")
    print(f"Last update: {measurement_time_sp[11:]}")

    cur_time = str(datetime.datetime.now())
    print(f"Current time: {cur_time[:16]}")
    print()
    """Budapest"""
    resource_bp = requests.get("https://aqicn.org/city/hungary/budapest/bp2--szena/", headers=headers)
    soup_bp = BeautifulSoup(resource_bp.content, "lxml")


    citydiv_bp = soup_bp.find(id="citydivmain")

    air_poll_bp = citydiv_bp.find(id="aqiwgtvalue").get_text()

    air_info_bp = citydiv_bp.find(id="aqiwgtinfo").get_text()

    measurement_time_bp = citydiv_bp.find(id="aqiwgtutime").get_text()

    print(f"Current air quality in Budapest: {air_poll_bp} PM2.5, {air_info_bp}")
    print(f"Last update: {measurement_time_bp[11:]}")

    cur_time = str(datetime.datetime.now())
    print(f"Current time: {cur_time[:16]}")
    print()

while True:
    scraping()
    time.sleep(60)

