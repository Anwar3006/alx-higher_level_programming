const header = $("header.green");
const toggleHeader = $("div#toggle_header");

toggleHeader.click(function(){
    if (header.hasClass("green") === true)
    {
        header.removeClass("green");
        header.addClass("red");
    }
    else
    {
        header.removeClass("red");
        header.addClass("green");
    }
})