# Login Microservice

This is a simple Python/Flask login server using MongoDB. 

You will need to edit app.py to include your login uri (on line 7) for your Mongo DB. 

This app.py also assumes you have a DB and collection named 'users'. If you have named yours differently, you will need to edit. 

You start it by using the command

`python3 app.py`

This will start a server on port 9005.

You can then open another terminal window to run the sample test CURL script to register. 

There is also a sample test CURL script to login.

You may also create your own server (on a different port) to hit this server with a POST and the json needed. Sample json are included with required fields. 