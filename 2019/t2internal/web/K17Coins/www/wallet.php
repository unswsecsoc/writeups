<?php

require_once('config.php');
error_reporting(E_ALL);

$db = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

function register() {
  global $db;
  if (!isset($_POST['username']))
    die;
  if (!isset($_POST['password']))
    die;
  if (strlen($_POST['username']) < 3)
    die("Username must has at least 3 characters");
  if (strlen($_POST['password']) < 3)
    die("Password must has at least 3 characters");
  $result = $db->query("SELECT * FROM users WHERE username='".$db->escape_string($_POST['username'])."'");
  if (!$result)
    die;
  if ($result->num_rows > 0)
    die('username already exists');
  for ($i = 0; $i < 5; $i++) {
    $db->query("INSERT INTO users (username, subacc, money, password) VALUES('".$db->escape_string($_POST['username'])."', $i, 100, '".$db->escape_string($_POST['password'])."')");
  }
  setcookie("username", $_POST['username']);
  setcookie("password", $_POST['password']);
}

function auth($username, $password) {
  global $db;
  $result = $db->query("SELECT * FROM users WHERE username='".$db->escape_string($username)."' AND password='".$db->escape_string($password)."'");
  if (!$result)
    return false;
  if ($result->num_rows == 0)
    return false;
  return true;
}

// session is hard
// so we use cookies
// but i heard that people can forge cookies
// so we also put password in the cookies
// and have this middleware to check it for every request
function ensure_login() {
  $errmsg = 'auth failed, plz clear cookies';
  if (!isset($_COOKIE['username']))
    die($errmsg);
  if (!isset($_COOKIE['password']))
    die($errmsg);
  if (!auth($_COOKIE['username'], $_COOKIE['password']))
    die($errmsg);
}

function login() {
  if (!isset($_POST['username']))
    die;
  if (!isset($_POST['password']))
    die;
  if (!auth($_POST['username'], $_POST['password']))
    die("wrong password");
  setcookie("username", $_POST['username']);
  setcookie("password", $_POST['password']);
}

function transfer() {
  global $db;

  /* check data validity */
  if (!isset($_POST['from']))
    die;
  if (!isset($_POST['to']))
    die;
  if (!isset($_POST['amount']))
    die;
  $from = intval($_POST['from']);
  $to = intval($_POST['to']);
  $amount = floatval($_POST['amount']);
  if ($from < 0 || $to < 0 || $from > 4 || $to > 4)
    die;

  /* make sure subacc has enough money */
  $result = $db->query("SELECT money FROM users WHERE username='".$db->escape_string($_COOKIE['username'])."' AND subacc=$from");
  $money = $result->fetch_row()[0];
  if ($money < $amount)
    die("not enough money");
  $money -= $amount;

  /* log the transfer */
  $log = "{$_COOKIE['username']}: transfering $amount from $from to $to";
  syslog(LOG_INFO, $log);
  // we keep the log mainly for legal purposes
  // make sure nobody tampers with syslog, we store hash of log for later verification
  // we keep hashing the hashed string, so we can form a blockchain in syslog
  // if anyone modifies anything in log, we'll know since all the subsequent hashes
  // would mismatch
  // this makes us super secure because i heard that blockchain is unhackable
  for ($i = 0; $i < 10; $i++) {
    $log = password_hash($log, PASSWORD_DEFAULT);
    syslog(LOG_INFO, $log);
  }

  /* perform the transfer */
  $db->query("UPDATE users SET money=$money WHERE username='".$db->escape_string($_COOKIE['username'])."' AND subacc=$from");
  $db->query("UPDATE users SET money=money+$amount WHERE username='".$db->escape_string($_COOKIE['username'])."' AND subacc=$to");
}

function buy() {
  global $db;

  /* check data validity */
  if (!isset($_COOKIE['username']))
    die('login first');
  if (!isset($_POST['subacc']))
    die;
  if (!isset($_POST['item']))
    die;
  $subacc = intval($_POST['subacc']);
  if ($subacc < 0 || $subacc > 4)
    die;
  $good = intval($_POST['item']);

  /* make sure subacc has enouggh money */
  $result = $db->query("SELECT price FROM goods WHERE id=$good");
  $price = $result->fetch_row()[0];
  $result = $db->query("SELECT id, money FROM users WHERE username='".$db->escape_string($_COOKIE['username'])."' AND subacc=$subacc");
  $res= $result->fetch_row();
  $money = $res[1];
  $user = $res[0];
  if ($money < $price)
    die("not enough money");
  $money -= $price;

  /* actually buy the item */
  $db->query("UPDATE users SET money=$money WHERE username='".$db->escape_string($_COOKIE['username'])."' AND subacc=$subacc");
  $db->query("INSERT INTO user_good VALUES($user, $good)");
}

// main logic
if (isset($_REQUEST['action'])) {
  switch ($_REQUEST['action']) {
  case 'register':
    register();
    header("Location: ?");
    die;
  case 'login':
    login();
    header("Location: ?");
    die;
  case 'buy':
    ensure_login();
    buy();
    break;
  case 'transfer':
    ensure_login();
    transfer();
    break;
  case 'src':
    show_source(__FILE__);
    die;
  default:
    break;
  }
}

?>
<html>
  <head>
    <link rel="stylesheet" href="https://www.google.cn/css/maia.css">
    <title>K17Coins</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
  </head>
  <body>
    <div class="maia-header" id="maia-header" role="banner">
      <div class="maia-aux">
        <h1>
          K17Coins
        </h1>
        <h2>
          Wallet (alpha)
        </h2>
      </div>
    </div>

    <div id="maia-main" role="main">
      <div>
        <h3>Item List</h3>
        <?php
        $result = $db->query("SELECT id, name, price FROM goods");
        while ($row = $result->fetch_array()) {
          echo "Item id {$row[0]}: {$row[1]}, price: \${$row[2]}<br>";
        }
        echo "</div>";

        if (isset($_COOKIE['username'])) {
          echo "<div><div>";
          ensure_login();
          // TODO: what about XSS attack
          echo "You are logged into {$_COOKIE['username']}<br>";
          $result = $db->query("SELECT * FROM users WHERE username='".$db->escape_string($_COOKIE['username'])."'");
          while ($row = $result->fetch_array()) {
            echo "<h3>Sub Acc {$row[2]}</h3>";
            echo "Wallet: \${$row[3]}<br>";
            echo "Items Owned:<br>";
            $items = $db->query("SELECT goods.name, goods.content FROM goods, user_good WHERE user_good.user={$row[0]} AND user_good.good=goods.id");
            while ($item = $items->fetch_array()) {
              echo $item[0] . ": " . $item[1] . "<br>";
            }
          }
        ?>
        </div>
        <div>
          <h3>Transfer Money</h3>
          <form action="?action=transfer" method="POST">
            <input type="number" name="from" placeholder="from subacc id">
            <input type="number" name="to" placeholder="recipient subacc id">
            <input type="number" name="amount" placeholder="amount">
            <input type="submit" value="Transfer" class="maia-button">
          </form>
        </div>
        <div>
          <h3>Buy Item</h3>
          <form action="?action=buy" method="POST">
            <input type="number" name="subacc" placeholder="subacc id">
            <input type="number" name="item" placeholder="item id">
            <input type="submit" value="Buy" class="maia-button">
          </form>
        </div>
      </div>
      <?php } else {?>
      <h3>Login/Register First</h3>
      <div>
        <form method="POST">
          <input type="text" name="username" placeholder="user name">
          <input type="password" name="password" placeholder="password">
          <input type="submit" name="action" value="login" class="maia-button">
          <input type="submit" name="action" value="register" class="maia-button">
        </form>
      </div>
      <?php } ?>
      <a href="?action=src">Sauce</a>
    </div>
    <div class="maia-footer" id="maia-footer">
      <div id="maia-footer-global">
        <div class="maia-aux">
          <ul>
            <li>Copyright 2019 K17Coins. No rights reserverd. Developed by <a href="https://www.adamyi.com">adamyi</a>.</li>
          </ul>
        </div>
      </div>
    </div>
  </body>
</html>
