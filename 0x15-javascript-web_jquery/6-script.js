document.addEventListener('DOMContentLoaded', function () {
  const div = $('#update_header');
  div.click(function () {
    $('header').text('New Header!!!');
  });
});
