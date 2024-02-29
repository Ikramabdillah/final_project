import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_paginate import Pagination, get_page_args
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timezone, date
from helpers import login_required
import math

# Configure application
app = Flask(__name__, static_url_path='/static')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Configure upload Folder
app.config["UPLOAD_FOLDER"] = "static/praktik"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///simgmpinformatika.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/akun", methods=["GET", "POST"])
@login_required
def akun():
    if request.method == "POST":
        id_user = request.form.get("id")
        nama = request.form.get("editnama")
        nip = request.form.get("editnip")
        nik = request.form.get("editnik")
        tempat_lahir = request.form.get("edittempat_lahir")
        alamat = request.form.get("editalamat")
        tanggal_lahir = request.form.get("edittanggal_lahir")
        nomor_hp = request.form.get("editnomor_hp")
        nuptk = request.form.get("editnuptk")
        jenis_kelamin = request.form.get("editjenis_kelamin")
        gol_jab = request.form.get("editgol_jab")
        email_pribadi = request.form.get("editemail_pribadi")
        email_pmm = request.form.get("editemail_pmm")
        pendidikan_terakhir = request.form.get("editpendidikan_terakhir")
        jenis_kepegawaian = request.form.get("editjenis_kepegawaian")
        sekolah = request.form.get("editsekolah")

        db.execute("UPDATE data_akun set nama = ?, nip = ?, nik = ?, tempat_lahir = ?, alamat = ?, tanggal_lahir = ?, nomor_hp = ?, nuptk = ?, jenis_kelamin = ?, gol_jab = ?, email_pribadi = ?, email_pmm = ?, pendidikan_terakhir = ?, jenis_kepegawaian = ?, sekolah = ? WHERE id = ?", nama, nip, nik, tempat_lahir, alamat, tanggal_lahir, nomor_hp, nuptk, jenis_kelamin, gol_jab, email_pribadi, email_pmm, pendidikan_terakhir, jenis_kepegawaian, sekolah, id_user)

        flash(f"Data berhasil diperbaharui", "success")
        return redirect("/akun")
    else:
        rows = db.execute("SELECT * FROM data_akun WHERE id = ?", session["user_id"])

        for row in rows:
            row_sekolah = db.execute("SELECT * FROM data_sekolah WHERE id = ?", row['sekolah'])
            row['nama_sekolah'] = row_sekolah[0]['nama_sekolah']
            row['alamat_sekolah'] = row_sekolah[0]['alamat_sekolah']
            row['npsn'] = row_sekolah[0]['npsn']
            row['kecamatan'] = row_sekolah[0]['kecamatan']
            row['kab_kota'] = row_sekolah[0]['kab_kota']
            row['kepsek'] = row_sekolah[0]['kepsek']

            try:
                row_kepsek = db.execute("SELECT nama_kepsek FROM data_kepsek WHERE id = ?", row['kepsek'])[0]['nama_kepsek']
                row['nama_kepsek'] = row_kepsek

            except:
                row['nama_kepsek'] = "Nama Kepala Sekolah Belum Diinput"

            if row['jenis_kelamin'] == "Laki-laki":
                row['foto_profil'] = "user-03.jpg"
            else:
                row['foto_profil'] = "woman.jpg"

            row['tanggal_b'] = datetime.strptime(row['tanggal_lahir'], '%Y-%m-%d').date()

            row['tanggal'] = row['tanggal_b'].day
            row['tahun'] = row['tanggal_b'].year
            row['bulan_a'] = row['tanggal_b'].month

            if row['bulan_a'] == 1:
                row['bulan'] = "Januari"
            elif row['bulan_a'] == 2:
                row['bulan'] = "Februari"
            elif row['bulan_a'] == 3:
                row['bulan'] = "Maret"
            elif row['bulan_a'] == 4:
                row['bulan'] = "April"
            elif row['bulan_a'] == 5:
                row['bulan'] = "Mei"
            elif row['bulan_a'] == 6:
                row['bulan'] = "Juni"
            elif row['bulan_a'] == 7:
                row['bulan'] = "Juli"
            elif row['bulan_a'] == 8:
                row['bulan'] = "Agustus"
            elif row['bulan_a'] == 9:
                row['bulan'] = "September"
            elif row['bulan_a'] == 10:
                row['bulan'] = "Oktober"
            elif row['bulan_a'] == 11:
                row['bulan'] = "November"
            elif row['bulan_a'] == 12:
                row['bulan'] = "Desember"

        schools = db.execute("SELECT * FROM data_sekolah")

        return render_template("akun.html", rows=rows, schools=schools)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    """Show portfolio of stocks"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            flash("Masukkan Username Anda!", "danger")
            return redirect("/")
        if not password:
            flash("Masukkan Kata Sandi Anda!", "danger")
            return redirect("/")

        query = db.execute("SELECT * FROM akun_login WHERE username = ? AND password = ?", username, password)

        if len(query) < 1:
            flash (f"Akun Belum terdaftar. Silahkan melakukan registrasi akun terlebih dahulu!", "danger")
            return redirect("/")

        if query[0]['jenis_akun'] == "nonaktif":
            flash (f"Akun Belum dikonfirmasi Admin. Hubungi Admin MGMP!", "danger")
            return redirect("/")

        if len(query) > 0:

            session['user_id'] = query[0]['id_user']
            session['jenis_akun'] = query[0]['jenis_akun']

            if session['jenis_akun'] == "admin":
                session['admin'] = True
                flash(f"Berhasil Masuk Akun sebagai Admin", "success")
                return redirect("/akun")

            flash(f"Berhasil Masuk Akun", "success")
            return redirect("/akun")
        else:
            flash(f"Username atau Password Salah!", "danger")
            return redirect("/")
    else:

        rows = db.execute("SELECT * FROM pertemuan")

        for row in rows:
            row['sekolah'] = db.execute("SELECT nama_sekolah FROM data_sekolah WHERE id = ?", row['lokasi'])[0]['nama_sekolah']

            row['tanggal_a'] = datetime.strptime(row['tanggal'], '%Y-%m-%d').date().weekday()
            row['tanggal_b'] = datetime.strptime(row['tanggal'], '%Y-%m-%d').date()

            if row['tanggal_a'] == 0:
                row['hari'] = "Senin";
            elif row['tanggal_a'] == 1:
                row['hari'] = "Selasa";
            elif row['tanggal_a'] == 2:
                row['hari'] = "Rabu";
            elif row['tanggal_a'] == 3:
                row['hari'] = "Kamis";
            elif row['tanggal_a'] == 4:
                row['hari'] = "Jumat";
            elif row['tanggal_a'] == 5:
                row['hari'] = "Sabtu";
            elif row['tanggal_a'] == 6:
                row['hari'] = "Minggu";

            row['tanggal'] = row['tanggal_b'].day
            row['tahun'] = row['tanggal_b'].year
            row['bulan_a'] = row['tanggal_b'].month

            if row['bulan_a'] == 1:
                row['bulan'] = "Januari"
            elif row['bulan_a'] == 2:
                row['bulan'] = "Februari"
            elif row['bulan_a'] == 3:
                row['bulan'] = "Maret"
            elif row['bulan_a'] == 4:
                row['bulan'] = "April"
            elif row['bulan_a'] == 5:
                row['bulan'] = "Mei"
            elif row['bulan_a'] == 6:
                row['bulan'] = "Juni"
            elif row['bulan_a'] == 7:
                row['bulan'] = "Juli"
            elif row['bulan_a'] == 8:
                row['bulan'] = "Agustus"
            elif row['bulan_a'] == 9:
                row['bulan'] = "September"
            elif row['bulan_a'] == 10:
                row['bulan'] = "Oktober"
            elif row['bulan_a'] == 11:
                row['bulan'] = "November"
            elif row['bulan_a'] == 12:
                row['bulan'] = "Desember"

        schools = db.execute("SELECT * FROM data_sekolah")

        members = db.execute("SELECT * FROM pengurus")

        for member in members:
            member_sekolah = db.execute("SELECT * FROM data_sekolah WHERE id = ?", member['asal_sekolah'])
            member['nama_sekolah'] = member_sekolah[0]['nama_sekolah']

        return render_template("index.html", rows=rows, schools=schools, members=members)


@app.route("/register", methods = ["GET", "POST"])
def register():
    username = request.form.get("usernameReg")
    password = request.form.get("passwordReg")
    nama = request.form.get("nameReg")
    jenis_kelamin = request.form.get("jenis_kelaminReg")
    email = request.form.get("emailReg")
    sekolah = request.form.get("sekolahReg")

    if ' ' in username:
            flash(f"Username tidak boleh menggunakan spasi!", "danger")
            return redirect("/")

    length = digit = huruf = False

    if len(password) < 8:
        flash(f"Password minimal 8 karakter kombinasi huruf dan angka", "danger")
        return redirect("/")

    elif len(password) >= 8:
        length = True

        for letter in password:
            if letter.isdigit():
                digit = True
            if letter.isalpha():
                huruf = True

    username_check = db.execute ("SELECT * FROM akun_login WHERE username = ?", username)

    if len(username_check) > 0:
        flash(f'Username <b>' + username + '</b> telah terdaftar. Coba username lainnya!', "danger")
        return redirect("/")

    if digit and huruf and length:
        db.execute("INSERT INTO akun_login (username, email, password, id_user, jenis_akun) VALUES (?, ?, ?, (SELECT MAX(id) + 1 FROM akun_login ), 'nonaktif')", username, email, password)

        db.execute("INSERT INTO data_akun (id, nama, nip, alamat, nomor_hp, email_pribadi, email_pmm, pendidikan_terakhir, tempat_lahir, tanggal_lahir, jenis_kepegawaian, nik, nuptk, sekolah, jenis_kelamin, gol_jab) VALUES ((SELECT MAX(id) FROM akun_login), ?, 0, 'Belum diisi', 0, 'Belum diisi', ?, 'Belum diisi', 'Belum diisi', '1901-01-01', 'Belum diisi', 0, 0, ?, ?, 'Belum diisi')", nama, email, sekolah, jenis_kelamin)

        flash (f"Daftar Akun berhasil! Tunggu hingga Admin mengkonfirmasi akun Anda.", "success")
        return redirect("/")

    else:
        flash(f"Password minimal 8 karakter kombinasi huruf dan angka", "danger")
        return redirect("/")


@app.route("/konfirmasi", methods = ["GET", "POST"])
def konfirmasi():
    if request.method == "POST":
        id_user = request.form.get("id")

        if request.form['action'] == "Aktifkan":

            db.execute("UPDATE akun_login SET jenis_akun = 'guru' WHERE id_user = ?", id_user)

            flash(f"Akun telah diaktifkan", "success")
            return redirect("/konfirmasi")

        elif request.form['action'] == "Nonaktifkan":
            db.execute("UPDATE akun_login SET jenis_akun = 'nonaktif' WHERE id_user = ?", id_user)

            flash(f"Akun telah dinonaktifkan", "danger")
            return redirect("/konfirmasi")
    else:
        rows = db.execute("SELECT * FROM akun_login ORDER BY jenis_akun DESC")
        for row in rows:
            row['nama'] = db.execute("SELECT nama FROM data_akun WHERE id = ?", row['id_user'])[0]['nama']
            row['nama_sekolah'] = db.execute("SELECT nama_sekolah FROM data_sekolah WHERE id = (SELECT sekolah FROM data_akun WHERE id = ?)", row['id_user'])[0]['nama_sekolah']
            if row['jenis_akun'] == "nonaktif":
                row['status'] = "Tidak Aktif"
            else:
                row['status'] = "Aktif"

        page = request.args.get('page', 1, type=int)
        per_page = 5
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = (len(row) + (per_page - 1))
        data = math.ceil(len(rows) / per_page)

        item_on_page = rows[start:end]

        return render_template("konfirmasi.html", rows=item_on_page, total_pages=total_pages, data=data, page=page)

@app.route("/jadwal", methods = ["GET", "POST"])
def jadwal():
    if request.method == "POST":
        id_pertemuan = request.form.get("id_pertemuan")
        tanggal = request.form.get("tanggalEdit")
        lokasi = request.form.get("lokasiEdit")
        link = request.form.get("linkEdit")

        try:
            db.execute("UPDATE pertemuan set tanggal = ?, lokasi = ?, link = ? WHERE id = ?", tanggal, lokasi, link, id_pertemuan)

            flash(f"Data pertemuan berhasil diubah!", "success")
            return redirect("/jadwal")

        except:

            flash(f"Data pertemuan gagal diubah!", "danger")
            return redirect("/jadwal")
    else:
        rows = db.execute("SELECT * FROM pertemuan")

        for row in rows:
            row['sekolah'] = db.execute("SELECT nama_sekolah FROM data_sekolah WHERE id = ?", row['lokasi'])[0]['nama_sekolah']

            row['tanggal_a'] = datetime.strptime(row['tanggal'], '%Y-%m-%d').date().weekday()
            row['tanggal_b'] = datetime.strptime(row['tanggal'], '%Y-%m-%d').date()

            if row['tanggal_a'] == 0:
                row['hari'] = "Senin";
            elif row['tanggal_a'] == 1:
                row['hari'] = "Selasa";
            elif row['tanggal_a'] == 2:
                row['hari'] = "Rabu";
            elif row['tanggal_a'] == 3:
                row['hari'] = "Kamis";
            elif row['tanggal_a'] == 4:
                row['hari'] = "Jumat";
            elif row['tanggal_a'] == 5:
                row['hari'] = "Sabtu";
            elif row['tanggal_a'] == 6:
                row['hari'] = "Minggu";

            row['tanggal'] = row['tanggal_b'].day
            row['tahun'] = row['tanggal_b'].year
            row['bulan_a'] = row['tanggal_b'].month

            if row['bulan_a'] == 1:
                row['bulan'] = "Januari"
            elif row['bulan_a'] == 2:
                row['bulan'] = "Februari"
            elif row['bulan_a'] == 3:
                row['bulan'] = "Maret"
            elif row['bulan_a'] == 4:
                row['bulan'] = "April"
            elif row['bulan_a'] == 5:
                row['bulan'] = "Mei"
            elif row['bulan_a'] == 6:
                row['bulan'] = "Juni"
            elif row['bulan_a'] == 7:
                row['bulan'] = "Juli"
            elif row['bulan_a'] == 8:
                row['bulan'] = "Agustus"
            elif row['bulan_a'] == 9:
                row['bulan'] = "September"
            elif row['bulan_a'] == 10:
                row['bulan'] = "Oktober"
            elif row['bulan_a'] == 11:
                row['bulan'] = "November"
            elif row['bulan_a'] == 12:
                row['bulan'] = "Desember"

        schools = db.execute("SELECT * FROM data_sekolah")

        return render_template("/jadwal.html", rows=rows, schools=schools)

@app.route("/setting", methods = ["GET", "POST"])
def setting():
    if request.method == "POST":
        username = request.form.get("usernameEdit")
        password = request.form.get("passwordEdit")
        confirmation = request.form.get("confirmation")

        if ' ' in username:
            flash(f"Username tidak boleh menggunakan spasi!", "danger")
            return redirect("/setting")

        if password != confirmation:
            flash(f"Password tidak sesuai!", "danger")
            return redirect("/setting")

        length = digit = huruf = False

        if len(password) < 8:
            flash(f"Password minimal 8 karakter kombinasi huruf dan angka", "danger")
            return redirect("/setting")

        elif len(password) >= 8:
            length = True

            for letter in password:
                if letter.isdigit():
                    digit = True
                if letter.isalpha():
                    huruf = True

        if length and digit and huruf:
            db.execute("UPDATE akun_login set username = ?, password = ? WHERE id_user = ?", username, password, session["user_id"])

            flash("Data berhasil diperbarui!", "success")
            return redirect("/setting")
        else:

            flash(f"Password minimal 8 karakter kombinasi huruf dan angka", "danger")
            return redirect("/setting")

    else:
        rows = db.execute("SELECT * FROM akun_login WHERE id_user = ?", session["user_id"])

        return render_template("setting.html", rows=rows)

@app.route("/pengurus", methods = ["GET", "POST"])
def pengurus():
    if request.method == "POST":
        id_pengurus = request.form.get("id_pengurus")
        nama = request.form.get("namaEdit")
        sekolah = request.form.get("sekolahEdit")
        jenis_kelamin = request.form.get("jkEdit")

        try:
            db.execute("UPDATE pengurus set nama = ?, asal_sekolah = ?, jenis_kelamin = ? WHERE id = ?", nama, sekolah, jenis_kelamin, id_pengurus)

            flash(f"Data pengurus berhasil diubah!", "success")
            return redirect("/pengurus")
        except:
            flash(f"Data pengurus gagal diubah!", "danger")
            return redirect("/pengurus")
    else:
        members = db.execute("SELECT * FROM pengurus")

        for member in members:
            member_sekolah = db.execute("SELECT * FROM data_sekolah WHERE id = ?", member['asal_sekolah'])
            member['nama_sekolah'] = member_sekolah[0]['nama_sekolah']

        schools = db.execute("SELECT * FROM data_sekolah")

        return render_template("pengurus.html", members=members, schools=schools)

@app.route("/sekolah", methods = ["GET", "POST"])
def sekolah():
    if request.method == "POST":
        if request.form['action'] == "simpan":

            id_sekolah = request.form.get("id_sekolah")
            nama_sekolah = request.form.get("namaSekolah")
            alamat_sekolah = request.form.get("alamatSekolah")
            npsn = request.form.get("npsnSekolah")
            kecamatan = request.form.get("kecamatanSekolah")
            kab_kota = request.form.get("kab_kotSekolah")
            kepsek = request.form.get("kepsekSekolah")

            try:
                db.execute("UPDATE data_sekolah SET nama_sekolah = ?, alamat_sekolah = ?, npsn = ?, kecamatan = ?, kab_kota = ?, kepsek = ? WHERE id = ?", nama_sekolah, alamat_sekolah, npsn, kecamatan, kab_kota, kepsek, id_sekolah)

                flash(f"Data sekolah berhasil diperbarui!", "success")
                return redirect("/sekolah")
            except:
                flash(f"Data sekolah gagal diperbarui!", "danger")
                return redirect("/sekolah")
        elif request.form['action'] == "tambah":
            nama_sekolah = request.form.get("namaTambahSekolah")
            alamat_sekolah = request.form.get("alamatTambahSekolah")
            npsn = request.form.get("npsnTambahSekolah")
            kecamatan = request.form.get("kecamatanTambahSekolah")
            kab_kota = request.form.get("kab_kotTambahSekolah")
            kepsek = request.form.get("kepsekTambahSekolah")

            try:
                db.execute("INSERT INTO data_sekolah (id, nama_sekolah, alamat_sekolah, npsn, kecamatan, kab_kota, kepsek) VALUES ((SELECT MAX(id) + 1 FROM data_sekolah), ?, ?, ?, ?, ?, ?)", nama_sekolah, alamat_sekolah, npsn, kecamatan, kab_kota, kepsek)

                flash(f"Data sekolah berhasil ditambahkan!", "success")
                return redirect("/sekolah")
            except:
                flash(f"Data sekolah gagal ditambahkan!", "danger")
                return redirect("/sekolah")
        elif request.form['action'] == "Hapus":
            id_sekolah = request.form.get('idHapus')

            try:
                db.execute("DELETE FROM data_sekolah WHERE id = ?", id_sekolah)

                flash(f"Data sekolah berhasil dihapus!", "success")
                return redirect("/sekolah")
            except:
                flash(f"Data sekolah gagal dihapus!", "danger")
                return redirect("/sekolah")

    else:
        rows = db.execute("SELECT * FROM data_sekolah")

        for row in rows:
            try:
                row['nama_kepsek'] = db.execute("SELECT nama_kepsek FROM data_kepsek WHERE id = ?", row['kepsek'])[0]['nama_kepsek']
            except:
                row['nama_kepsek'] = "Data Kepala Sekolah belum diinput"

        page = request.args.get('page', 1, type=int)
        per_page = 5
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = (len(row) + (per_page - 1))
        data = math.ceil(len(rows) / per_page)

        item_on_page = rows[start:end]

        kepseks = db.execute("SELECT * FROM data_kepsek")

        return render_template("sekolah.html", rows=item_on_page, total_pages=total_pages, page=page, data=data, kepseks=kepseks)


@app.route("/cari_praktik", methods = ["GET", "POST"])
def cari_praktik():
    if request.method == "POST":
        cari = request.form.get("caripraktik")

        if not cari:
            return redirect("/#praktikbaik")

        cari_split = cari.split()
        cari_count = len(cari_split)
        start = 0
        quote = ""

        for row in cari_split:
            quote += (f"judul_praktik LIKE '%" + row + "%' OR deskripsi LIKE '%" + row + "%' OR tingkatan LIKE '%" + row + "%'")
            if start != (cari_count - 1):
                quote += " OR "
            start += 1

        rows = db.execute(f"SELECT * FROM praktik_baik WHERE {quote}")

        for row in rows:
            row['nama_user'] = db.execute("SELECT nama FROM data_akun WHERE id = ?", row['id_user'])[0]['nama']
            row['deskripsi_str'] = db.execute("SELECT SUBSTR(deskripsi, 1, 110) as deskripsi FROM praktik_baik WHERE id = ?", row['id'])[0]['deskripsi']

            if row['tipe_file'] == "pdf":
                file_path = f"static/praktik/{row['nama_file']}"
                row['size_file'] = f"{get_size(file_path, 'kb')} KB"
            else:
                row['size_file'] = "Video YouTube"

            row['tanggalpraktik'] = datetime.strptime(row['tanggal_praktik'], '%Y-%m-%d').date()

            row['tanggal'] = row['tanggalpraktik'].day
            row['tahun'] = row['tanggalpraktik'].year
            row['bulan_a'] = row['tanggalpraktik'].month

            if row['bulan_a'] == 1:
                row['bulan'] = "Januari"
            elif row['bulan_a'] == 2:
                row['bulan'] = "Februari"
            elif row['bulan_a'] == 3:
                row['bulan'] = "Maret"
            elif row['bulan_a'] == 4:
                row['bulan'] = "April"
            elif row['bulan_a'] == 5:
                row['bulan'] = "Mei"
            elif row['bulan_a'] == 6:
                row['bulan'] = "Juni"
            elif row['bulan_a'] == 7:
                row['bulan'] = "Juli"
            elif row['bulan_a'] == 8:
                row['bulan'] = "Agustus"
            elif row['bulan_a'] == 9:
                row['bulan'] = "September"
            elif row['bulan_a'] == 10:
                row['bulan'] = "Oktober"
            elif row['bulan_a'] == 11:
                row['bulan'] = "November"
            elif row['bulan_a'] == 12:
                row['bulan'] = "Desember"

            row['tanggal'] = f"{row['tanggal']} {row['bulan']} {row['tahun']}"

        if len(rows) > 0:
            page = request.args.get('page', 1, type=int)
            per_page = 9
            start = (page - 1) * per_page
            end = start + per_page
            total_pages = (len(rows) + (per_page - 1))
            data = math.ceil(len(rows) / per_page)
            hasil = len(rows)

            item_on_page = rows[start:end]


            return render_template("cari_praktik.html", cari=cari, hasil=hasil, rows=item_on_page, page=page, total_pages=total_pages, data=data)
        else:
            return render_template("cari_praktik.html", cari=cari, hasil=len(rows))

    else:

        return render_template("cari_praktik.html")

def get_size(file_path, unit='bytes'):
    file_size = os.path.getsize(file_path)
    exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
    if unit not in exponents_map:
        raise ValueError("Must select from \
        ['bytes', 'kb', 'mb', 'gb']")
    else:
        size = file_size / 1024 ** exponents_map[unit]
        return round(size, 3)

@app.route("/kepsek", methods = ["GET", "POST"])
def kepsek():
    if request.method == "POST":
        if request.form['action'] == "simpan":

            id_kepsek = request.form.get("id_kepsek")
            nama_kepsek = request.form.get("namaEditKepsek")
            nip_kepsek = request.form.get("nipEditKepsek")

            try:
                db.execute("UPDATE data_kepsek SET nama_kepsek = ?, nip_kepsek = ? WHERE id = ?", nama_kepsek, nip_kepsek, id_kepsek)

                flash(f"Data Kepala sekolah berhasil diperbarui!", "success")
                return redirect("/kepsek")
            except:
                flash(f"Data Kepala sekolah gagal diperbarui!", "danger")
                return redirect("/kepsek")

        elif request.form['action'] == "tambah":
            nama_kepsek = request.form.get("namaTambahKepsek")
            nip_kepsek = request.form.get("nipTambahKepsek")

            try:
                db.execute("INSERT INTO data_kepsek (id, nama_kepsek, nip_kepsek) VALUES ((SELECT MAX(id) + 1 FROM data_kepsek), ?, ?)", nama_kepsek, nip_kepsek)

                flash(f"Data Kepala sekolah berhasil ditambahkan!", "success")
                return redirect("/kepsek")
            except:
                flash(f"Data Kepala sekolah gagal ditambahkan!", "danger")
                return redirect("/kepsek")
        elif request.form['action'] == "Hapus":
            id_kepsek = request.form.get('idHapus')

            try:
                db.execute("DELETE FROM data_kepsek WHERE id = ?", id_kepsek)

                flash(f"Data Kepala sekolah berhasil dihapus!", "success")
                return redirect("/kepsek")
            except:
                flash(f"Data Kepala sekolah gagal dihapus!", "danger")
                return redirect("/kepsek")

    else:
        rows = db.execute("SELECT * FROM data_kepsek")

        page = request.args.get('page', 1, type=int)
        per_page = 5
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = (len(rows) + (per_page - 1))
        data = math.ceil(len(rows) / per_page)

        item_on_page = rows[start:end]

        return render_template("kepsek.html", rows=item_on_page, total_pages=total_pages, page=page, data=data)


@app.route("/tambah_praktik", methods = ["GET", "POST"])
def tambah_praktik():
    if request.method == "POST":
        judul_praktik = request.form.get("judulPraktik")
        tingkatan_praktik = request.form.get("tingkatanPraktik")
        deskripsi_praktik = request.form.get("deskripsiPraktik")
        jenis_praktik = request.form.get("jenisPraktik")
        tanggal_praktik = datetime.today().strftime('%Y-%m-%d')
        tanggal_name = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        if jenis_praktik == "link":
            nama_file = request.form.get("linkPraktik")
            size_file = "0"

            try:
                db.execute("INSERT INTO praktik_baik (id, judul_praktik, tingkatan, deskripsi, tanggal_praktik, nama_file, tipe_file, size_file,  id_user) VALUES ((SELECT MAX(id) + 1 FROM praktik_baik), ?, ?, ?, ?, ?, ?, ?, ?)", judul_praktik, tingkatan_praktik, deskripsi_praktik, tanggal_praktik, nama_file, jenis_praktik, size_file, session["user_id"])

                flash(f"Data praktik baik anda berhasil ditambahkan!", "success")
                return redirect("/tambah_praktik")
            except:

                flash(f"Data praktik baik anda gagal ditambahkan!", "danger")
                return redirect("/tambah_praktik")

        elif jenis_praktik == "pdf":
            file_pdf = request.files['pdfPraktik']

            nama_file = file_pdf.filename
            file_extension = nama_file.rsplit('.', 1)[1].lower()
            new_nama_file = tanggal_name + '.' + file_extension

            try:
                file_size = "0"
                request.files['pdfPraktik'].save('static/praktik/' + new_nama_file)
                db.execute("INSERT INTO praktik_baik (id, judul_praktik, tingkatan, deskripsi, tanggal_praktik, nama_file, tipe_file, size_file,  id_user) VALUES ((SELECT MAX(id) + 1 FROM praktik_baik), ?, ?, ?, ?, ?, ?, ?, ?)", judul_praktik, tingkatan_praktik, deskripsi_praktik, tanggal_praktik, new_nama_file, jenis_praktik, file_size, session["user_id"])

                flash("Data praktik baik anda berhasil ditambahkan!", "success")
                return redirect("/tambah_praktik")
            except:

                flash("Data praktik baik anda gagal ditambahkan!", "danger")
                return redirect("/tambah_praktik")


    else:
        return render_template("tambah_praktik.html")
