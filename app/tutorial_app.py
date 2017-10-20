from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('basic.html')


@app.route("/get_data/", methods=['POST'])
def get_data():
	my_list = ['a', 'b', 'c', 'd', 'e']

	return jsonify({'data': render_template('response.html', my_list=my_list)})



if __name__ == '__main__':
	app.run(debug=True)