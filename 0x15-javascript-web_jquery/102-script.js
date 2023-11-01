/* Say hello to everybody! */

$(document).ready(function () {
    $("#btn_translate").click(function () {
        const myInput = $("#language_code");

        const inputValue = myInput.val();
        const URL = `https://hellosalut.stefanbohacek.dev/?lang=${inputValue}`;
        $.ajax({
            url: URL,
            method: "GET",
            dataType: "json",
            success: function (data) {
                $("#hello").html(data.hello);
            },
            error: function (xhr, status, error) {
                console.error("AJAX error:", status, error);
            }
        });
    });
});