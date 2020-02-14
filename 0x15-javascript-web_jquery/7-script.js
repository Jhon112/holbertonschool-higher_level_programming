const url = 'https://swapi.co/api/people/5/?format=json';

$.ajax({
  type: 'GET',
  url: url
}).done(data => {
  $('#character').text(data.name);
});
