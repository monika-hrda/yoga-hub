/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $('input#class_name, textarea#description').characterCounter();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        firstDay: 1,
        yearRange: 2,
        minDate: new Date(),
        showClearBtn: true,
        i18n: {
            done: "Select"
        },
        autoClose: true
    });
});