#!/usr/bin/python3


import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value
    
opened_file = open('data/'+pageId, 'w') 
opened_file.write(description)
opened_file.close()
#permission error type = chmod 777 data

os.rename('data/'+pageId, 'data/'+title)

#redirection
print("Location: index.py?id="+title)
print()
