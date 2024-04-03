document.addEventListener('DOMContentLoaded', function () {
    const div = $('#toggle_header');
    const var_header = $('header')
    var_header.addClass('red')
  
    div.click(function() {
        if (var_header.hasClass("red")) {
          var_header.removeClass("red").addClass("green");
        } else {
          var_header.removeClass("green").addClass("red");
        }
      });
  });
