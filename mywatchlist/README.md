# Tugas 3 Django Project
## LINK APLIKASI
https://django-project-iqbal.herokuapp.com/mywatchlist
<hr>

## Perbedaan Antara JSON, XML, dan HTML

JSON atau JavaScript Object Notation adalah suatu format file berbentuk teks yang digunakan untuk menyimpan dan melakukan transmisi objek data dalam bentuk key dan value. JSON digunakan untuk menyimpan informasi dalam suatu cara yang mudah diakses dan terorganisir karena pengaksesannya lebih cepat serta efisien dibanding dalam bentuk XML.

XML atau Extensible Markup Language didesain untuk menyimpan data dan sangat populer untuk melakukan transfer data (data delivery). XML diturunkan dari SGML dan memberikan ruang untuk men-define markup elements dan generate customized markup language. XML menggunakan tags dalam formatnya, sehingga pengaksesan lebih lambat dan ukuran data lebih besar dibandingkan dengan JSON.

HTML atau Hypertext Markup Language adalah suatu markup language yang digunakan untuk menampilkan data-data pada web page. Pada HTML, dapat melakukan kustomisasi tampilannya pada web page dengan menambahkan elemen statis dan dinamis agar tampilan menjadi lebih menarik.

<hr>

## Mengapa Data Delivery Penting dalam Pengimplementasian Sebuah Platform?

Data delivery menjadi hal yang sangat dibutuhkan pada suatu platform yang dinamis agar seorang client atau user bisa melakukan CRUD process (Create, Read, Update, Delete). Untuk mencapai hal tersebut, dapat menggunakan beberapa data delivery format seperti JSON, XML, dan juga HTML. Dengan data delivery, komunikasi antara user dan platform akan menjadi lebih efisien dan mudah.

<hr>

## Implementasi
1. Membuat aplikasi Django baru bernama `mywatchlist` dengan cara menjalankan command `python manage.py startapp mywatchlist` pada direktori.
2. Menambahkan path `mywatchlist` pada `urlpatterns` di file `urls.py` yang ada pada folder `project-django` agar dapat menghandle pengaksesan path `mywatchlist/` dengan isi `path('mywatchlist/', include('mywatchlist.urls'))`. Setelah itu, saya menambahkan mywatchlist pada `installed_app` yang ada pada `settings.py`.
3. Membuat class model ‘MyWatchlist’ yang menyimpan variable watched (BooleanField), title (CharField), rating (DecimalField), release_date (DateField), dan review (TextField) pada file `models.py` yang ada pada folder `mywatchlist`.
4. Menambahkan 10 data film yang ingin dimasukkan pada database dalam file baru bernama `initial_mywatchlist_data.json` pada folder baru`fixtures` yang terletak di dalam folder `mywatchlist`
5. Membuat fungsi pada `views.py` yang berfungsi untuk menampilkan watchlist dalam HTML, JSON, dan XML. Selanjutnya melakukan routing pada `urls.py` dengan menambahkan path HTML, JSON, dan XML pada `urlpatterns`.
6. Melakukan migration dengan menjalankan command `python manage.py makemigrations` dan `python manage.py migrate` serta loaddata dengan command `python manage.py loaddata initial_mywatchlist_data.json`.
<hr>

## Postman
### HTML Response
![html](/images/Postman_HTML.jpg)

### JSON Response
![html](/images/Postman_JSON.jpg)

### XML Response
![html](/images/Postman_XML.jpg)