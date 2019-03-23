#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_html import HTMLSession

def main():
    session = HTMLSession()
    r = session.get("https://www.keishicho.metro.tokyo.jp/jiken_jiko/hassei/jiko.html")

    about = r.html.find('.t-box2', first=True)
    rows = about.text.split("\n")
    print(rows[0])
    for index in range(len(rows)):
        if rows[index] == "発生件数":
            print(rows[index] + ": " + rows[index + 1])
        if rows[index] == "死者数":
            print(rows[index] + ": " + rows[index + 1])
        if rows[index] == "負傷者数":
            print(rows[index] + ": " + rows[index + 1])

    sel = "#main > div > p:nth-child(5)"
    about = r.html.find(sel, first=True)
    print(about.text)

    sel = "#main > div > p:nth-child(7)"
    about = r.html.find(sel, first=True)
    print(about.text)
    

if __name__ == '__main__':
    main()
    