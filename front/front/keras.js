$.ajaxSetup({
    contentType: "application/json; charset=utf-8"
});

function sendRequest() {
    frases = []
    url = "http://localhost:5000/depressao"
    $('input[type="text"]').each(function () {
        if ($(this).val() != "") {
            frases.push($(this).val())
        }
    });
    dataFrases = {
        frases
    }   
    $("#result").text("...")
    $("#acuracia").text("...")
    $.post( url,JSON.stringify(dataFrases), function( data ) {
        $("#result").text(data.isDepressivo)
        $("#acuracia").text(data.acuracia)    
    })
    .fail(function(response){
        alert("Erro ao obter resultado...")
    })
}
function gerarFrases() {
    idPessoa = Math.floor(Math.random() * (287-233)) + 233;
    url = "http://localhost:5000/getFrases/"+idPessoa
    $('input[type="text"]').each(function () {
        $(this).val('')
    })
    $("#result").text("...")
    $("#acuracia").text("...")
    $.get( url,function( data ) {
        i = 0
        $("#result").text(data.isDepressivo)
        $("#acuracia").text(data.acuracia)
        $('input[type="text"]').each(function () {
            $(this).val(data.frases[i])
            i += 1
        })
    })
    .fail(function(response){
        alert("Erro ao obter resultado...")
    }) 
}

function limparFrases(){
    $('input[type="text"]').each(function () {
        $(this).val("")
    })
    $("#result").text("")
    $("#acuracia").text("")
}

$("#sendRequest").click(function(e) {
    e.preventDefault();
    setTimeout(function(){
        sendRequest()
    },1000)
})
$("#gerarFrases").click(function(e){
    e.preventDefault()
    setTimeout(function(){gerarFrases()}, 1000)
})
$("#limpar").click(function(e){
    e.preventDefault()
    setTimeout(function(){
        limparFrases()
    },1000)
})