# Overview
<img src="./static/images/logo_panjang.png" height="120px">
`ITP (Informatics Teachers Platform)` is a web-based application developed with Python, HTML, CSS, JavaScript, Bootstrap and FontAwesome. The main modules used to develop `ITP` is Flask (https://palletsprojects.com/p/flask/) and CS50 Library for Python (https://cs50.readthedocs.io/libraries/cs50/python/), while the database engine used in `ITP` is SQLite (https://www.sqlite.org/index.html).

Link to the video: https://youtu.be/68mjlXaamWc

# Database Schema
The database is designed using relational model to connected all the table. Foreign key constraint is used to keep the database integrity.

Table structure for table `akun_login` : the first step to use the website 

    CREATE TABLE `akun_login` (
      `id` int(11) pirmary key NOT NULL,
      `username` varchar(99) NOT NULL,
      `email` varchar(99) NOT NULL,
      `password` varchar(99) NOT NULL,
      `id_user` int(10) NOT NULL,
      `jenis_akun` varchar(100) NOT NULL
    )

Table structure for table `data_akun` : after the user has login, the data will save in table of `data_akun`.

	CREATE TABLE `data_akun` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `nama` varchar(100) NOT NULL,
	  `nip` bigint(50) NOT NULL,
	  `alamat` varchar(100) NOT NULL,
	  `nomor_hp` bigint(20) NOT NULL,
	  `email_pribadi` varchar(100) NOT NULL,
	  `email_pmm` varchar(100) NOT NULL,
	  `pendidikan_terakhir` varchar(50) NOT NULL,
	  `tempat_lahir` varchar(100) NOT NULL,
	  `tanggal_lahir` date NOT NULL,
	  `jenis_kepegawaian` varchar(100) NOT NULL,
	  `nik` bigint(50) NOT NULL,
	  `nuptk` bigint(50) NOT NULL,
	  `sekolah` varchar(99) NOT NULL,
	  `jenis_kelamin` varchar(90) NOT NULL,
	  `gol_jab` varchar(99) NOT NULL
	)

Table structure for table `data_kepsek` : to save the id of headmaster for the member of `MGMP/ITP` community.

	CREATE TABLE `data_kepsek` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `nama_kepsek` varchar(100) NOT NULL,
	  `nip_kepsek` bigint(100) NOT NULL
	)

Table structure for table `data_sekolah` : to save the id of school for the member of `MGMP/ITP` community.

	CREATE TABLE `data_sekolah` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `nama_sekolah` varchar(100) NOT NULL,
	  `alamat_sekolah` varchar(100) NOT NULL,
	  `npsn` int(50) NOT NULL,
	  `kecamatan` varchar(99) NOT NULL,
	  `kab_kota` varchar(99) NOT NULL,
	  `kepsek` int(12) NOT NULL
	)

Table structure for table `perangkat_pembelajaran` : to save the matterial 

	CREATE TABLE `perangkat_pembelajaran` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `judul` varchar(100) NOT NULL,
	  `tingkatan` varchar(100) NOT NULL,
	  `deskripsi` varchar(200) NOT NULL,
   	  `tanggal_perangkat` date NOT NULL,
	  `nama_file` varchar(100) NOT NULL,
	  `tipe_file` varchar(100) NOT NULL,
	  `size_file` bigint(60) NOT NULL,
	  `id_user` int(12) NOT NULL
	)

Table structure for table `pertemuan` : to save the meeting 

	CREATE TABLE `pertemuan` (
	  `id` int(11) PRIMARY KEYNOT NULL,
	  `pertemuan` int(12) NOT NULL,
	  `tanggal` date NOT NULL,
	  `lokasi` int(12) NOT NULL,
	  `link` varchar(100) NOT NULL
	)

Table structure for table `praktik_baik` : to save the sharing good parctice

	CREATE TABLE `praktik_baik` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `judul_praktik` varchar(100) NOT NULL,
	  `tingkatan` varchar(100) NOT NULL,
	  `deskripsi` varchar(400) NOT NULL,
	  `tanggal_praktik` date NOT NULL,
	  `nama_file` varchar(100) NOT NULL,
	  `tipe_file` varchar(100) NOT NULL,
	  `size_file` bigint(20) NOT NULL,
	  `id_user` bigint(6) NOT NULL
	)

Table structure for table `supervisi` : to save the data of evaluation teacher teaching methods

	CREATE TABLE `supervisi` (
	  `id` int(11) PRIMARY KEY NOT NULL,
	  `id_user` int(12) NOT NULL,
	  `semester` int(12) NOT NULL,
	  `nama_file` varchar(100) NOT NULL,
	  `waktu_pengajuan` date NOT NULL,
	  `status_kepsek` int(12) NOT NULL,
	  `status_pengawas` int(12) NOT NULL,
	  `deskripsi_kepsek` varchar(200) NOT NULL,
	  `deskripsi_pengawas` varchar(200) NOT NULL
	)

# Structure

All the assets and resources used in this application are located inside the `static` folder. Meanwhile `templates` keep all the HTML files which renders results returned by `app.py`.
The backbone of `ITP` is in `app.py`, where records from the database are retrieved and modified, user inputs are processed, and results are rendered to the templates.
`helpers.py` provides several functions to help with multi-level authentication and the adaptation of the famous CS50's. `readme.md` contains introductions related to the `ITP` website. 

	-final_project/
 		-flask_session/
   		-static/
	 	-templates/
   		-app.py
	 	-helpers.py
   		-simgmpinformatika.db
	 	-DESIGN.md
   		-README.me

|-templates/ |
| :--------: |
-akun.html
-cari_perangkat.html
-cari_praktik.html
-index.html
-jadwal.html
-kepsek.html
-konfirmasi.html
-layout.html
-pengurus.html
-perangkat.html
-praktik.html
-sekolah.html
-setting.html
-struktur.html
-tambah_perangkat.html
-tambah_praktik.html

# Project Team

| Muh. Ikram Abdillah Mata | Yudi Arianto Latief | Sri Febrina Ramadhani |
| :---------: | :---------: | :--------: |
