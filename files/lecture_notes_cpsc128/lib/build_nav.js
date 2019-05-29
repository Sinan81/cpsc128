// build_nav.js
// Builds contents of nav element from rel="prev" and rel="next" link elements.
jQuery(document).ready(function(){
	var prev_href = jQuery('link[rel="Prev"]').attr('href');
	var next_href = jQuery('link[rel="Next"]').attr('href');
	var contents_href = jQuery('link[rel="Contents"]').attr('href');
	/* alert('Links: \n' + prev_href + '\n' + next_href + '\n' + contents_href ); */
	var prev_link = jQuery('<a></a>').attr('href',prev_href).attr('style','float: left;').text('← Previous page');
	var contents_link = jQuery('<a></a>').attr('href',contents_href).text('Contents');
	var next_link = jQuery('<a></a>').attr('href',next_href).attr('style','float: right;').text('Next page →');
	jQuery('nav').attr('style','text-align: center;').append(prev_link).append(contents_link).append(next_link);
	/*alert( jQuery('div#nav').text() );*/
});
