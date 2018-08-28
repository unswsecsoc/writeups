<?php setrawcookie("meme","but_did_you_try_flag.php_?"); ?>

<!DOCTYPE html>
<html>
<head>
  <title>PUGB: Your one-stop website for all things doggo battle royale</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
  <link rel="stylesheet" href="/static/style.css">
</head>

<!-- TODO: fix the QR code alignment issue --> 
<!-- TODO: remove this page from robots.txt after proper filters against web crawlers are installed -->

<body style="background-color:black;">

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="/">
	    <img src="/static/icon.jpg" class="d-inline-block align-top" width="30" height="30" alt="">
	    <b>PUGB</b>
      </a>
	
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="/">Home </a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">News</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/media.php">Media</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Support</a>
          </li>
        </ul>
      </div>

	  <span class="navbar-text">PUPPER UNBORK's GOODBOYES &nbsp;</span>
	  <button type="button" class="btn btn-success" onClick="document.getElementById('key').scrollIntoView();"><b>JOIN THE BATTLE!</b></button>
	</div>
  </nav>

	<div class="jumbotron bg-success m-tight">
      <div class="container">
		<h1 class="m-text" style="font-family:Helvetica;">Thank you for your valued contribution ! </h1>
	  </div>
	</div>
	
	<div id="key" class="jumbotron bg-secondary">
	  <div class="container">
		<h2 class="s-text">As promised, here is the key !!! Just scan the QR code below</h2>
		<small><i>(phone camera recommended)</i></small>

		<div class="container" style="text-align:center;">
		  <pre>
<?php
		    $session = curl_init();
			curl_setopt($session, CURLOPT_URL, "http://qrenco.de/flag%7Bits_2018_and_people_are_still_getting_rickrolled%7D");
			curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($session, CURLOPT_USERAGENT, "curl/1.33.7"); /* cleaner output */
			curl_setopt($session, CURLOPT_HEADER, false);

			$result = curl_exec($session);
			curl_close($session);
			echo $result;   /* echo preg_replace("#\\n#", "\n", $result); */
		?>
		  </pre>  
		</div>  <!-- QR code generated using qrenco.de --> 

      </div>
	</div>

</body>

</html> 
