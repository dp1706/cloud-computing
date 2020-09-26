<?php
$owner_name="time";
$main_pass="123";
?>
<!DOCTYPE html>
<html>
<head>
  <title>iclient_login</title>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">  
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  
</head>
<body>
  <center>
    <a href="login2.php" class="text-success">Owner Login</a><a class="ml-5" href="login.php">Customer Login</a>
  </center>
<form action="login2.php" method="post"> 
<div class="site-section mt-5">
        <div class="container">


            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="row">
                        <div class="col-md-12 form-group">
                            <label for="username" >Username</label>
                            <input type="text" name="name"  class="form-control form-control-lg" autocomplete="off" autofocus/>
                        </div>
                        <div class="col-md-12 form-group">
                            <label for="pword">Password</label>
                            <input type="password" name="passd" class="form-control form-control-lg" autocomplete="off" >
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <input type="submit" value="login" class="btn btn-primary btn-lg px-5">
                        </div>
                    </div>
                </div>
            </div>
  </form>       
  
</body>
</html>

  <?php
 session_start();
   $uname= filter_input(INPUT_POST, 'name');
  $passd= filter_input(INPUT_POST, 'passd'); 
    if(strcmp($owner_name,$uname)==0){
      if (strcasecmp($main_pass, $passd)==0) {
      $_SESSION["owner_name"] = $uname;
    echo "<script>window.location.href='show.php'</script>";
    exit();
      }
     }
      
  ?>