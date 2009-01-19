/* Romanian initialisation for the jQuery UI date picker plugin. */
/* Written by Edmond L. (ll_edmond@walla.com). */
jQuery(function(jQuery){
	jQuery.datepicker.regional['ro'] = {
		closeText: 'Inchide',
		prevText: '&#x3c;Anterior',
		nextText: 'Urmator&#x3e;',
		currentText: 'Azi',
		monthNames: ['Ianuarie','Februarie','Martie','Aprilie','Mai','Junie',
		'Julie','August','Septembrie','Octobrie','Noiembrie','Decembrie'],
		monthNamesShort: ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun',
		'Jul', 'Aug', 'Sep', 'Oct', 'Noi', 'Dec'],
		dayNames: ['Duminica', 'Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata'],
		dayNamesShort: ['Dum', 'Lun', 'Mar', 'Mie', 'Joi', 'Vin', 'Sam'],
		dayNamesMin: ['Du','Lu','Ma','Mi','Jo','Vi','Sa'],
		dateFormat: 'mm/dd/yy', firstDay: 0,
		isRTL: false};
	jQuery.datepicker.setDefaults(jQuery.datepicker.regional['ro']);
});
