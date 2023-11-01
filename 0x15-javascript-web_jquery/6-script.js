/* Update the text of an element */

$(document).ready(function () {
    let myDiv = $("#update_header");

    myDiv.click(function () {
        $("header").html("New Header!!!");
    });
});
