"""Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий."""
import json
import os
import csv
import pickle


def walk_dir(path):
    parent_directories = {}
    os.chdir(path)
    for path_, dirs_, files_ in os.walk(os.getcwd()):
        file_child = {}
        dir_child = {}
        par_dir = path_.split('\\')[-1]
        if dirs_:
            for dir_ in dirs_:
                path_dir = path_ + "\\" + dir_
                dir_child[dir_] = [{'type': 'dir'}, {"size": os.path.getsize(path_dir)}]
        if files_:
            for file_ in files_:
                path_file = path_ + "\\" + file_
                file_child[file_] = [{'type': 'file'}, {"size": os.path.getsize(path_file)}]
            dir_child.update(file_child)
            parent_directories[par_dir] = dir_child

    rm_empty_key = []
    for key, value in parent_directories.items():
        if value == {}:
            rm_empty_key.append(key)
    for key in rm_empty_key:
        if key in parent_directories:
            del parent_directories[key]

    return parent_directories


def write_file(dct_folders: dict):
    csv_line = ""
    with open("folders.json", 'w', encoding='utf-8') as file:
        json.dump(dct_folders, file, indent=4, ensure_ascii=False)
    with open("folders.csv", 'w', encoding='utf-8') as file1:
        file1.write("Parent`s directory,directory,{type: size}" + '\n')
        for key, value in dct_folders.items():
            for key1, value1 in value.items():
                csv_line = "\n".join([key + ',' + key1 + ','.join([str(i) for i in value1])])
                file1.write(csv_line + '\n')

    with open("foldes.pickle", 'wb') as file2:
        pickle.dump(dct_folders, file2)



write_file(walk_dir("HW"))
