<?php

ini_set('session.cookie_httponly', 0);

if(isset($_REQUEST['page']) && $_REQUEST['page'] != "") {
	$page = $_REQUEST['page'];

	//Filter against "file" and script
	$page = preg_replace("/file/", '', $page);
	$page = preg_replace("/script/", '', $page);	

	$no = '<h2 align="center"><u><b>ACCESS FORBIDDEN</b></u></h2><br \><h3 align="center">A moderator has been dispatched to review your search</h3>';

	//Alert the admin 
	if(preg_match("/localhost/i", $page) || preg_match("/127\.0\.0\.1/", $page)) {

		$result = $no;
		$triggered = 1; 

		//exec the command to clean files older than 5 minutes
		exec("find /var/www/html/payloads -mmin +5 -type f -exec rm -fv {} \;");


	//Normal case where no dangerous words used
	} else {
		try {
			$session = curl_init();
			curl_setopt($session, CURLOPT_URL, $page);
			curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($session, CURLOPT_FOLLOWLOCATION, true);
			curl_setopt($session, CURLOPT_SSL_VERIFYPEER, false);
			curl_setopt($session, CURLOPT_TIMEOUT, 10);
			
			$result = curl_exec($session);
			curl_close($session);

			//Resource not found 
			if(is_null($result) || empty($result)) {
				$result = '<h3 style="color:red;" align="center">Failed to fetch resource.</h3>';
			}

		} catch (Exception $e) {
			trigger_error(sprintf('Curl failed with #%d %d', $e->getCode(), $e->getMessage(), E_USER_ERROR));
		}
	}
}

	if($triggered == 1) { 
		ob_start();
	}

?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0/lux/bootstrap.min.css" rel="stylesheet" integrity="sha384-GxhP7S92hzaDyDJqbdpcHqV5cFflxAx0Yze/X7vUONp43KK1E8eUWaJIMkit3D0R" crossorigin="anonymous">
    
    <title>Super Secure Resource Finder</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="/">Super Secure Resource Finder</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarColor03">
        </div>
		<?php if(isset($_REQUEST["page"])) {
			echo "<span class=\"navbar-text\">Requested: $page</span>\n";
		}?>
      </div>
    </nav>

    <div class="container mt-5">    
      <h3>Who needs <u>TOR</u> when you can request pages through us ?</h3>
      <form method="get" action="/">
        <input class="form-control mt-5" name="page" type="text" placeholder="wttr.in" />
		<!-- try wttr.in/Moon it's pretty cool -->
        <input class="btn btn-info mt-3" type="submit" value="Submit" />
      </form>
    </div>

	<?php if(isset($result)) { /* This code only prints on POST */?>
		<div class="jumbotron" style="margin-top:2%;">
		  <div class="well"> <!-- start of resource -->
			<?php echo "\n$result\n\n"; ?>
		  </div> <!-- end of resource -->
		</div>
	<?php } ?>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.min.js" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  
  </body>
</html>

<?php 

	//echo "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	if($triggered == 1){
		
		#save temp file 
		$id = md5(uniqid(rand(), true));
		$filename = $id.'.html';
		file_put_contents('/var/www/html/payloads/'.$filename, ob_get_contents());

		#get admin to execute it
		$cmd = "/usr/bin/python /etc/triggerxss.py http://$_SERVER[HTTP_HOST]/payloads/".$filename;
		//echo $cmd;
		exec($cmd);

	}
	
?>
