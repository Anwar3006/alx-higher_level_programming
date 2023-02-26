const headerElem = $('header');
const updateHeader = $('div#update_header');

updateHeader.click(function() {
  $headerElem.text('New Header!!!');
});