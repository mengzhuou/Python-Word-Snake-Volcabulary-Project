# issues:
# 1. Timer won't stop whole function after time ends
# 2. 


import mysql.connector
from mysql.connector import Error
import time
import _thread

# import numpy as np
import random
import string

import re

def countdown(t, endSentence):
    while t:
        time.sleep(1)
        t -= 1
    isCountingDown = False
    print(endSentence)
    cursor.close()
    connection.commit()
    connection.close()



try:
    connection = mysql.connector.connect(host='localhost',
                                        database='entries', #entries is the database name
                                        user='root',
                                        password='ou1106983163')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        # print("Connected to MySQL Workbench Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        # print("You're connected to database: ", record)
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")
        with connection.cursor() as cursor:

            alphabet = random.choice(string.ascii_letters)

            word = []

            i = 1
            # define the countdown func.
            isCountingDown = True

                
            while (isCountingDown):
                
                _thread.start_new_thread(countdown, (10, "\nGame is over", ))

                if (i-1 == 0): 
                    preword = alphabet
                    print("     Round ", i)
                    print("     Previous word: " + preword + ".")
                
                else:
                    preword = word[len(word)-1]
                    print("     Round ", i)
                    print("     Previous word: " + word[i-2] + ".")
                
                temp = (input("Please continue (start with " + preword[-1] + "): "))
                # while (re.search(r"(^[a-z]+^[A-Z]+)"), temp):
                #     print("     Special character(s) or number(s) are not accepted.")
                #     temp = input("Please continue (start with " + preword[-1] + "): ")


                # Need this ',' to end the query? dummo why but its important
                    
                # print(cursor.statement)
                cursor.execute("select definition from entries where word = %s", (temp,))
                records = cursor.fetchall()
                while (not records):
                    print("Couldn't find an existing word! Please re-enter your input: ")
                    temp = (input("Please continue (start with " + preword[-1] + "): "))
                    cursor.execute("select definition from entries where word = %s", (temp,)) 
                    records = cursor.fetchall()

                for record in records:
                    print(record)
                
                word.append(temp)

                print(word)
                i+=1
                time.sleep(0.1)

except:
    pass