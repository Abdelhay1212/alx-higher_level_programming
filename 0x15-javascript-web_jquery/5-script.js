/* Append element into another one */

$(document).ready(function () {
    let myDiv = $("#add_item");
    let newLi = $("<li>Item</li>");

    myDiv.click(function () {
        $(".my_list").append(newLi);
    });
});
