$(document).ready(function () {
    updateTable();
    setInterval(updateTable, 1000);

});

function updateTable() {
    $.ajax({
        type: 'GET',
        url: 'api',
        success: function (response) {
            dados = $.parseJSON(response);
            var userList = '';
            $.each(dados, function(key, value) {
                userList += '<tr id="rowUsers" class="">';
                userList += '<td>'+value["nome"]+'</td>';
                userList += '<td>'+value["sobrenome"]+'</td>';
                userList += '<td>'+value["endereco"]+'</td>';
                userList += '<td><a id="showUpdateField" onclick="showUpdateField('+ key + ');" class="submit btn">Editar</a>&nbsp<a onclick="deleteField('+ key +');" class="submit btn">Deletar</a></td>';
                userList += '</tr>';    
            });
            $('#tabela').html(userList);
        },
        error: function(result) {

        }
    });
}
function addField() {
    var nome = $("#addNome").val();
    var sobrenome = $("#addSobrenome").val();
    var endereco = $("#addEndereco").val();
    $.ajax({
        type: 'POST',
        url: 'api',
        data: {
            nome:nome,
            sobrenome:sobrenome,
            endereco:endereco
        },
        success: function (response) {
            
        },
        error: function(result) {
            // Do something with the result
        }
    });
    return false;
}

function deleteField(id){
    $.ajax({
        url: 'api',
        type: 'DELETE',
        data: {
            id:id
        },
        success: function(result) {
            // Do something with the result
        },
        error: function(result) {
            // Do something with the result
        }
    });
}

function showUpdateField(id){
    $.ajax({
        type: 'GET',
        url: 'api',
        success: function (response) {
            dados = $.parseJSON(response);
            $('#updateId').val(id);
            $('#updateNome').val(dados[id]['nome']);
            $('#updateSobrenome').val(dados[id]['sobrenome']);
            $('#updateEndereco').val(dados[id]['endereco']);
            $('#updateField').show("fade", { direction: "right" }, 100);
        },
        error: function(result) {

        }
    });
    
}

function updateField(){
    var id = $("#updateId").val();
    var nome = $("#updateNome").val();
    var sobrenome = $("#updateSobrenome").val();
    var endereco = $("#updateEndereco").val();
    $.ajax({
        url: 'api',
        type: 'PUT',
        data: {
            id:id,
            nome:nome,
            sobrenome:sobrenome,
            endereco:endereco
        },
        success: function(response) {
         //...
        },
        error: function(result) {
            // Do something with the result
        }
    });
    $('#updateField').hide("fade", { direction: "right" }, 100);
return false;
}