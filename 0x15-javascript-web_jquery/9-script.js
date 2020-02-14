const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(() => {
  $.ajax({
    method: 'GET',
    url
  }).done(data => {
    $('#hello').text(data.hello);
  });
});
