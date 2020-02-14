const url = 'https://swapi.co/api/films/?format=json';

$.ajax({
  method: 'GET',
  url
}).done(data => {
  for (const movie of data.results) {
    const title = `<li>${movie.title}</li>`;
    $('UL#list_movies').append(title);
  }
});
