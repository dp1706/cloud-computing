<!DOCTYPE html>
<html>
<head>
	<title>shwo</title>
	<meta charset="utf-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">  
	  <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
	<section class="p-5">
		<table class="table ml-5" style="width: 600px;">
		  <thead>
		    <tr>
		      <th scope="col">Customers List</th>
		    </tr>
		  </thead>
		  <tbody>
		<?php
		$conn = mysqli_connect("dwarkadb.c2rtzccaylej.us-east-2.rds.amazonaws.com", "dwarka", "abcd12345efgh", "Cloud_login");
		if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
		} 
		$sql = "SELECT * from prime";
		$result = $conn->query($sql);
		if ($result->num_rows > 0) {

		while($row = $result->fetch_assoc()) {

			echo "<tr><td> " . $row["name"]. "</td><tr>";
			}
		  echo "</tbody>";
		echo "</table>";	
		}

		else { echo "0 results"; }

		$conn->close();
		?>    
	</section>
<section class="p-5">
	<table class="table ml-5" style="width: 600px;">
	  <thead>
	    <tr>
	      <th scope="col">Name</th>
	      <th scope="col">Feedback</th>
	    </tr>
	  </thead>
	  <tbody>
	<?php
	$conn = mysqli_connect("dwarkadb.c2rtzccaylej.us-east-2.rds.amazonaws.com", "dwarka", "abcd12345efgh", "Cloud_login");
	if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
	} 
	$sql = "SELECT * from feed";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {

	while($row = $result->fetch_assoc()) {

		echo "<tr><td> " . $row["name"]. "</td><td>" . $row["feed_b"]. "</td><tr>";
		}
	  echo "</tbody>";
	echo "</table>";	
	}

	else { echo "0 results"; }

	$conn->close();
	?>    
</section>
</body>
</html>
