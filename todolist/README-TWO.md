# Tugas 6 Django Project
## LINK APLIKASI
https://django-project-iqbal.herokuapp.com/todolist
<hr>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. 

### Asynchronous Programming
Asynchronous programming adalah suatu program yang dapat dijalankan secara paralel. Artinya, program tersebut dapat mengerjakan banyak tugas pada satu waktu yang bersamaan tanpa harus menunggu program sebelumnya selesai.

### Synchronous Programming
Synchronous programming adalah  program yang harus berjalan secara serial atau berurutan. Suatu program akan dijalankan apabila program sebelumnya yang sedang dijalankan sudah selesai beroperasi.

<hr>

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programming adalah sebuah paradigma pemrograman yang flownya akan ditentukan oleh suatu event. Paradigma ini dapat menjalankan program ataupun memanggil function berdasarkan mouse hover, click, dan lain-lain.

Pada tugas ini, salah satu pengimplementasian paradigma Event-Driven Progamming adalah pada
`document.getElementById("button").onclick = addTodo` yang ketika button ditekan, maka task baru akan ditambahkan melalui function addTodo.

<hr>

## Jelaskan penerapan asynchronous programming pada AJAX.

Sebagai pendahuluan, AJAX adalah Asynchronous JavaScript and XMLHTTP. Maka, suatu aplikasi yang mengimplementasikan AJAX akan dijalankan secara asynchronous sehingga dapat di update tanpa melakukan reload pagenya. Implementasinya menggunakan paradigma Event-Driven Programming dan juga AJAX GET dan AJAX POST. Ketika AJAX menerima request dari user, maka AJAX akan mengirimkannya ke server agar datanya dapat diubah secara asynchronous dan user tetap dapat berinteraksi dengan web page. Dan ketika response dikembalikan, AJAX akan menjalankan perintah sesuai dari request tersebut.

<hr>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### AJAX GET
1. Membuat view baru yang mengambil data dalam bentuk JSON dan return response berupa JSON.
2. Implementasikan routing ke function `show_json` dengan menambahkan `path('json/', show_json, name='show_json'),` pada `urls.py`.
3. Import JQuery AJAX dengan menambahkan pada tag `<script>`.
4. Membuat fungsi yang untuk menunjukkan data-data todolist pada HTML.

### AJAX POST
1. Membuat view baru yang dapat membuat object ToDoList baru dan return dalam JsonResponse.
2. Implementasikan routing ke function `create_task_ajax` dengan menambahkan `path('add/', create_task_ajax, name='create_task_ajax'),` pada `urls.py`.
3. Membuat modal bootstrap yang berfungsi untuk membuat task baru.
4. Membuat fungsi untuk membuat object ToDoList baru dan melakukan modifikasi pada modal serta implementasikan form pada modal tersebut.
