/* Click and turn red */

$(document).ready(function () {
    let myDiv = $("#red_header");

    myDiv.click(function () {
        $("header").css("color", "#FF0000");
    });
});