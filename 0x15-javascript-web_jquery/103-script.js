/*  And press ENTER */

$(document).ready(function () {
    $(document).ready(function () {
        const button = $("#btn_translate");
        const input = $("#language_code");

        function fetchData() {
            const query = input.val();
            const URL = "https://hellosalut.stefanbohacek.dev/?lang=" + query;

            $.ajax({
                url: URL,
                method: "GET",
                dataType: "json",
                success: function (data) {
                    $("#hello").html(`${data.hello}`);
                },
                error: function (xhr, status, error) {
                    console.error("API error:", status, error);
                }
            });
        }

        /* fetching data when pressing ENTER */
        input.keypress(function (event) {
            if (event.which === 13) {

                event.preventDefault();

                fetchData();
            }
        });

        /* fetching data when clicking btn_translate */
        button.click(fetchData);
    });
});