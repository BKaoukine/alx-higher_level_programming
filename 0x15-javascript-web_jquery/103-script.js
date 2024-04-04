document.addEventListener('DOMContentLoaded', function () {
  const base_url = 'https://hellosalut.stefanbohacek.dev/';

  $('#btn_translate').click(function () {
    const user_language = $('input#language_code').val();
    const url = `${base_url}?lang=${user_language}`;
    $('#hello').empty();
    $.get(url, function (response) {
      $('#hello').append(response.hello);
    });
  });

  $('input#language_code').keypress(function (e) {
    const key = e.which;
    if (key == '13') {
      $('#btn_translate').trigger('click');
    }
  });
});
