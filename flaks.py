from flask import Flask, jsonify, request
import os
import json
import sys

def loadJson_it():
    with open('ithome.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_notice():
    with open('corona_notice.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_new():
    with open('corona_new.json','r',encoding = 'utf-8') as file:
        return json.load(file)


it_json = loadJson_it()
corona_notice_json = loadJson_notice()
corona_new_json = loadJson_new()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/ithome', methods = ['POST'])
def ithome():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if  content == u"학과 공지":
     response_data = {
         "version" : "2.0",
            "template" : {
             "outputs" : [
                 {
                        "simpleText" : {
                         "text" : "1. " + it_json[0]['title'] + "(" + it_json[0]['date'] + ")\n" + it_json[0]['url'] + "\n\n2. " + it_json[1]['title'] + "(" + it_json[1]['date'] + ")\n" + it_json[1]['url'] + "\n\n3. " + it_json[2]['title'] + "(" + it_json[2]['date'] + ")\n" + it_json[2]['url'] + "\n\n4. " + it_json[3]['title'] + "(" + it_json[3]['date'] + ")\n" + it_json[3]['url'] + "\n\n5. " + it_json[4]['title'] + "(" + it_json[4]['date'] + ")\n" + it_json[4]['url']
                            }
                        }
                    ]
                }
            }
    return jsonify(response_data)

@app.route('/corona', methods = ['POST'])
def corona():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if  content == u"코로나 공지":
        if len(corona_notice_json) > 5:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필수공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] + "\n\n4. " + corona_notice_json[3]['text'] + "(" + corona_notice_json[3]['date'] + ")\n" + corona_notice_json[3]['link'] + "\n\n5. " + corona_notice_json[4]['text'] + "(" + corona_notice_json[4]['date'] + ")\n" + corona_notice_json[4]['link']        
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 4:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필수공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] + "\n\n4. " + corona_notice_json[3]['text'] + "(" + corona_notice_json[3]['date'] + ")\n" + corona_notice_json[3]['link']      
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 3:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필수공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 2:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필수공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 1:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필수공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        else:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}]}}
    return jsonify(response_data)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080",debug=True)