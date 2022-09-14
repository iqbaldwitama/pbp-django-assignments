# Tugas 2 Django Project
### LINK APLIKASI
https://django-project-iqbal.herokuapp.com/

### BAGAN
![Bagan](../static/Flowchart.jpg?raw=true) 
<br>
Aplikasi bekerja diawali dengan request yang diberikan oleh client yang kemudian akan diproses oleh URL dan diteruskan ke Views. Fungsi yang ada pada Views akan dijalankan dan melakukan query ke Models yang diteruskan ke Database. Selanjutnya, Database akan mengembalikan query yang direquest dan meneruskannya ke template untuk dirender. Terakhir, template tersebut diteruskan ke client untuk ditampilkan.
<br>
<hr>

### Virtual Environment
**Penjelasan mengenai Virtual Environment dan alasan menggunakannya** 
<br>
Python virtual environment (env) adalah sebuah tool yang dapat berfungsi untuk menjaga dependencies yang dibutuhkan oleh berbagai macam project yang berbeda dengan membentuk suatu virtual environment yang terisolasi secara khusus untuk masing-masing project tersebut. Ketika kita menggunakan virtual environment, maka segala data yang dibutuhkan oleh suatu project seperti packages, libraries, ataupun version akan terinstall pada project tersebut saja sehingga dapat menghindari adanya konflik dengan project lain.

**Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
<br>
Jawabannya adalah bisa. Namun, ketika kita melakukan instalasi ataupun update packages dan dependencies, maka segala instalasi tersebut akan mengubah data secara global pada local storage kita yang dapat menyebabkan konflik karena perbedaan versi.
<hr>

### Implementasi poin 1-4
**Poin 1 (views.py)**
<br>
Pada file views.py yang ada di dalam folder katalog, saya membuat suatu fungsi baru bernama show_katalog yang menerima sebuah parameter request. Pada fungsi tersebut, tersimpan data-data dalam bentuk dictionary yang akan digunakan pada file katalog.html. Data-data yang terdapat dalam dictionary tersebut adalah list_item yang didapatkan dari class CatalogItem pada file models.py, nama, serta id dan method ini akan mengembalikan hasil rendernya.
<br>

**Poin 2 (urls.py)**
<br>
Pada file urls.py yang ada pada folder katalog, saya menambahkan path baru pada urlpatterns yaitu path('', show_katalog, name='show_katalog') yang di mana merujuk fungsi yang ada pada models.py pada folder katalog yaitu show_katalog untuk dipetakan pada katalog.html. Sedangkan pada file urls.py yang ada pada folder project_django, saya menambahkan path('katalog/', include('katalog.urls')). Hal ini bertujuan agar ketika routing ke /katalog dilakukan, akan dipetakan file urls.py pada folder katalog.
<br>

**Poin 3 (katalog.html)**
<br>
Pada file katalog.html, saya menambahkan data yang telah dibuat pada dictionary di file views.py sebelumnya. Untuk menampilkannya ke dalam file html, cukup dengan menambahkan key data dan ditulis dalam syntax {{key}}, sebagai contoh {{nama}} untuk menampilkan value dari key ‘nama’ yang telah di-assign. Terakhir, untuk menampilkan daftar item yang telah di-assign ke key ‘list_item’, perlu dilakukan looping dengan menggunakan for loop.
<br>

**Poin 4 (deployment to Heroku)**
<br>
Terakhir, untuk melakukan deployment aplikasi ke Heroku, saya mendaftarkan HEROKU_API_KEY dan HEROKU_APP_NAME ke secret yang ada pada setting aplikasi github.