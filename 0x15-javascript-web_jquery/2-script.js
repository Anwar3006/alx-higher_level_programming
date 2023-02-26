// Updates the text color of the <header> element to red 
// when the user clicks on the tag DIV#red_header

const redHead = $("div#red_header");
const header = $("header");

redHead.click(function(){
    redHead.css("color", "red");
});