document.addEventListener('DOMContentLoaded', function () {
  const hello = $('#hello');
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    const reslt = response.hello;
    hello.append(reslt);
  });
});
