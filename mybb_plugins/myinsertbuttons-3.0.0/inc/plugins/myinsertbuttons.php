<?php
/**
 * My Insert Buttons
 * https://github.com/martec
 *
 * Copyright (C) 2015-2015, Martec
 *
 * My Insert Buttons is licensed under the GPL Version 3, 29 June 2007 license:
 *	http://www.gnu.org/copyleft/gpl.html
 *
 * @fileoverview My Insert Buttons - Insert new button in Sceditor for Mybb
 * @author Martec
 * @requires jQuery and Mybb
 */

// Disallow direct access to this file for security reasons
if(!defined("IN_MYBB"))
{
	die("Direct initialization of this file is not allowed.<br /><br />Please make sure IN_MYBB is defined.");
}

define('MIB_PLUGIN_VER', '3.0.0');

function myinsertbuttons_info()
{
	global $lang;

	return array(
		'name'			=> 'My Insert Buttons',
		'description'	=> $lang->myinsertbuttons_plug_desc,
		'website'		=> '',
		'author'		=> 'martec',
		'authorsite'	=> '',
		'version'		=> MIB_PLUGIN_VER,
		'compatibility' => '18*'
	);

}

function myinsertbuttons_install()
{
	global $db, $lang;

	$lang->load('config_myinsertbuttons');

	$query	= $db->simple_select("settinggroups", "COUNT(*) as rows");
	$dorder = $db->fetch_field($query, 'rows') + 1;

	$groupid = $db->insert_query('settinggroups', array(
		'name'		=> 'myinsertbuttons',
		'title'		=> 'My Insert Buttons',
		'description'	=> $lang->myinsertbuttons_sett_desc,
		'disporder'	=> $dorder,
		'isdefault'	=> '0'
	));

	$db->insert_query('settings', array(
		'name'		=> 'myinsertbuttons_rules',
		'title'		=> $lang->myinsertbuttons_rules_title,
		'description'	=> $lang->myinsertbuttons_rules_desc,
		'optionscode'	=> 'textarea',
		'value'		=> 'imgur',
		'disporder'	=> 1,
		'gid'		=> $groupid
	));

	$db->insert_query('settings', array(
		'name'		=> 'myinsertbuttons_rules_des',
		'title'		=> $lang->myinsertbuttons_rulesdes_title,
		'description'	=> $lang->myinsertbuttons_rules_desc,
		'optionscode'	=> 'textarea',
		'value'		=> '',
		'disporder'	=> 2,
		'gid'		=> $groupid
	));

	$db->insert_query('settings', array(
		'name'		=> 'myinsertbuttons_imgurapi',
		'title'		=> $lang->myinsertbuttons_imgur_title,
		'description'	=> $lang->myinsertbuttons_imgur_desc,
		'optionscode'	=> 'text',
		'value'		=> '',
		'disporder'	=> 3,
		'gid'		=> $groupid
	));

	rebuild_settings();
}

function myinsertbuttons_is_installed()
{
	global $db;

	$query = $db->simple_select("settinggroups", "COUNT(*) as rows", "name = 'myinsertbuttons'");
	$rows  = $db->fetch_field($query, 'rows');

	return ($rows > 0);
}

function myinsertbuttons_uninstall()
{
	global $db;

	$db->write_query("DELETE FROM " . TABLE_PREFIX . "settings WHERE name IN('myinsertbuttons_rules')");
	$db->delete_query("settinggroups", "name = 'myinsertbuttons'");
}

function myinsertbuttons_activate()
{
	global $db, $plugins_cache;

	require_once MYBB_ROOT."inc/adminfunctions_templates.php";

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />') . '#i',
		'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>'
	);

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote('<script type="text/javascript">') . '#i',
		"<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}"
	);

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote('maximize,') . '#i',
		'"+newbutbar+newbutbar2+"maximize,'
	);

	if ($plugins_cache['active']['quickadveditorplus'] or $plugins_cache['active']['quickadveditor']) {
		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />') . '#i',
			'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>'
		);

		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote('<script type="text/javascript">') . '#i',
			"<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}"
		);

		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote('maximize,') . '#i',
			'"+newbutbar+newbutbar2+"maximize,'
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />') . '#i',
			'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>'
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote('<script type="text/javascript">') . '#i',
			"<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}"
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote('maximize,') . '#i',
			'"+newbutbar+newbutbar2+"maximize,'
		);
	}
}

function myinsertbuttons_deactivate()
{
	global $db, $plugins_cache;
	include_once MYBB_ROOT."inc/adminfunctions_templates.php";

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>') . '#i',
		'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />'
	);

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote("<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}") . '#i',
		'<script type="text/javascript">'
	);

	find_replace_templatesets(
		'codebuttons',
		'#' . preg_quote('"+newbutbar+newbutbar2+"maximize,') . '#i',
		'maximize,'
	);

	if ($plugins_cache['active']['quickadveditorplus'] or $plugins_cache['active']['quickadveditor']) {
		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>') . '#i',
			'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />'
		);

		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote("<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}") . '#i',
			'<script type="text/javascript">'
		);

		find_replace_templatesets(
			'codebutquick',
			'#' . preg_quote('"+newbutbar+newbutbar2+"maximize,') . '#i',
			'maximize,'
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote('<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />
<script type="text/javascript" src="{$mybb->asset_url}/jscripts/sceditor/myinsertbuttons/mibutton.js?ver='.MIB_PLUGIN_VER.'"></script>') . '#i',
			'<link rel="stylesheet" href="{$mybb->asset_url}/jscripts/sceditor/editor_themes/{$theme[\'editortheme\']}" type="text/css" media="all" />'
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote("<script type=\"text/javascript\">
var newbutbar = newbutbar2 = '',
iclid = '{\$mybb->settings['myinsertbuttons_imgurapi']}';
if (!'{\$mybb->settings['myinsertbuttons_rules']}'.trim() == ''){
	newbut = '{\$mybb->settings['myinsertbuttons_rules']}';
	newbutbar = ''+newbut+'|';
	icm_but_rls = newbut.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',0);
		\$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}
if (!'{\$mybb->settings['myinsertbuttons_rules_des']}'.trim() == ''){
	newbut2 = '{\$mybb->settings['myinsertbuttons_rules_des']}';
	newbutbar2 = ''+newbut2+'|';
	icm_but_rls = newbut2.split(',');
	for (var i = icm_but_rls.length-1; i >= 0; i--) {
		mibutton(''+icm_but_rls[i]+'',1);
		$(mibimage(''+icm_but_rls[i]+'')).insertAfter('textarea');
	}
}") . '#i',
			'<script type="text/javascript">'
		);

		find_replace_templatesets(
			'codebutquick_pm',
			'#' . preg_quote('"+newbutbar+newbutbar2+"maximize,') . '#i',
			'maximize,'
		);
	}
}
?>