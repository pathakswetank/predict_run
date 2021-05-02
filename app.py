from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Individual_Run.html')
    
@app.route('/player_names', methods=['GET'])
def player_names():
    response = jsonify({
        'PLAYER': util.player_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_run', methods=['GET', 'POST'])
def predict_run():
    
    PLAYER = request.form['PLAYER']
    Avg = float(request.form['Avg'])
    BF = int(request.form['BF'])
    SR = float(request.form['SR'])
    Fours = int(request.form['Fours'])
    Six = int(request.form['Six'])

    response = {
        'estimated_run': util.estimated_run(PLAYER, Avg, BF, SR,Fours, Six)
    }
    #response.headers.add('Access-Control-Allow-Origin', '*')

    #return response
    return render_template("result.html", response = response)
        

if __name__ == "__main__":
    print("Starting Python Flask Server For Run Prediction...")
    util.load_saved_artifacts()
    app.run()