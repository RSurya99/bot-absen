from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import datetime
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy

DOWNLOAD_DIRECTORY = '/https://8f22ea76d9c4.ngrok.io/bot'
app = Flask(__name__)
app.secret_key = "Secret Key"

DB_USER = "root"
DB_PASS = ""
DB_HOST = "localhost"
DATABASE = "absensi_rpl"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DATABASE)    #"mysql+pymysql://root:NO@localhost/flask_crud"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class absensi_xiirpl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.String(225))
    nama = db.Column(db.String(225))
    jam_absen = db.Column(db.String(225))
    keterangan = db.Column(db.String(225))

    def __init__(self, tanggal, nama, jam_absen, keterangan):
        self.tanggal = tanggal
        self.nama = nama
        self.jam_absen = jam_absen
        self.keterangan = keterangan


@app.route('/bot', methods=['GET','POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '/absen' in incoming_msg:
        inc_msg = incoming_msg.split()
        name = inc_msg[-2]
        ket = inc_msg[-1]

        current_data = datetime.datetime.now()

        current_time = [current_data.hour, current_data.minute, current_data.second]
        current_time = list(map(str, current_time))

        current_date = datetime.datetime.today().strftime('%Y-%m-%d')
        current_time = ':'.join(current_time)

        my_data = absensi_xiirpl(current_date,name,current_time,ket)
        db.session.add(my_data)
        db.session.commit()
        
        msg.body('Absen Berhasil')
        responded = True
    if not responded:
        msg.body('Maaf perintah yang anda masukkan salah / tidak ada')
    return str(resp)

@app.route('/')
def index():
    return "fathur nanti masukkin datanya disini ya"

if __name__ == '__main__':
    app.run(debug=True)