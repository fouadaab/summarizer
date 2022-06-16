from flask import Flask, request, render_template, jsonify
from models.db_model import DBManipulation
from models.exceptions import KeyMissingError, ValueTypeError
from summarizer.sbert import SBertSummarizer
import nltk
from typing import Tuple
import enum

# Using an instance of SBERT to create the model
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

not_found = {'message': 'this id does not exist'}, 404

class SummaryParams(enum.IntEnum):
    MIN_LENGTH = 3
    SUMMARY_LENGTH = 2

def init_app(app: Flask):

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('index.html')


    @app.get('/texts')
    def read_texts():
  
        all_texts = DBManipulation.get_all_texts()

        json_return = all_texts or {'message': 'DB collection is empty'}

        return jsonify(json_return), 200


    @app.get('/text/<int:id>')
    def get_specific_text_by_id(id: int) -> Tuple:

        specific_text = DBManipulation.get_text_by_id(id)

        if not specific_text:

            return not_found

        return jsonify(specific_text), 200


    @app.post('/text')
    def create_text():

        try: 

            data = request.form['data']

            inserted_data = DBManipulation.save(data)

            return {'_id': inserted_data}, 201
        
        except KeyMissingError as error:

            return error.__dict__, 400

        except ValueTypeError as error:

            return error.__dict__, 400


    @app.delete('/text/<int:id>')
    def delete_text_by_id(id: int) -> Tuple:

        deleted_text = DBManipulation.delete_a_text(id) 

        if not deleted_text:

            return not_found

        return jsonify(deleted_text), 200 


    @app.route('/summarize/<int:id>', methods=["GET"])
    def summarize(id: int):
        
        record = DBManipulation.get_text_by_id(id)
        if not record:
            return not_found
        
        text = record['text']
        sent = nltk.sent_tokenize(text)
        
        if len(sent) < SummaryParams.MIN_LENGTH:
            summary =  "Please insert a minimum of 3 sentences in the text area."
        else:
            summary = model(text, num_sentences=SummaryParams.SUMMARY_LENGTH)
        
        return render_template('summary.html',result=summary)