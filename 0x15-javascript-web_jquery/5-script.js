document.addEventListener('DOMContentLoaded', function () {
  const div = $('#add_item');
  div.click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
