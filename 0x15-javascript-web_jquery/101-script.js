/* List, add, remove */

$(document).ready(function () {
    const add_item = $("#add_item");
    const remove_item = $("#remove_item");
    const clear_item = $("#clear_list");
    const my_list = $(".my_list")

    add_item.click(function () {
        const new_item = $("<li>Item</li>");

        my_list.append(new_item);
    });

    remove_item.click(function () {
        const lastListItem = $(".my_list li:last");

        lastListItem.remove();
    });

    clear_item.click(function () {
        my_list.empty();
    })
});
