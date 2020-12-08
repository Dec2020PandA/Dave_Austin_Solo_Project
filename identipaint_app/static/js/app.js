$(document).foundation()

$("#test-answer").on("submit", function () {
    $(".hide-info").removeClass("hide-info")
    window.setTimeout(function () {
        $(".orbit").foundation("changeSlide", (isLTR = true))
    }, 2000)
    return false
})
