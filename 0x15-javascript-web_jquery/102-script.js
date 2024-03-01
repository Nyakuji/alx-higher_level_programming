const url = 'https://www.fourtonfish.com/hellosalut/hello/';
$(this).ready(function () {
  $('#btn_translate').on('click', function () {
    $.getJSON(url + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
