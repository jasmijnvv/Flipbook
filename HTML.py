def create_page_cover(book_name, image_path):
    page_cover = f"\
        <div class='page cover'> \n \
        <h1>{book_name}</h1> \n \
        <img src='{image_path}' alt='Example image' width='300' class='Opaopbed'> \n \
    </div> \n "

    return page_cover

def create_page(chapter_name, text, image_path, naam):
  page = f" \
  <div class='page'> \n \
     <audio src='audio/H1 Opa de kat.mp4' controls></audio> \n \
    <h2>{chapter_name}</h2> \n \
    <p> \n \
        {text} \
    </p> \n \
    <img src='{image_path}' width='180' class='Opaopstoel'> \n \
    <p> \n \
        {naam}\
    </p> \n \
  </div> \n "

  return page


doc_begin = "<!DOCTYPE html> \n \
 <html> \n \
<head> \n \
  <meta charset='UTF-8'> \n \
  <title>Book Flip Demo</title> \n \
 \n \
  <!-- Use prebuilt library --> \n \
  <script src='https://unpkg.com/page-flip/dist/js/page-flip.browser.js'></script> \n \
 \n \
  <style> \n \
    #book { \n \
      width: 400px; \n \
      height: 600px; \n \
      margin: 10px auto; \n \
      margin-bottom: 40; \n \
      flex-direction: column; \n \
      align-items: center; \n \
    } \n \
    .page { \n \
      background: rgb(232, 225, 208); \n \
      border: 1px solid #ccc; \n \
      display: flex; \n \
      justify-content: center; \n \
      align-items: center; \n \
      font-size: 30px; \n \
    } \n \
    audio { \n \
    color-scheme: light; \n \
    width: 190px; \n \
    height: 25px; \n \
    } \n \
    audio {margin-bottom: -30px;} \n \
    h1 {text-align: center; \n \
    margin-bottom: 5px;} \n \
    h2 {text-align: center; \n \
    margin-bottom: -0.25px;} \n \
    p {text-align: left; \n \
    margin-left: 15px; \n \
    margin-top: 5px} \n \
    div {text-align: center;} \n \
 \n \
    .Opaopbed{ \n \
      display: block; \n \
      margin-left: auto; \n \
      margin-right: auto; \n \
      margin-bottom: auto; \n \
    } \n \
    .Opaopstoel{ \n \
      display: block; \n \
      margin-left: auto; \n \
      margin-right: auto; \n \
      margin-bottom: auto; \n \
    } \n \
    .ObesiOpa{ \n \
      display: block; \n \
      margin-left: auto; \n \
      margin-right: auto; \n \
      margin-bottom: auto; \n \
    } \n \
    .Opaopdieet{ \n \
      display: block; \n \
      margin-left: auto; \n \
      margin-right: auto; \n \
      margin-bottom: auto; \n \
    }  \n \
    .Opaisfit{ \n \
      display: block; \n \
      margin-left: auto; \n \
      margin-right: auto; \n \
      margin-bottom: auto; \n \
    } \n \
a { \n \
  text-decoration: none; \n \
  display: inline-block; \n \
 \n \
  padding: 10px 26px;} \n \
a:hover { \n \
  background-color: #ddd; \n \
  color: black;} \n \
.vorige { \n \
  background-color: #fdfdfd; \n \
  border: 1px solid black; \n \
  color: black; \n \
  width: 5px; \n \
  height: 20px; \n \
  margin-top: 10px; \n \
  margin-bottom: auto; \n \
  } \n \
.volgende { \n \
  background-color: #fe8002; \n \
  border: 1px solid black; \n \
  color: white; \n \
  width: 5px; \n \
  height: 20px; \n \
  margin-top: 10px; \n \
  margin-bottom: auto; \n \
  } \n \
  </style> \n \
</head> \n \
 \n \
<body> \n \
<div id='book'> \n "
   
doc_end = "\
 \n \
  <div class='controls'> \n \
    <a onclick= 'previousPage()' href ='#' class='vorige'>&laquo;</a> \n \
    <a onclick= 'nextPage()' href='#' class='volgende'>&raquo;</a> \n \
  </div> \n \
 \n \
</div> \n \
 \n \
<script> \n \
  const pageFlip = new St.PageFlip( \n \
    document.getElementById('book'), \n \
    { \n \
      width: 500, \n \
      height: 600, \n \
      showCover: true \n \
    } \n \
  ); \n \
 \n \
  pageFlip.loadFromHTML(document.querySelectorAll('.page')); \n \
 \n \
  function nextPage() {pageFlip.flipNext()} \n \
  function previousPage() {pageFlip.flipPrev()} \n \
</script> \n \
 \n \
</body> \n \
</html> \n \
"
