<?php
    $dbhost = 'localhost:3306';
    $dbuser = 'root';
    $dbpass = 'root';
    $conn = mysqli_connect($dbhost,$dbuser,$dbpass);

    if(!conn){
      die('Could Not Connect to dataBase:- '.mysqli_error());

    }
    echo 'Connect Succesfully';
    mysqli_select_db($conn,'test');
    $query = 'select * from posts';
    $result = mysqli_query($conn,$query);
    mysqli_close($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>This is PHP Page</title>
</head>
<body>
    
    <h1>Hello World</h1>
       <?php   if(mysqli_num_rows($result)>0):?>
               <ul>
              <?php while($row=mysqli_fetch_object($result)):?>
                 <li><?php echo $row->text?></li>  
              <?php endwhile;?>
               </ul>
     <?php else: ?>
       <p>No Posts</p>   
       <?php endif; ?>
</body>
</html>