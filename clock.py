from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route('/data/now')
def nowtime():
    date_time = datetime.datetime.now()
    json_data = {}
    json_data['date'] = date_time.strftime('%Y-%m-%d')
    json_data['week'] = date_time.strftime('%a')
    json_data['time'] = date_time.strftime('%H:%M:%S')
    json_data['micro_sec'] = date_time.strftime('%f')
    return jsonify(json_data)


@app.route('/')
def index():
    html_page = '''<!DOCTYPE html>
    <html lang="ja">
    <head>
        <title>flask + ajax sample</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <h1>現在時刻</h1>
        <div>
            <h2>Server Time [python3 + flask + jQuery.ajax]</h2>
            <p id="flask_time"></p>
            <p><a href="/data/now">Data ( json )</a></p>
            <script>
                 $(function(){
                     setInterval(function(){
                         $.ajax({
                             type:'GET',
                             url:'/data/now',
                             dataType: 'json',
                             success: function(json){
                                 $('#flask_time').html( json.date +"("+ json.week + ") "
                                                        + json.time + " " + json.micro_sec );
                             }
                         });
                     }, 1000);
                 });
            </script>
        </div>
    </body>
    </html>
'''
    return html_page


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
