from flask import Flask, render_temp, flask, request, url_for, redirect
from cont_manag import Content

Topic_Dict = Content();
app = Flask(_name_)


# create route Site
@app.route('/site')
def site():
    #invoke the NCR API site when our visual image recognition successfully
    # detects a pattern or an object and then labels the site.  
    return 


# create route Item
@app.route('/item')
def item():
    #invoke the item list form API and meant to display current item that exists
    #in the store and a specific person's shopping history.
    return


# get route Itemlist
@app.route('/itemlist')
def itemList():
    #
    #
    return 

# get transcation
@app.route('/transcation')
def transcation():
    #The transaction process gets the info of the labeled site; 
    #meanwhile, this will implement the item-list route to compare to 
    #what items are being checked out now and the items we remind and recommend consumer to purchase. 
    
    return