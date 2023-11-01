/* Star wars movies */

$(document).ready(function () {
    const URL = "https://swapi-api.alx-tools.com/api/films/?format=json"

    $.ajax({
        url: URL,
        method: "GET",
        dataType: "json",
        success: function (data) {
            const movies = data.results;
            for (const movie of movies) {
                const li = $(`<li>${movie.title}</li>`);
                $("#list_movies").append(li);
            }
        },
        error: function (xhr, status, error) {
            console.error("AJAX error:", status, error);
        }
    });
});
