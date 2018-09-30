from json import JSONDecodeError
from time import sleep
import os
import requests
import json
from pprint import pprint as pp


def gettoken(uid, pwd):
    tkn = None
    try:
        data = {"username": uid, "password": pwd}
        r = requests.post(url="http://localhost:8000/api/token", data=data)
        assert r.status_code == 200
        try:
            tkn = r.json()
        except JSONDecodeError as jerr:
            print(jerr)
            raise jerr
    except AssertionError as err:
        print(err)
        print(r.status_code)
        raise Exception("Error Occured") from err

    except Exception as err:
        print(err)
        raise Exception("Decode Error not utf-8 compatible") from err

    return tkn

    # headers = {"Authorization": f"Bearer {token}"}


def getpopularity(access, refresh):
    headers = {"Authorization": f"Bearer {access}"}
    r = requests.get(url="http://localhost:8000/popularity/", headers=headers)
    sleep(.2)
    if not r.status_code == 200:
        data = {"refresh": refresh}
        print("REFRESHING TOKEN HOLA!!!!")
        r1 = requests.post(url="http://localhost:8000/api/token/refresh", data=data)
        access = r1.json().get("access")
        headers = {"Authorization": f"Bearer {access}"}
        r = requests.get(url="http://localhost:8000/popularity/", headers=headers)
    return r.content.decode("utf-8"), access


if __name__ == "__main__":
    pwd = os.environ.get("APP_USER_PWD")
    uid = os.environ.get("APP_USER_ID")
    x = gettoken(uid=uid, pwd=pwd)
    for c in range(10):
        cnt, access = getpopularity(**x)
        x["access"] = access
        print(len(cnt), access)
