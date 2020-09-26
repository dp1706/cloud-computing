<!DOCTYPE html>
<html>
<head>
  <title>client_login</title>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">  
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  
</head>
<body>
  <center>
    <a href="login.php" class="text-success">Customer Login</a><a class="ml-5" href="login2.php">Owner Login</a><a class="ml-5" href="register.php">Register</a>
  </center>
<form action="login.php" method="post"> 
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
  $conn = mysqli_connect("dwarkadb.c2rtzccaylej.us-east-2.rds.amazonaws.com", "dwarka", "abcd12345efgh", "Cloud_login");
  if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
  } 
  $sql = "select pass from prime where name='$uname'";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    if(strcmp($row["pass"],$passd)==0){
      $_SESSION["username"] = $uname;
    echo "<script>window.location.href='feed.php'</script>";
    exit();
   // echo "wellcome";
    }
    else{
    }
  }
}else{
       
  exit();
    }
  $conn->close();
  ?>
