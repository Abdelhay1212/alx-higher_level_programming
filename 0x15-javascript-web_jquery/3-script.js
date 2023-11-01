/* Add `.red` class */

$(document).ready(function () {
    let myDiv = $("#red_header");

    myDiv.click(function () {
        $("header").addClass("red");
    });
});
