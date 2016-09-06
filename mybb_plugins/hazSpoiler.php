<?php
/**
 * Haz Spoiler
 * Copyright 2015 Hazmole, All Rights Reserved
 * License: http://www.mybb.com/about/license
 *
 * Get a Great help of Sephiroth's [Spoiler MyCode] plugin
 */

// Disallow direct access to this file for security reasons
if(!defined("IN_MYBB"))
{
    die("Direct initialization of this file is not allowed.");
}

function hazSpoiler_info()
{
    return array(
        "name"          => "Haz Spoiler",
        "description"   => "Add [spoiler] tag",
        "website"       => "",
        "author"        => "Hazmole",
        "authorsite"    => "",
        "version"       => "1.0",
        "guid"          => "",
        "codename"      => str_replace('.php', '', basename(__FILE__)),
        "compatibility" => "*"
    );
}

$plugins->add_hook("parse_message", "hazspoiler_run");

function hazspoiler_run($message) {
	
	// Key Define
	$pattern = array("#\[spoiler=(?:&quot;|\"|')?([a-zA-Z0-9!:\#\.\? \',\-\(\)]*?)[\"']?(?:&quot;|\"|')?\](.*?)\[\/spoiler\](\r\n?|\n?)#si", "#\[spoiler\](.*?)\[\/spoiler\](\r\n?|\n?)#si",);
	$replace = array(	hazspoiler_getSpoilerWrap(hazspoiler_getSpoilerHeader("$1"), 		hazspoiler_getSpoilerBody("$2")),
						hazspoiler_getSpoilerWrap(hazspoiler_getSpoilerHeader("Spoiler"), 	hazspoiler_getSpoilerBody("$1")));
	
	// Do
	while(preg_match($pattern[0], $message) or preg_match($pattern[1], $message)) {
		$message = preg_replace($pattern, $replace, $message);
	}
	$find = array(
		"#<div class=\"spoiler_body\">(\r\n?|\n?)#",
		"#(\r\n?|\n?)</div>#"
	);
	$replace = array(
		"<div class=\"spoiler_body\">",
		"</div>"
	);
	$message = preg_replace($find, $replace, $message);
	return $message;
}
// Functions
function hazspoiler_getSpoilerButton($title) {
	$script = "$(this).parent().parent('.spoiler_wrap').children('.spoiler_body').toggle(100);";
	return "<a href=\"javascript:void(0);\" onClick=\"".$script."\">".$title."</a>";
};
function hazspoiler_getSpoilerBody($content) {
	return "<div class=\"spoiler_body\" style=\"display: none; border: 1px blue solid; padding:5px; width:90%;\">".$content."</div>";
};
function hazspoiler_getSpoilerHeader($title) {
	return "<div class=\"spoiler_header\">".hazspoiler_getSpoilerButton($title)."</div>";
};
function hazspoiler_getSpoilerWrap($head, $body) {
	return "<div class=\"spoiler_wrap\">".$head.$body."</div>";
};

?>
