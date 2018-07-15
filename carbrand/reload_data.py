# -*-coding:utf-8-*-

# Create your models here.
import json
import os
import MySQLdb


def save_carbrand_data():
    db = MySQLdb.connect("localhost", "root", "passw0rd", "carbrand", charset='utf8')
    cursor = db.cursor()
    with open('../car_new_01.json', 'r') as file:
        list_car = json.load(file)
        for car in list_car:
            #print car['name_cn']
            #print car
            #print type(str(list_car[0]['name_cn']))
            name_cn = car['name_cn'].encode('utf-8')
            img = car['img'].encode('utf-8')
            carbrand_id = car['carbrand_id']
            introduction = car['introduction'].encode('utf-8')
            if "'" in introduction:
                print introduction
                intr = introduction.replace("'", "\\\'")
            ranking = car['ranking']
            if len(str(carbrand_id)) == 6:
                country_id = int(str(carbrand_id)[0:4])
            else:
                country_id = int(str(carbrand_id)[0:5])
            sql = "INSERT INTO carbrand_carbrand(NAME_CN, IMG, CARBRAND_ID, " \
                  "RANKING, COUNTRY_ID, INTRODUCTION) VALUES ('%s','%s','%d','%d','%d','%s') " \
                  % (name_cn, img, carbrand_id, ranking, country_id, intr)
            print sql
            try:
                cursor.execute(sql)
                db.commit()
                print "insert success"
            except Exception:
                db.rollback()
                print "insert failed"


def save_country_data():
    db = MySQLdb.connect("localhost", "root", "passw0rd", "carbrand", charset='utf8')
    cursor = db.cursor()
    with open('../car_country.json', 'r') as file:
        list_country = json.load(file)
        for country in list_country:
            print country['country_name_cn']
            country_name_cn = country['country_name_cn'].encode('utf-8')
            country_id = country['country_id']
            sql = "INSERT INTO carbrand_country(COUNTRY_ID, COUNTRY_NAME_CN) VALUES ('%d','%s') " \
                  % (country_id, country_name_cn)
            print sql
            try:
                cursor.execute(sql)
                print "insert success"
                db.commit()
            except Exception:
                db.rollback()
                print "insert failed"


save_carbrand_data()
#save_country_data()
