document.addEventListener('DOMContentLoaded', function () {

  const div_char = $('div#character');
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(response){
    div_char.append(response.name)
  })
});
