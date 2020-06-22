from flask import Flask, session
# session enables us to add a piece of identification data to...
# browser using cookie and linking this to a piece of...
# identification data to a web server aka session ID...
# these two piece of data are stored in a dictionary called session.

from checker import check_logged_in
# module that we created with the checked_logged_in decorator

app =  Flask(__name__)
# create a new flask web app.

app.secret_key = 'supersecretkey'
# flask uses a string to encrypt your cookie prior...
# to transmitting to your browser.

@app.route('/login')
def do_login():
    session['logged_in'] = True
    # we are setting the session's dictionary key which is 'logged_in' to True
    return "You are now logged IN."
    # return a message to confirm we're logged IN.

@app.route('/logout')
def do_logout():
    del session['logged_in']
    # the recommended way of logging out is removing the key instead of ...
    # just setting the key to True.
    return 'You are now logged OUT'
    # return a message to confirm we're logged OUT.

@app.route('/')
def hello(): # Let's set a welcome message to our homepage!
  return """Hello from Flask! Here we are testing the logging in
            and logging out and user restriction functionality
            using Flask's session!"""

@app.route('/page11')
@check_logged_in # check if user is logged in using our created checker module
def page11():
  return 'You are viewing page11!'

@app.route('/page12')
@check_logged_in # check if user is logged in using our created checker module
def page12():
  return 'You are viewing page12!'

@app.route('/page13')
@check_logged_in # check if user is logged in using our created checker module
def page13():
  return 'You are viewing page13!'

if __name__ == '__main__':
    app.run(debug=True)
