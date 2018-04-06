$(document).ready(function () {

    // add a variable that remains through closure
    var lastTimeResponse = [];

    function getRealData() {
        $.get("api", function(dados, status){
            response = $.parseJSON(dados);

            $(function() {
            $.each(response, function(i, item) {
                var $tr = $('<tr>').append(
                    $('<td>').text(i),
                    $('<td>').text(item["nome"]),
                    $('<td>').text(item["sobrenome"]),
                    $('<td>').text(item["endereco"])
                ); //.appendTo('#records_table');
            $("#tabela").append($tr)
            });
        });
    });
    }
    getRealData();

});