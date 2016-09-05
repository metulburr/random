<?php


if(!defined("IN_MYBB"))
{
	die("Direct initialization of this file is not allowed.<br /><br />Please make sure IN_MYBB is defined.");
}

function mwsshcode_info() {
	return array(
		"name"			=> "MWS Syntax Highlighter",
		"description"	=> "[shcode=python][/shcode] SyntaxHighlighter is an open source Java Script client side code syntax highlighter..",
		"website"		=> "http://alexgorbatchev.com/SyntaxHighlighter/",
		"author"		=> "MaRZoCHi",
		"authorsite"	=> "http://www.marzochi.ws",
		"version"		=> "1.1",
		"compatibility" => "14*,16*",
		"guid" 			=> "8036c90522d8e7d1b30caa08b218c2e7"
	);
}

$plugins->add_hook("parse_message", "mwsshcode_run");

function mwsshcode_activate() {
	global $db;
	$insertarray = array(
		'name' => 'mwsshcode', 
		'title' => 'MWS Syntax Highlighter', 
		'description' => "Full settings of Syntax Highlighter.", 
		'disporder' => 100, 
		'isdefault' => 0
	);
	$gid = $db->insert_query("settinggroups", $insertarray);
	
	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_enabled",
		"title" 		=> "Active?",
		"description" 	=> "Activate Plugin?",
		"optionscode"   => "yesno",
		"value"         => 2,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);
	
	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_auto-links",
		"title"			=> "Automatic Links",
		"description"	=> "Allows you to turn detection of links in the highlighted element on and off. If the option is turned off, URLs won’t be clickable",
		"optionscode"   => "yesno",
		"value"         => 2,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_gutter",
		"title"			=> "Gutter Style",
		"description"	=> "Allows you to turn gutter with line numbers on and off.",
		"optionscode"   => "yesno",
		"value"         => 1,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);	

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_theme",
		"title"			=> "Higlight Theme",
		"description"	=> "SyntaxHighlighter introduced custom CSS themes.Select your theme",
		"optionscode"    => "radio
Default=Default
Django=Django
Eclipse=Eclipse
Emacs=Emacs
FadeToGrey=FadeToGrey
MDUltra=MDUltra
Midnight=Midnight
RDark=RDark",
		"value"          => "Default",
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);	

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_smart-tabs",
		"title"			=> "Smart Tbas",
		"description"	=> "Allows you to turn smart tabs feature on and off",
		"optionscode"   => "yesno",
		"value"         => 1,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);	

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_tab-size",
		"title"			=> "Smart Tab Size",
		"description"	=> "Allows you to adjust tab size",
		"optionscode"	=> "text",
		"value"			=> 4,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_toolbar",
		"title"			=> "Show Toolbar",
		"description"	=> "Toggles toolbar on/off",
		"optionscode"   => "yesno",
		"value"         => 0,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_class-name",
		"title"			=> "Extra Style Class",
		"description"	=> "Enter Custom CSS class name for applying to code area",
		"optionscode"	=> "text",
		"value"			=> "",
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);

	$setting = array(
		"sid"			=> NULL,
		"name"			=> "mwsshcode_first-line",
		"title"			=> "First-Line Number",
		"description"	=> "Allows you to change the first (starting) line number",
		"optionscode"	=> "text",
		"value"			=> 1,
		"disporder"		=> 2,
		"gid"			=> $gid
	);
	$db->insert_query("settings", $setting);
	rebuild_settings();
}
global $ins_count;
$ins_count = 0;
function insert_template_codes() {
	global $mybb,$ins_count;
	if ($ins_count == 0) {
		$shcode	= "<!-- start: mws_shcode -->\n";
		$shcode .= "<link type=\"text/css\" rel=\"stylesheet\" href=\"{$mybb->settings['bburl']}/inc/plugins/syntax/styles/shCore{$mybb->settings['mwsshcode_theme']}.css\">\n<script src=\"{$mybb->settings['bburl']}/inc/plugins/syntax/scripts/shCore.js\" type=\"text/javascript\"></script>\n<script type=\"text/javascript\">";
		$shcode .= "\n\tSyntaxHighlighter.defaults['toolbar'] = {$mybb->settings['mwsshcode_toolbar']};"; 
		$shcode .= "\n\tSyntaxHighlighter.defaults['first-line'] = {$mybb->settings['mwsshcode_first-line']};"; 
		$shcode .= "\n\tSyntaxHighlighter.defaults['tab-size'] = {$mybb->settings['mwsshcode_tab-size']};"; 
		$shcode .= "\n\tSyntaxHighlighter.defaults['smart-tabs'] = {$mybb->settings['mwsshcode_smart-tabs']};"; 
		$shcode .= "\n\tSyntaxHighlighter.defaults['auto-links'] = {$mybb->settings['mwsshcode_auto-links']};"; 
		$shcode .= "\n\tSyntaxHighlighter.defaults['guttter'] = {$mybb->settings['mwsshcode_gutter']};"; 
		$shcode .= "\n\tSyntaxHighlighter.all();";
		$shcode .= "\n</script>\n";
		$shcode	.= "<!-- end: mws_shcode -->";
		$GLOBALS['headerinclude'] .= $shcode ;
		$ins_count = 1;
	}
}

function mwsshcode_deactivate() {
	global $db;
	$db->delete_query("settinggroups", "name = 'mwsshcode'");
	rebuild_settings();
}

function mwsshcode_check($brush,$text) {
	global $mybb;
	insert_template_codes();
	$text = preg_replace("/\<a href=\"(.*?)\"(.*?)>(.*?)\<\/a\>/si","\\3",$text);
	$text = str_replace ( "\n", "&#10;", $text);
	$sstart = "";
	$sfinish = "";
	if (!empty($mybb->settings['mwsshcode_class-name'])) {
		$sstart = "<div class=\"{$mybb->settings['mwsshcode_class-name']}\">";
		$sfinish = "</div>";
	}
	return "<script type=\"text/javascript\" src=\"{$mybb->settings['bburl']}/inc/plugins/syntax/scripts/shBrush_{$brush}.js\"></script>{$sstart}<pre class=\"brush: {$brush};\">{$text}</pre>{$sfinish}";
}


function mwsshcode_run($content) {
	global $mybb;
	if ($mybb->settings['mwsshcode_enabled']) {
		$content = preg_replace("/\[shcode\=(.+?)\](.*?)\[\/shcode\]/ies", '"".mwsshcode_check("$1","$2").""', $content);
	}
	return $content;
}
?>