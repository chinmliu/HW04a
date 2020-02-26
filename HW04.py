#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests


def get_repo(id):
    url = "https://api.github.com/users/" + id + "/repos"
    r = requests.get(url)
    return r.json()


def get_commits(id):
    j = get_repo(id)
    list = []
    for item in j:
        c_url = "https://api.github.com/repos/" + id + "/" + item["name"] + "/commits"
        r_2 = requests.get(c_url)
        j_2 = r_2.json()
        list.append([item["name"], len(j_2)])
    return list


def get_results(id):
    result = get_commits(id)
    for i in result:
        print("Repo: " + i[0] + " " + "Number of commits: " + str(i[1]))

# get_results("chinmliu")
