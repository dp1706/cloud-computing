<!DOCTYPE html>
<html>
<head>
	<title>feedd_back</title>
	<meta charset="utf-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">  
	  <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<style type="text/css"></style>
</head>
<body>
	<center>
	  <a href="login.php" class="text-success">Customer Login</a><a class="ml-5" href="login2.php">Owner Login</a><a class="ml-5" href="r2.php">Register</a>
	</center>
	<section>
		<div class="container p-5">
		  <form action="feed.php" method="post" style="margin-left: 30%;" class="p-3">
		    <label for="subject">Give Feedback</label><br>
		    <input type="write something" name="feed_back" class="p-3  m-2" style="width: 50%;"><br>
		    <input type="submit" value="Submit" class="btn btn-primary btn-sm px-2 ">
		  </form>
		</div>
	</section>
<?php
session_start();
	#echo "Name " . $_SESSION["username"] . "<br>";
$name = $_SESSION["username"];
$input= filter_input(INPUT_POST, 'feed_back');
$conn = mysqli_connect("dwarkadb.c2rtzccaylej.us-east-2.rds.amazonaws.com", "dwarka", "abcd12345efgh", "Cloud_login");
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
} 
else  
{
    if (empty($input)){
	    
	}
	else{
		    $sql = "INSERT INTO feed values ('$name','$input')";
		    if ($conn->query($sql))
		    {
		      echo "<center>New record is inserted sucessfully<center>";
		    }
		    else
		    {
		      echo "Error: ". $sql ."". $conn->error;
			}
			  $input= NULL;
			$name= NULL; 
	}		
  $conn->close();
  }
?>
</body>
</html>
