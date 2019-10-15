$("#formFrases").submit(function(e) {
    e.preventDefault();
    sendRequest()
})


function sendRequest() {
    frases = []
    url = "http://localhost:5000/depressao"
    $('input[type="text"]').each(function () {
        if ($(this).val() != "") {
            frases.push($(this).val())
        }
    });

    data = {
        frases
    }

    $.post( url,frases, function( data ) {
        
    });
}

function gerarFrases() {
    frasesNeutras = ["", "", "", "", "", "", "", "", "", ""]
    frasesDepressivas = ["", "", "", "", "", "", "", "", "", ""]
    frasesNaoDepressivas = ["", "", "", "", "", "", "", "", "", ""]
    $('input[type="radio"]').each(function () {
        if ($(this).is(":checked")) {
            radio = $(this).val()
        }
    });
    console.log(radio)
}

