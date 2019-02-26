<!DOCTYPE html>
<head>
  <title>PUGB: Your one-stop website for all things doggo battle royale</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
  <link rel="stylesheet" href="/static/style.css">
</head>

<body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">
	    <img src="/static/icon.jpg" class="d-inline-block align-top" width="30" height="30" alt="icon">
	    <b>PUGB</b>
      </a>
	
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
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
	  <button type="button" class="btn btn-warning" onClick="document.getElementById('play').scrollIntoView();"><b>JOIN THE BATTLE!</b></button>
	</div>
  </nav>

	<div class="jumbotron">
      <div class="container">
	    <h1>The market has been dominated by hooman Battle Royale games, but we are launching a doggo-based VR-BR game !</h1>
      </div>
      <div class="container hovertitle" style="margin-top:10%; margin-bottom:10%">
	    <h1 style="font-size: 4vw; text-align:center">&horbar; PUPPER UNBORK's &horbar;</h1>
		<h1 style="font-size: 8vw; text-align:center"><u>GOODBOYES</u></h1>
      </div>

	  <div class="container">
	    <div class="row">

	      <div class="col-6">
	        <h3 class="s-text" style="padding-top:10%">The game is still in Early Access due to the difficult nature of augmenting human vision into doggo vision ...</h3>
		  </div>

		  <div class="col-5" style="margin-left:5%;">
		    <img src="/static/sad.gif" class="responsive-m" alt="sad doggo" style="border-style:inset; border-width:4px;">
	      </div>

  	    </div>
	  </div> <!-- close container-->
	</div>
	
	<div class="jumbotron bg-secondary">
	  <div class="container">
		<div class="row">

		  <div class="col-8">
            <h2 class="s-text">However, if you become one of our monthly Patreon supporters, we will give you a secret <u>Alpha-tester key</u>, much excite !!!!</h2>
	        <small style="font-family: Ubuntu;">*We simply ask for a humble $1000<sub><i>/mth</i></sub> as the dogs keep destroying our motion capture equipment</small> 
	      </div>

	      <div class="col-3" style="margin-left:5%;">
	        <img src="/static/excited.gif" class="responsive" alt="excited doggo" style="border-style:inset; border-width:2px;">
	      </div>

        </div>
      </div>
	</div>

	<div class="jumbotron" id="play" style="margin-bottom:20%">
	  <h2 class="s-text">We expect the game to leave Early Access in about 5 years </h2>
	  <h2 class="s-text">until then, stay tuned for new updates and make sure to check out some of our heckin' cool concept art !</h2>
	</div>

</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
</html> 
