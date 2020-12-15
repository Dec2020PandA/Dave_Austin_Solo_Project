$(document).foundation()

var counter = 0

function update_info() {
    $("#artist-info").html($(".is-active .artist-info").html())
}

$("[data-orbit]").on("slidechange.zf.orbit", function () {
    update_info()
})

$("#test-answer button").on("click", function () {
    if ($("#artist-info").attr("class") == "hide-info") {
        let answer = $(this).attr("value")

        if ($(".is-active").attr("id") == answer) {
            $("#test_messages .correct").removeClass("hide-info")
            counter++
        } else {
            $("#test_messages .wrong").removeClass("hide-info")
        }

        $("#artist-info").removeClass("hide-info")
        $("#continue button").css("display", "block")
    }

    return false
})

$("#continue").on("submit", function () {
    if ($(".is-active").attr("data-slide") != 4) {
        $("#test_messages *").addClass("hide-info")
        $("#artist-info").addClass("hide-info")
        $("#continue button").css("display", "none")

        window.setTimeout(function () {
            $(".orbit").foundation("changeSlide", (isLTR = true))
        }, 500)
        return false
    } else {
        $("#results_input").val(counter)
    }
})

update_info()
