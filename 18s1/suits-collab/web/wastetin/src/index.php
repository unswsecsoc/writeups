<!DOCTYPE html>
<head>
	<title>WasteTin</title>
</head>

<body>

<h1>WasteTin</h1>

<p>WasteTin > PasteBin</p>

<p>Type shit below:</p>
<form id="fuckshit" action="./" method="post">
<textarea form="fuckshit" name="fuck" id="fuck" rows="8" cols="40"></textarea>
<p>Filename (max length 42 characters):
<input type="text" name="shit" id="shit" value="shit" />
<button type="submit">submit</button>
</p>
</form>

<?php
//error_reporting(0); //muhuhuhaha

if (array_key_exists("fuck",$_POST) && array_key_exists("shit",$_POST)) {
   try {
      $fuck = $_POST["fuck"];
      $shit = substr(htmlentities(str_replace('/', '', $_POST["shit"])).".txt", 0, 42);

      //dumb way to make new filename
      $dirname = "files/".uniqid()."/";
      if (!is_dir($dirname)) {
         mkdir($dirname, 0755, true);
      }
      $filename = $dirname.$shit;
      //while(file_exists($filename)) {
      //   $dirname = "files/".uniqid()."/";
      //   if (!is_dir($dirname)) {
      //      mkdir($dirname, 0555, true);
      //   }
      //   $filename = $dirname.$shit;
      //}
      if (file_exists($filename)) {
         print "Sorry, this filename is taken.";
      } else if (realpath($filename) != realpath("/flag")) {
         $fh = fopen($filename, 'w');
         fwrite($fh, $fuck);
         print "<p>Your shit has been uploaded successfully</p>";
         print "View your shit <a href=".$filename.">here</a>";
      } else {
          print "fuck";
      }

   } catch (Exception $e) {
      //print $e;
      die("machine broke machine broke<br>understandable, have a nice day");
   }
}

?>

</body>
