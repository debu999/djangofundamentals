function resetForms() {
    for (i = 0; i < document.forms.length; i++) {
        document.forms[i].reset();
    }
}

$(document).ready(function () {
    $('#updateflg').click(function () {
        let ischk = $('#updateflg').is(":checked");
        if (ischk) {
            $("#delDiv").hide();
            $("#todoall").hide();
            // $("#updDiv").show();
            $("#updlistrad").show();
            $('input[name="updlist"]').prop('checked', false);
            $('#updbtn').show();
            $('#addbtn').hide();
        }
        else {
            $("#delDiv").show();
            $("#todoall").show();
            // $("#updDiv").hide();
            $("#updlistrad").hide();
            $('#addbtn').show();
            $('#updbtn').hide();
        }
    });
    $('.todoupdls').on('change', function () {
        let idVal = $(this).attr("id");
        let pkVal = $(this).val();
        $('#id_text').val($.trim($("label[for='" + idVal + "']").text()));
        $('#id_todo').attr("value", pkVal);
    });
    resetForms();
});

function removechecked() {
    $('#updateflg').prop('checked', false);
    // $('#updDiv').hide();
    $('#updbtn').hide();
    $('#updlistrad').hide();
}