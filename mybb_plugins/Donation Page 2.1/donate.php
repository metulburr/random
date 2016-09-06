<?php
/*
*
* Donation Page Plugin
* Copyright 2009-2010 MyBBWebHost, all rights reserved.
* http://www.mybbwebhost.com
* This plugin is provided as-as.  You may edit the plugin as you please, but you may not remove this in-file copyright.
* You may not distribute this plugin or claim it as your own.
*
*/

define('IN_MYBB', 1); 
define('THIS_SCRIPT', 'donate.php');
require_once "./global.php";

$message = $mybb->settings['dp_message'];

if ( $mybb->user['username'] == '' ) {
$username = 'Guest';
} else {
$username = $mybb->user['username'];
}
if ( $mybb->settings['dp_credits'] == "1" ) {
$credits = '<div class="smalltext" style="text-align:right;">Donation Page plugin created by <a href="http://www.mybbwebhost.com" title="MyBBWebHost - MyBB Oriented Hosting">MyBBWebHost</a>.</div>';
} else {
$credits = '';
}

$minimum = $mybb->settings['dp_minimum'];

$formcheck = '<script type="text/javascript">
<!--
function validate_form ( )
{
valid = true;
if ( document.donation_form.amount.value < '. $minimum .' )
{
alert ( "Please enter a minimum of '. $minimum . ' ' .$mybb->settings['dp_currency'] .'." );
valid = false;
}
return valid;
}
//-->
</script>';


$value = $mybb->settings['dp_value'];

if ( $mybb->settings['dp_guests'] == "0" && $mybb->user['uid'] == "0" ) {
$paypalform = '<div style="margin-top:10px;margin-bottom:5px;font-weight:bold;text-align:center;">You must <a href="member.php?action=login">login</a> or <a href="member.php?action=register">register</a> in order to donate.  Sorry!</div>';
} else {
$paypalform = '<form action="https://www.paypal.com/cgi-bin/webscr" method="post" style="margin-top:10px;text-align:center;" name="donation_form" onsubmit="return validate_form ( );">
<input type="hidden" name="cmd" value="_xclick">
<input type="hidden" name="business" value="'.$mybb->settings['dp_email'].'" />
<input type="hidden" name="item_name" value="'.$mybb->settings['bbname'].' Donation from '. $username .'">
<input type="hidden" name="no_note" value="0" />
<input type="hidden" name="currency_code" value="'.$mybb->settings['dp_currency'].'">
<input name="return" value="'.$mybb->settings['bburl'].'" type="hidden">
<input name="cancel_return" value="'.$mybb->settings['bburl'].'" type="hidden">
<input type="hidden" name="tax" value="0" />
<label><strong>Username:</strong> '. $username .'</label><br style="margin-bottom:5px;" />
<label style="font-weight:bold;">Donation Amount (in '. $mybb->settings['dp_currency'] .'):</label><br />
<input type="text" class="textbox" name="amount" style="width:120px;text-align:left;margin:7px;" value="'. $value .'" /><br />
<input type="image" src="https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif" style="border:0;" name="submit" alt="PayPal - The safer, easier way to pay online!" />
</form>';
}
$title = $mybb->settings['dp_title'];

add_breadcrumb($title, "donate.php");

eval("\$donate = \"".$templates->get("donation_page")."\";"); 
output_page($donate); 
?>