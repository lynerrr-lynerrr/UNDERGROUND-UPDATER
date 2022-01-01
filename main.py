#!/usr/bin/python

import os
import platform
import json
import wget
import zipfile
import shutil

OS = platform.system()
version_download_url = 'https://underground-project.ru/version.json'

def download(DEFAULT_PATH, latestversion):
    findunder = os.path.exists(f"{DEFAULT_PATH}UNDERGROUND")
    findarchive = os.path.exists(f"{DEFAULT_PATH}UNDERGROUND-{latestversion}.zip")
    if findunder == True:
        shutil.rmtree(f"{DEFAULT_PATH}UNDERGROUND")
    if findarchive == True:
        print('\n Найден архив, пропускаю скачивание и перехожу к установке...')
        with zipfile.ZipFile(f"{DEFAULT_PATH}UNDERGROUND-{latestversion}.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{DEFAULT_PATH}")
        print('\n Установлено!')
        os.remove(f"{DEFAULT_PATH}UNDERGROUND-{latestversion}.zip")
    else:
        wget.download(download_url, f"{DEFAULT_PATH}")
        with zipfile.ZipFile(f"{DEFAULT_PATH}UNDERGROUND-{latestversion}.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{DEFAULT_PATH}")
        print("\n Установлено!")
        os.remove(f"{DEFAULT_PATH}UNDERGROUND-{latestversion}.zip")

print("\n Узнаем последнию версию UNDERGROUND...")
wget.download(version_download_url)
readversion = open('version.json', 'r')
readversionjson = json.loads(readversion.read())
latestversion = readversionjson['version']
download_url = f'https://underground-project.ru/UNDERGROUND-{latestversion}.zip'


if OS == 'Linux':
    HOME = os.getenv("HOME")
    DEFAULT_PATH = f'{HOME}/.minecraft/versions/'
    is_under_exist = os.path.exists(f"{DEFAULT_PATH}UNDERGROUND/")

elif OS == 'Windows':
    ROAMING = os.getenv("APPDATA")
    DEFAULT_PATH = ROAMING + "\\.minecraft\\versions\\"
    is_under_exist = os.path.exists(f"{DEFAULT_PATH}UNDERGROUND\\")
else:
    print("\n Ваша операционная система не поддерживается скриптом")

minecraft_exist = os.path.exists(f"{DEFAULT_PATH}")
if minecraft_exist == True:
    if is_under_exist == True:
        try:
            version_file = open(f'{DEFAULT_PATH}UNDERGROUND/version.json', 'r')
            versionjson = json.loads(version_file.read())
            version = versionjson['version']
        except:
            version = 'undefined'
        if latestversion == version:
            print('\n У вас установлена последняя версия UNDERGROUND!')
        else:
            print('\n Старая версия UNDERGROUND была найдена, обновляю...')
            download(DEFAULT_PATH, latestversion)
    else:
        print("\n Версия UNDERGROUND не была найдена, скачиваю в директорию по умолчанию...")
        download(DEFAULT_PATH, latestversion)
else:
    print("\n У вас не установлен Minecraft, либо в папке minecraft отсутствует папка versions")

print("\n Нажмите Enter чтобы выйти из программы...")
os.remove('version.json')
input()
