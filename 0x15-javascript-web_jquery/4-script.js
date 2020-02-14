$('div#toggle_header').click(e => {
  e.preventDefault();
  $('header').toggleClass('green red');
});
