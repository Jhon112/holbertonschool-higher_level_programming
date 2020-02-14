$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const input = $('INPUT#language_code');
  const button = $('INPUT#btn_translate');

  button.click(e => {
    $.ajax({
      method: 'GET',
      url,
      data: { lang: input.val() }
    }).done(data => {
      $('#hello').text(data.hello);
    });
  });
});
