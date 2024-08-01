from flask import request, jsonify

from app import app, db
from app.models import data


@app.route('/login', methods=['POST'])
def login():
    rdata = request.json
    username = rdata.get('username')
    password = rdata.get('password')
    print(f"Username: {username}")
    print(f"Password: {password}")
    
    try:
        add = data(username=username, password=password)
        db.session.add(add)
        db.session.commit()
        print(add)
    except:
        db.session.rollback()
        print("err")

    # Di sini, Anda bisa menambahkan logika untuk memeriksa username dan password
    # Contoh sederhana untuk tujuan ilustrasi:
    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/api/get", methods=["GET","POST"])
def ambil():
    dataHasil = data.query.all()
    data_dict = [ini.data_dict() for ini in dataHasil]
    return jsonify(data_dict)
