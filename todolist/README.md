# Tugas 4 Django Project
## LINK APLIKASI
https://django-project-iqbal.herokuapp.com/todolist
<hr>

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

`{% csrf_token %}` adalah salah satu tag yang diimplementasikan pada Django untuk menghindari malicious attacks. Attack yang dimaksud adalah Cross Site Request Forgery (CSRF) yaitu sebuah serangan yang memungkinkan attacker untuk menyebabkan user melakukan hal yang tidak diinginkan. `{% csrf_token %}` bersifat unik, rahasia, dan unpredictable yang dihasilkan oleh sisi server suatu aplikasi dan ditransmisi ke client sehingga dapat menghindari serangan. 

Apabila kita tidak mengimplementasikan `{% csrf_token %}` pada aplikasi, website akan tetap dapat berjalan seperti biasa. Namun, terdapat beberapa celah sehingga attacker dapat menyerang bagian user dan site yang menjadi rawan karena tidak adanya proteksi. Karena kedua hal tersebut merupakan dua hal yang paling krusial dalam suatu aplikasi, maka Django tidak membiarkan deployment tanpa adanya `{% csrf_token %}`.
<hr>

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Bisa. Kita dapat membuat `form` secara manual dengan cara menambahkan tag `<input><\input>` sesuai dengan type, name, dan value yang kita inginkan. Setelah form tersebut disubmit, data tersebut dapat kita akses dengan menggunakan method `request.POST.get("title")`.
<hr>

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML

Pertama-tama, user akan menekan tombol submit. Kemudian data-data input dari user dapat dengan suatu `POST.get` method di `views`. Setelah terjadi pengiriman data POST request ke server, maka database pada server akan berubah sesuai dengan event dari POST request tersebut. Terakhir, views akan memanggil function render yang berisikan data yang akan ditampilkan pada HTML sehingga data akan terupdate dengan versi yang terbaru.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi todolist dengan menjalankan perintah `python manage.py startapp todolist`.
2. Menambahkan path `path('todolist/', include('todolist.urls')),` pada `urls.py` dan aplikasi `todolist` pada `settings.py`.
3. Membuat class baru pada `models.py` dan membuat fields yang dibutuhkan seperti `user`, `date`, `title`, `description`, `status`.
4. Mengimplementasikan form registrasi, login, logout, show_todolist, create_task, update_task.
5. Membuat dan mengimplementasikan file-file HTML pada folder templates.
6. Menambahkan routing pada todolist pada `urls.py` seperti register, login, logout, create-task.
7. Lakukan migrations dengan menjalankan perintah `python manage.py makemingrations` dan `python manage.py migrate`.
8. Lakukan git add, commit, dan push ke repository.
