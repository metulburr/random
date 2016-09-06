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

if(!defined("IN_MYBB"))
{
	die("Direct initialization of this file is not allowed.<br /><br />Please make sure IN_MYBB is defined.");
}

$plugins->add_hook("build_friendly_wol_location_end", "donationpage_online");

// Plugin Information
function donationpage_info()
{
    return array(
        "name"        => "Donation Page",
        "description" => "Sets up a page where your users can donate to your PayPal account.",
        "website"     => "http://www.mybbwebhost.com",
        "author"      => "MyBBWebHost",
        "authorsite"  => "http://www.mybbwebhost.com",
        "version"     => "2.1",
	"compatibility" => "*",
	"guid"        => "6dd78c94f6ead4eb1770080da7668f63 ",
        );
}

function donationpage_is_installed()
{
	global $db;

if ($db->num_rows($db->simple_select("settings","name","name='dp_title'")) >= 1)	
{
		return true;
	}

	return false;
}

// Install and Activate
function donationpage_activate() {

global $db;

    $dp_group = array(
        "gid" => "NULL",
        "name" => "donationpage",
        "title" => "Donation Page Settings",
        "description" => "Set up and edit your donation page here.",
        "disporder" => "35",
        "isdefault" => "no",
        );
    $db->insert_query("settinggroups", $dp_group);
    $gid = $db->insert_id();
    
    $dp_1 = array(
        "sid" => "NULL",
        "name" => "dp_title",
        "title" => "Donation Page Title",
        "description" => "This is the display title of your donation page.",
        "optionscode" => "text",
        "value" => "Donation Page",
        "disporder" => "1",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_1);

    $dp_2 = array(
        "sid" => "NULL",
        "name" => "dp_guests",
        "title" => "Guest Access",
        "description" => "Should guests be allowed to donate?",
        "optionscode" => "yesno",
        "value" => "1",
        "disporder" => "2",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_2);

    $dp_3 = array(
        "sid" => "NULL",
        "name" => "dp_currency",
        "title" => "Currency",
        "description" => "What is the currency you wish to be paid in?",
        "optionscode" => "select
USD= US Dollars
AUD= Australian Dollars
GBP= British Pound
CAD= Canadian Dollars
JPY= Japanese Yen
DKK= Danish Krone
HKD= Hong Kong Dollar
JPY= Japanese Yen
CHF= Swiss Franc
PLN= Polish Zloty
SGD= Singapore Dollar
EUR= Euro",
        "value" => "USD",
        "disporder" => "3",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_3);

    $dp_4 = array(
        "sid" => "NULL",
        "name" => "dp_email",
        "title" => "PayPal Email",
        "description" => "What is your PayPal email address?",
        "optionscode" => "text",
        "value" => "paypal@example.com",
        "disporder" => "4",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_4);

    $dp_5 = array(
        "sid" => "NULL",
        "name" => "dp_message",
        "title" => "Donation Page Message",
        "description" => "What would you like it to say on the donation page? (HTML Permitted)",
        "optionscode" => "textarea",
        "value" => "Want to show how much you care about our forum?  With web hosting, domain, and advertising costs, it''s expensive to keep our forum up and running.  Currently, all of the expensive come right out of the administrator''s pocket.  That''s why we now offer a method for you to donate and help us stay online!<br /><br />While the suggested donation is $10, we will be thankful for ALL donations, big and small.  100% of donations will be used for our forums, and NONE of it will be used for personal expenses.  To get started, simply enter an amount below and click Donate.",
        "disporder" => "5",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_5);

    $dp_6 = array(
        "sid" => "NULL",
        "name" => "dp_value",
        "title" => "Recommended Donation Amount",
        "description" => "The amount of money you recommend users to donate (Will appear in textbox by default, do not include currency symbols!)",
        "optionscode" => "text",
        "value" => "10.00",
        "disporder" => "6",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_6);

    $dp_7 = array(
        "sid" => "NULL",
        "name" => "dp_minimum",
        "title" => "Minimum Donation Amount",
        "description" => "This is the minimum amount of money required to donate - Recommended: 1, Disable: 0. (Decimal numbers are allowed, do not include currency symbols!)",
        "optionscode" => "text",
        "value" => "1",
        "disporder" => "7",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_7);

    $dp_8 = array(
        "sid" => "NULL",
        "name" => "dp_credits",
        "title" => "Keep MyBBWebHost Credit Line?",
        "description" => "While we greatly appreciate it if you leave the credits line at the bottom of the Donation Page, it is not required.",
        "optionscode" => "yesno",
        "value" => "1",
        "disporder" => "8",
        "gid" => intval($gid),
        );
    $db->insert_query("settings", $dp_8);

$insert_array = array(
		'title' => 'donation_page',
		'template' => $db->escape_string('<html>
<head>
<title>{$mybb->settings[\'bbname\']} - {$mybb->settings[\'dp_title\']}</title>
{$headerinclude}
{$formcheck}
</head>
<body>
{$header}
<table border="0" cellspacing="{$theme[\'borderwidth\']}" cellpadding="{$theme[\'tablespace\']}" class="tborder">
<tr>
<td class="thead"><strong>{$mybb->settings[\'dp_title\']}</strong></td>
</tr>
<tr>
<td width="100%" class="trow1">
{$message}
{$paypalform}
{$credits}
</td>
</tr>
</table>
{$footer}
</body>
</html>'),
		'sid' => '-1',
		'version' => '',
		'dateline' => TIME_NOW
	);
	
	$db->insert_query("templates", $insert_array);


rebuildsettings();

}

// Deactivate and Uninstall
function donationpage_deactivate() {

global $db, $mybb;
    require "../inc/adminfunctions_templates.php";
    $query = $db->query("SELECT gid FROM ".TABLE_PREFIX."settinggroups WHERE name='donationpage'");
    $g = $db->fetch_array($query);
    $db->query("DELETE FROM ".TABLE_PREFIX."settinggroups WHERE gid='".$g['gid']."'");
    $db->query("DELETE FROM ".TABLE_PREFIX."settings WHERE gid='".$g['gid']."'");
    $db->delete_query("templates","title='donation_page'");

rebuildsettings();

global $db;

}

function donationpage_online(&$plugin_array)
{
if (preg_match('/donate\.php/',$plugin_array['user_activity']['location']))
{
$plugin_array['location_name'] = "Viewing <a href=\"donate.php\">Donation Page</a>";
}

return $plugin_array;
}
?>