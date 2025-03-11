<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "car_rental_admin";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    exit();
}

// Prepare the SQL statement
$query = "SELECT * FROM bookedcars";
$statement = $pdo->prepare($query);

// Execute the prepared statement
$statement->execute();

// Fetch all the rows as an associative array
$result = $statement->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="css/bootstrap.css">
<style>
table, th, td {
  border:1px solid black;
  border-collapse: collapse;
}

#bookedcars {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#bookedcars td, #bookedcars th {
  border: 1px solid #ddd;
  padding: 8px;
}

#bookedcars tr:nth-child(even){background-color: #f2f2f2;}

#bookedcars tr:hover {background-color: #ddd;}

#bookedcars th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}

.btn {
  background-color: #04AA6D;
  color: white;
  padding: 8px 10px;
  border: 0px;
  cursor: pointer;
  border-radius: 3px;
  outline: none;
  height: 5vh;
  width: 5%;
}
</style>
</head>
<body>

<h2 style="text-align:center">CAR RENTALS</h2>
<br>

<table id="bookedcars">
  <tr>
    <th>Car ID</th>
    <th>Model</th>
    <th>Number Plate</th>
  </tr>

  <?php
  // Process and display the results
  foreach ($result as $row) {
      echo "<tr>
              
              <td>" . htmlspecialchars($row['car_id']) . "</td>
              <td>" . htmlspecialchars($row['model']) . "</td>
              <td>" . htmlspecialchars($row['number_plate']) . "</td>
            </tr>";
  }
  ?>
</table>

</body>
</html>

<?php
// Close the prepared statement
$statement->closeCursor();
?>
