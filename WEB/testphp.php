<!doctype html>
<html>
<head>
<style>
body{
  margin: 0;
  background: #d9d9d9;
  color:#fff;
}
table, th, td {
  border: black;
  border-collapse: collapse;
}
table{
    margin: auto;
}
th, td {
  padding: 8px;
  text-align: center;
}
#form{
  font-size:20px;
}
#again{
    top: 0%;
    width: 100%;
    height: 10%;
    font-size:20px;
}
header{
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  padding: 10px;
  background-color: #8c8c8c;
  border-bottom: 4px solid #4d4d4d;
  margin: 0;
  width: 100%;
}
#button{
  width:60px;
  height:30px;
  background-color: #4d4d4d;
  border: none;
  color:#fff;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 10px;
  cursor: pointer;
  border-radius: 30px;
}
#url{
  margin-right:8px;
  margin-left:8px;
  height:30px;
  border: 3px solid #4d4d4d;
  border-radius:10px;
}
.container{
   width: 1000px;
    margin: auto;
    margin-top: 60px;
}
ul.tabs{
   margin: 0px;
   padding: 0px;
   list-style: none;
    font-size: 20px;
}
ul.tabs li{
   background: none;
   color: #fff;
   display: inline-block;
   padding: 10px 15px;
   cursor: pointer;
    font-weight: bold;
}
ul.tabs li.current{
    background: #a6a6a6;
   color: #fff;
    font-weight: bold;
}
.tab-content{
   display: none;
   background: #a6a6a6;
   padding: 15px;
}
.tab-content.current{
   display: inherit;
}
#icon {
    width: 30px;
    height: 30px;
    display: inline-block;
    vertical-align: middle;
}
#icon2 {
    width: 18px;
    height: 18px;
    display: inline-block;
    vertical-align: middle;
    margin-left: 2px;
}
footer{
    border-top: solid 2px #000000;
    font-weight: bold;
    font-size: 15px;
    text-align: center;
    height: 48px;
    bottom: 48px;
    margin-top: 400px;
}
a:link { color: black; text-decoration: none;}
a:visited { color: black; text-decoration: none;}
a:hover { color: black; text-decoration: none;}
#count{
    text-align: right;
    margin-top: 50px;
    margin-left: 160px;
    margin-right: 160px;
    font-weight: bold;
}
</style>
</head>
<body>
<div id="wrap">
<header>
<?php $url=$_GET["url"]; exec("python3 aa.py $url");
echo "<div id=\"again\">
<form id=\"form\" action=\"testpage.php\" method=\"get\">
<a href=\"NoClick.html\"><img id=\"icon\" src=\"icon2.png\">
<b>Check another one! =>   </b></a>
<input type=\"text\" name=\"url\" id=\"url\" value=$url style=\"width:900px\">
<input id=\"button\" type=\"submit\" value=\"Check!\">
</div>"?>
</header>

<div class="container">
   <ul class="tabs">
      <li class="tab-link current" data-tab="tab-1">Result</li>
      <li class="tab-link" data-tab="tab-2">Details</li>
   </ul>
   <div id="tab-1" class="tab-content current">
        <table style="width:75%">
        <tr>
            <th>NUM</th>
            <th>Attack Type</th>
            <th>Malicious Signature / File Name</th>
        </tr>
        <?php
        $host = "localhost"; // 자신의 mysql
        $user = "guest"; // 기본 사용자.
        $password = "1234"; // apm 기본 암호
        $DB_name = "RESULT"; // 데이터베이스 이름 : test
        $conn = mysqli_connect($host, $user, $password, $DB_name);
        $cnt=0;
      if(mysqli_connect_errno($conn)){
          echo "연결실패!";
      }
      else{
          $result = mysqli_query($conn, "select * from RESULT");
          while($row = mysqli_fetch_array($result)){
          // Name 열의 데이터를 가져온다.
              if($row['ATTACKTYPE'] == null){
                  continue;
              }
              else{
                  echo "<tr>";
                  echo "<td>";
                  echo $row['NUM'];
                  echo "</td>";
                  echo "<td>";
                  echo $row['ATTACKTYPE'];
                  echo "</td>";
                  echo "<td>";
                  echo $row['TARGET'];
                  echo "</td>";
                  echo "</tr>";
                  $cnt = $cnt+1;
              }
          }
          echo"</table>";
          if($cnt == 0){
              echo"<div style=\"color:green\" id=\"count\">검출된 위협 수 : 0</div>";
          }
          else{
              echo"<div style=\"color:red\" id=\"count\">검출된 위협 수 : $cnt</div>";
          }
        mysqli_query($conn, "DELETE FROM RESULT");
        mysqli_query($conn, "ALTER TABLE RESULT AUTO_INCREMENT=1");
        mysqli_close($conn);
        ?>
   </div>
   <?php
        $detail = $url;
        echo "<pre>\n";
        print_r(get_headers($detail, 1));
        echo "</pre>\n";
    ?>
    <div id="tab-2" class="tab-content">
    <span style="font-size:20px; font-weight:bold; border-bottom:solid 2px #fff;">HTTP Response</span><br><br>
    <?php
        $detail=get_headers($url,0);
        foreach ($detail as $value)
        {
            echo $value."<br /><br />";
        }
    ?>
</div><!-- container -->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){

   $('ul.tabs li').click(function(){
      var tab_id = $(this).attr('data-tab');

      $('ul.tabs li').removeClass('current');
      $('.tab-content').removeClass('current');

      $(this).addClass('current');
      $("#" + tab_id).addClass('current');
   })

})
</script>
<footer><br>Copyright &copy2019   By team NoClick<img id="icon2" src="icon2.png"></footer>
</div>
</body>

</html>
