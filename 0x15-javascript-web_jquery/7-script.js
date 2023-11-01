/* Star wars character */

$(document).ready(function () {
    const URL = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

    $.ajax({
        url: URL,
        method: "GET",
        dataType: "json",
        success: function (data) {
            $("#character").html(data.name)
        },
        error: function (xhr, status, error) {
            console.error("AJAX error:", status, error);
        }
    });
});
