document.addEventListener('DOMContentLoaded', function () {
  const add_item = $('#add_item');
  const remove_item = $('#remove_item');
  const clear_list = $('#clear_list');
  const my_list = $('ul.my_list');

  add_item.click(function () {
    my_list.append('<li>Item</li>');
  });

  remove_item.click(function () {
    $('ul li:last').remove();
  });

  clear_list.click(function () {
    $('ul.my_list li').remove();
  });
});
