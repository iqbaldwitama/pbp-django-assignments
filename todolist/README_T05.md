# Tugas 5 Django Project
## LINK APLIKASI
https://django-project-iqbal.herokuapp.com/todolist
<hr>

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Internal CSS
Internal CSS adalah ketika kode CSS diletakkan di dalam bagian <head> pada halaman HTML. Internal CSS merujuk pada suatu tag HTML yang spesifik, serta menggunakan style yang ditujukan pada elemen halaman yang sesuai. Segala Class dan ID yang digunakan hanya akan berguna pada halaman tersebut.

Kelebihan:
1. Dapat menggunakan class dan ID selector.
2. Tidak perlu mengunggah beberapa file berbeda untuk styling.

Kekurangan:
1. Menambahkan kode pada file HTML dapat memperbesar ukuran page dan waktu loading

### External CSS
External CSS adalah ketika menghubungkan halaman web dengan file .css external. Metode ini cenderung lebih efisien, terlebih lagi ketika ingin styling website yang berskala besar. Dengan External CSS, kita dapat melakukan edit style pada satu .css file saja dapat mengubah style pada seluruh site.

Kelebihan:
1. Karena kode CSS diletakkan pada dokumen yang berbeda, maka struktur pada file HTML akan lebih rapi dan ukurannya lebih kecil.
2. Dapat menggunakan satu file .css yang sama untuk beberapa halaman.

Kekurangan:
1. Terdapat kemungkinan halaman tidak ter-render dengan sempurna sampai file CSS nya berhasil di load.
2. Menghubungkan beberapa file CSS dapat meningkatkan waktu download site.

### Inline CSS
Inline CSS digunakan untuk melakukan styling pada elemen HTML secara spesifik. Untuk CSS jenis ini, hanya diperlukan attribute style pada setiap tag HTML tanpa menggunakan selector. Style jenis ini tidak terlalu direkomendasikan karena styling dilakukan secara individual. Namun, styling jenis ini dapat berfungsi pada beberapa situasi, seperti ketika kita tidak memiliki akses pada file CSS atau ketika hanya membutuhkan styling untuk satu elemen saja.

Kelebihan:
1. Dapat secara mudah memasukkan CSS rules ke dalam halaman HTML, sehingga lebih cepat untuk testing dan mendapatkan preview perubahan yang dilakukan.
2. Tidak perlu membuat dan mengunggah dokumen terpisah untuk styling.

Kekurangan:
1. Memakan waktu dan dapat membuat struktur file HTML menjadi berantakan.
2. Melakukan styling pada beberapa elemen dapat membuat ukuran halaman menjadi besar dan meningkatkan download time.

<hr>
  
## Jelaskan tag HTML5 yang kamu ketahui.

1. `<a>` : mendefinisikan suatu hyperlink
2. `<b>` : menyajikan teks dalam format bold
3. `<body>` : mendefinisikan body dari document
4. `<br>` : memberikan line break
5. `<button>` : membuat clickable button
6. `<div>` : menentukan suatu section dalam document
7. `<head>` : mendefinisikan head dari document
8. `<h1> sampai <h6>` : mendefinisikan heading dari HTML
9. `<hr>` : menyajikan garis horizontal
10. `<p>` : mendefinisikan paragraf
11. `<style>` : memasukkan informasi style pada head document
12. `<table>` : mendefinisikan data dari table
13. `<td>` : mendefinisikan cell pada table
14. `<th>` : mendefinisikan header cell pada table
15. `<tr>` : mendefinisikan row cell pada table

<hr>

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

### Element selector
Selector ini memilih elemen HTML berdasarkan nama elemen.

Contoh dari kode todolist.html:
```
  th {
        font-size: 120%;
        padding: 12px 15px
    }
```

### ID Selector
Selector ini menggunakan atribut id dari elemen HTML untuk memilih elemen.

Contoh dari kode todolist.html:
```
#rcorners1 {
             box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
             border-radius: 25px;
          }
```

### Class Selector
Selector ini memilih elemen HTML dengan atribut class yang spesifik.

Contoh  dari kode todolist.html:
```
.wrap {
        display: flex;
        align-items: center;
        align-content: flex-start;
        justify-content: space-between;
    }
```
  
### Universal Selector
Selector ini memilih semua elemen HTML pada halaman tersebut.

Contoh dari kode todolist.html:
```
* {
    font-family: 'Arial';
    text-align: center;
    vertical-align: middle;
 }
```
  
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Load bootstrap pada Django Project dengan cara menambahkan beberapa barisan kode pada `base.html` yang terletak pada folder templates.
  Pada head:
  ```
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  ```
  Pada body:
  ```
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  ```

2. Melakukan kostumisasi templat pada halaman login, register, todolist, dan create-task dengan cara menambahkan Internal CSS styling pada masing-masing file html. 
3. Mengubah table to-do-list pada `todolist.html` menjadi berbentuk cards dengan grid (row and column) dengan cara menambahkan elemen div yang mengimplementasi class row dan col-sm-3.
4. Menambahkan styling pada cards dengan [referensi](https://getbootstrap.com/docs/4.3/components/card/).
5. Menjadikan halaman-halaman tersebut menjadi responsive serta interactive dengan menambahkan efek ketika hover pada beberapa elemen seperti cards dan button.
6. Add, Commit, dan Push segala perubahan ke GitHub.
