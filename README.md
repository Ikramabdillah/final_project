# ITP (INFORMATIC TEACHERS PLATFORM)
<img src="./static/images/logo_panjang.png" height="120px">

## Collaborator
| Muh. Ikram Abdillah Mata | Yudi Arianto Latief | Sri Febrina Ramadhani |
| :---------: | :---------: | :--------: |

> Build using CS, Python, Flask, HTML, JavaScript, Bootstrap, FontAwesome, and Sqlite for database

| <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/pocoo_flask_logo_icon_168045.png" height="50px"> | <img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" height="50px"> | <img src="https://user-images.githubusercontent.com/30186107/29488525-f55a69d0-84da-11e7-8a39-5476f663b5eb.png" height="50px"> | <img src="https://cdn-icons-png.flaticon.com/512/5968/5968672.png" height="50px"> | <img src="https://pbs.twimg.com/profile_images/1491038861224517637/s-H1KgWO_400x400.png" height="50px"> | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Sqlite-square-icon.svg/1200px-Sqlite-square-icon.svg.png" height="50px"> |
| :--: | :--: | :--: | :--: | :--: | :--: |

## About Application
`ITP (Informatic Teachers Platform)` serves as a digital forum for informatics teachers who are members of the MGMP community. This application provides information about the MGMP Informatics community, starting from activities and documentation of activities, meeting schedules and ultimately the community management structure. In this application, teachers can share lesson plans and good practices about informatics learning in the classroom.

## App Features
> Features:
  - Register and login feature for informatics teacher
  - Share and download lesson plans features
  - Share and download good practice features
> User:
  - Admin User for Admin
    + set the appearance of the app's main page<br>
      | Homepage | Footer |
      | :------: | :----: |
      | <img src="./static/images/screenshot/menu_awal.png"> | <img src="./static/images/screenshot/footer.png"> |

    + Set MGMP meeting schedules<br>
      | Schedule on Homepage | Schedule on Admin Menu |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/jadwal.png"> | <img src="./static/images/screenshot/jadwal_pertemuan.png"> |
      | Edit Schedule | 
      | <img src="./static/images/screenshot/update_jadwal.png"> |

    + Confirming new user<br>
      | Confirm Menu on Admin |
      | :-------------------: |
      | <img src="./static/images/screenshot/konfirmasi.png"> |

    + Manage mgmp community board member data<br>
      | MGMP Board on Homepage | MGMP Board on Admin Menu |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/pengurus1.png"> | <img src="./static/images/screenshot/pengurus.png"> |
      | Edit Member | 
      | <img src="./static/images/screenshot/pengurus_edit.png"> |

    + Manage school data<br>
      | School Data on Admin | Edit School |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/sekolah.png"> | <img src="./static/images/screenshot/sekolah_edit.png"> |

    + Manage principal data<br>
      | Principal Data on Admin | Edit Principal |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/kepsek.png"> | <img src="./static/images/screenshot/kepsek_edit.png"> |
  
  - Basic User for Teacher
    + Register<br>
      | Register Form #1 | Register Form #2 |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/register_1.png"> | <img src="./static/images/screenshot/register_2.png"> |

    + Login<br>
      | Login Form |
      | :------: |
      | <img src="./static/images/screenshot/login.png"> |

    + Account menu<br>
      | Account Menu #1 | Account Menu #2 |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/akun.png" > | <img src="./static/images/screenshot/akun2.png"> |

    + Data account edit<br>
      | Edit Data Form |
      | :------: |
      | <img src="./static/images/screenshot/edit_akun.png"> |

    + Username and password edit<br>
      | Username and Password edit Form |
      | :------: |
      | <img src="./static/images/screenshot/password.png"> |

    + Good practice searching<br>
      | Good practice search form |
      | :------: |
      | <img src="./static/images/screenshot/good_practice.png"> |

    + Searching for good practice<br>
      | Enter keyword | Good Practice details |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/cari_praktik.png"> | <img src="./static/images/screenshot/detail_praktik.png"> |

    + Download or view good practice files<br>
      | Good practice file views | Good practice video views |
      | :------: | :--------: |
      | <img src="./static/images/screenshot/pdf_goodpractice.png"> | <img src="./static/images/screenshot/video_goodpractice.png"> |

    + Add own good practice<br>
      | Add good practice form |
      | :------: |
      | <img src="./static/images/screenshot/add_praktik.png"> |

    + Upload good practice<br>
      | Upload PDF file | Upload Link from YouTube |
      | :------: | :-----: |
      | <img src="./static/images/screenshot/add_pdf.png"> | <img src="./static/images/screenshot/add_link.png"> |

## Database
> Using SQLite

  | Database |
  | :------: |
  | <img src="./static/images/screenshot/database.png" height="300px"> |
  

> Our app use SQLite with database name <b>simgmpinformatika.db</b> has 8 tables:

  - <b>akun_login</b> for manage data that use to login
  - <b>data_akun</b> for manage informatics teacher datas
  - <b>data_kepsek</b> for manage principal datas
  - <b>data_sekolah</b> for manage school datas
  - <b>pengurus</b> for manage member of community board datas
  - <b>perangkat_pembelajaran</b> for manage lesson plans datas
  - <b>pertemuan</b> for manage MGMP meeting schedule datas
  - <b>praktik_baik</b> for manage good practice datas

## About CS50
This is CS50x , Harvard University's introduction to the intellectual enterprises of computer science and the art of programming for majors and non-majors alike, with or without prior programming experience. An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, Python, SQL, and JavaScript plus CSS and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. The on-campus version of CS50x , CS50, is Harvard's largest course. 

Students who earn a satisfactory score on 9 problem sets (i.e., programming assignments) and a final project are eligible for a certificate. This is a self-paced course–you may take CS50x on your own schedule.

### Instructors
| David J. Malan | Doug Lloyd | Brian Yu |
| :------------: | :--------: | :------: |
| <img src="https://pll.harvard.edu/sites/default/files/styles/1_1_xsmall/public/faculty/malan-sq.jpg?itok=h2GJJRFd"> | <img src="https://pll.harvard.edu/sites/default/files/styles/1_1_xsmall/public/faculty/doug-lloyd110x110.jpg?itok=-IEGG-DA"> | <img src="https://pll.harvard.edu/sites/default/files/styles/1_1_xsmall/public/faculty/Screen%20Shot%202020-11-24%20at%2011.46.25%20AM.png?itok=IoLFNl2v"> |

## License
> For open source project

## Documentation
- This video can provide more explanation on how the app works:
  > <a href="https://www.youtube.com/watch?v=68mjlXaamWc&ab_channel=KakYudiOfficial">Click Here</a>
## Acknolegments
- Kementerian Pendidikan, Kebudayaan, Riset dan Teknologi
- Direktorat Jendral Guru dan Tenaga Kependidikan
- Direktorat Jendral Pendidikan Dasar dan Menengah
- Mentors
- CS50 Staff and Fellow Teachers
