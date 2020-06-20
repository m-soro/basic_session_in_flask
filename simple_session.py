from flask import Flask, session
# session enables us to add a piece of identification data to...
# browser using cookie and linking this to a piece of...
# identification data to a web server aka session ID...
# these two piece of data are stored in a dictionary called session.

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

@app.route('/status')
def check_status():
    # if session['logged_in']: -> do not use. susceptiple to key error..
    if 'logged_in' in session: # this way of checking prevents the code from crashing!
        return 'You are currently logged in'
    return 'You are currently logged out'
    # return message to confirm status.

@app.route('/')
def hello():
  return """Hello from Flask! Here we are testing the logging in
            and logging out functionality using Flask's session!"""

@app.route('/page11')
def page11():
  return 'This is page11!'

@app.route('/page12')
def page12():
  return 'This is page12!'

@app.route('/page13')
def page13():
  return 'This is page13!'

if __name__ == '__main__':
    app.run(debug=True)
