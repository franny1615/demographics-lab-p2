from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

def get_state_options():
    state = counties[0]["State"]
    op = ""
    for c in counties:
        if state != c["State"]:
            op += Markup("<option value=" + state +">" + state + "</option>")
            state = c["State"]
    return op

def get_fact(state):
    funfact = ""
    for c in counties:
        if state == c["State"]:
            fact += c["Age"]["Percent Under 18 Years"]
            funfact += Markup("<p>" + str(fact) + "</p>")
    return funfact

@app.route("/")
def render_main():
    get_state_options()
    return render_template('home.html', option = get_state_options())
 
@app.route("/app", methods=['GET','POST'])
def render_fact():
    get_state_options()
    place = request.args['data']
    return render_template('home.html', fact = get_fact(place))
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
