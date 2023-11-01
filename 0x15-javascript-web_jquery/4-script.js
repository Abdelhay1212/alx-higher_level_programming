/* Toggle classes */

$(document).ready(function () {
    let myDiv = $("#toggle_header");

    myDiv.click(function () {
        $("header").toggleClass("red green");
    });
});
