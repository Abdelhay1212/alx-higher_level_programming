/* Say Hello */

$(document).ready(function () {
    const URL = "https://hellosalut.stefanbohacek.dev/?lang=fr"

    $.ajax({
        url: URL,
        method: "GET",
        dataType: "json",
        success: function (data) {
            $("#hello").html(`${data.hello}`);
        },
        error: function (xhr, status, error) {
            console.error("AJAX error:", status, error);
        }
    });
});
