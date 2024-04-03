document.addEventListener('DOMContentLoaded', function () {
  const listMovie = $('ul#list_movies');
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
    const reslt = response.results;
    for (let i = 0; i < reslt.length; i++) {
      listMovie.append('<li>' + reslt[i].title + '</li>');
    }
  });
});
