#!/usr/bin/node
// JavaScript script that adds a <li> element to a list
// when the user clicks on the tag DIV#add_item

const ul_list = $("ul.my_list");
const add_li = $("div#add_item");

add_li.click(function(){
    ul_list.append("<li>Item</li>");
});