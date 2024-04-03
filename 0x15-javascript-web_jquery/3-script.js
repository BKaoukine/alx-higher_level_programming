document.addEventListener('DOMContentLoaded', function () {
  const div = $('div#red_header');

  div.click(function () {
    $('header').addClass('red');
  });
});
