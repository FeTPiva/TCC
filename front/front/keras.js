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
        console.log(data.isDepressivo)
    })
}

function gerarFrases() {
    idPessoa = Math.floor(Math.random() * 287) + 234; // 288
    url = "http://localhost:5000/getFrases"
    data = {
        "id":idPessoa
    }
    $.post( url,data, function( data ) {
        
    });
}

