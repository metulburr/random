function mibimage(but_name) {
	button = '';
	if (but_name=='imgur') {
		if (iclid.trim()!='') {
			button = '<style type="text/css">'+
				'.sceditor-button-'+but_name+' div  {'+
					'background-image: url('+rootpath+'/jscripts/sceditor/myinsertbuttons/'+but_name+'.png) !important;'+
				'}'+
				'.sceditor-button-'+but_name+' div.imgurup  {'+
					'background-image: url('+rootpath+'/jscripts/sceditor/myinsertbuttons/spinner.gif) !important;'+
				'}'+			
			'</style>';
		}
	}
	else {
		button = '<style type="text/css">'+
			'.sceditor-button-'+but_name+' div  {'+
				'background-image: url('+rootpath+'/jscripts/sceditor/myinsertbuttons/'+but_name+'.png) !important;'+
			'}'+
		'</style>';	
	}
	return button;
}

function mibutton(but_name,type) {
	if (but_name=='imgur') {
		if (iclid.trim()!='') {
			$.sceditor.command.set("imgur", {
				_imgur: function() {
					document.querySelector('textarea').insertAdjacentHTML( 'afterEnd', '<input class="imgur" style="visibility:hidden;position:absolute;top:0;" type="file" onchange="upload(this.files[0])" accept="image/*">' );
					document.querySelector('input.imgur').click();				
				},
				exec: function ()
				{
					$.sceditor.command.get("imgur")._imgur();
				},
				txtExec: function() 
				{
					$.sceditor.command.get("imgur")._imgur();
				},
				tooltip: 'Upload to Imgur'
			});
		}
	}
	else {
		if (!type) {
			$.sceditor.command.set(''+but_name+'', {
				exec: function () {
					this.insert('['+but_name+']', '[/'+but_name+']');
				},
				txtExec: ['['+but_name+']', '[/'+but_name+']'],
				tooltip: 'Insert a '+but_name+''
			});
		}
		else {
			$.sceditor.command.set(''+but_name+'', {
				_dropDown: function (editor, caller, html) {
					var content, description;

					content = $(
						'<div>' +
							'<label for="des">' + editor._('Description (optional):') + '</label> ' +
							'<input type="text" id="des" />' +
						'</div>' +
						'<div><input type="button" class="button" value="' + editor._('Insert') + '" /></div>'
					);

					content.find('.button').click(function (e) {
						description = content.find('#des').val();
						before = '[' + but_name + ']';
						end = '[/' + but_name + ']';

						if (description) {
							descriptionAttr = '=' + description + '';
							before = '[' + but_name + ''+ descriptionAttr +']';
						}

						if (html) {
							before = before + html + end;
							end	   = null;
						}

						editor.insert(before, end);
						editor.closeDropDown(true);
						e.preventDefault();
					});

					editor.createDropDown(caller, 'insert'+but_name+'', content);
				},
				exec: function (caller) {
					$.sceditor.command.get(''+but_name+'')._dropDown(this, caller);
				},
				txtExec: function (caller) {
					$.sceditor.command.get(''+but_name+'')._dropDown(this, caller);
				},
				tooltip: 'Insert a '+but_name+''
			});		
		}
	}
}

/*****************************
 * Add imgur upload function *
 *****************************/
function upload(file) {

	/* Is the file an image? */
	if (!file || !file.type.match(/image.*/)) return;

	/* It is! */
	document.body.className = "uploading";
	var d = document.querySelector(".sceditor-button-imgur div");
	d.className = d.className + " imgurup";

	/* Lets build a FormData object*/
	var fd = new FormData(); // I wrote about it: https://hacks.mozilla.org/2011/01/how-to-develop-a-html5-image-uploader/
	fd.append("image", file); // Append the file
	var xhr = new XMLHttpRequest(); // Create the XHR (Cross-Domain XHR FTW!!!) Thank you sooooo much imgur.com
	xhr.open("POST", "https://api.imgur.com/3/image.json"); // Boooom!
	xhr.onload = function() {
		var code = '[img]' + JSON.parse(xhr.responseText).data.link + '[/img]';
		$('#message, #signature, textarea[name*="value"]').data('sceditor').insert(code);
		var d = document.querySelector(".sceditor-button-imgur div.imgurup");
		d.className = d.className - " imgurup";
		document.querySelector('input.imgur').remove();
	}
	// Ok, I don't handle the errors. An exercice for the reader.
	xhr.setRequestHeader('Authorization', 'Client-ID '+iclid+'');
	/* And now, we send the formdata */
	xhr.send(fd);
};