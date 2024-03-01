const url = 'https://www.fourtonfish.com/hellosalut/hello/';
$(this).ready(function () {
  $('#btn_translate').on('click', function () {
    $.getJSON(url + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      $.getJSON(url + $(this).val(), function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
