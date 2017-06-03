from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/users', methods=['GET','POST','DELETE'])
def get_user():
	if request.method=="GET":

		return json.dumps(['user1','user2','user3'])
	if request.method=="POST":
		print "got the post request"
		data = request.json

		return ""


if __name__ == "__main__":
	app.run(debug=True)