$(document).foundation()

function update_info() {
    $("#artist-info").html($(".is-active .artist-info").html())
    console.log("fire!")
}

$("[data-orbit]").on("slidechange.zf.orbit", function () {
    update_info()
})

$("#test-answer button").on("click", function () {
    let answer = $(this).attr("value")

    if ($(".is-active").attr("id") == answer) {
        $(".is-active .correct").removeClass("hide-info")
    } else {
        $(".is-active .wrong").removeClass("hide-info")
    }

    $(".is-active .artist-info").removeClass("hide-info")
    window.setTimeout(function () {
        $(".orbit").foundation("changeSlide", (isLTR = true))
    }, 2000)

    return false
})

update_info()
