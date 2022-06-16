# Text Summarizer
Store Text Data in MongoDB (NoSQL) And Summarizes On Demand

To run the app from the root folder (path_to_root_folder/.): <br>
$ export FLASK_APP=api <br>
$ flask run <br>
(open link, dev should be running on http://127.0.0.1:5000 by default) <br>

Run unit test (test sample): <br>
$ python -m unittest discover -p testing.py <br>
<br>
MongoDB pre-configured: (For storage and collection of texts)
- Running on localhost, listening port 27017
- DB name: squirro
- Collection: texts
