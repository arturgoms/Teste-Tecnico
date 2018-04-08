$(document).ready(function () {
    homePage();
    updateTable();
    setInterval(updateTable, 500);

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
                userList += '<td><a id="showUpdateField" onclick="showUpdateField('+ key + ');" class="btn editar">Editar</a><a id="delete" onclick="deleteField('+ key +');" class="btn deletar">Deletar</a></td>';
                userList += '</tr>';    
            });
            $('#tabela').html(userList);
        },
        error: function(result) {
            try {
                $('#message').html("<strong>ERROR:</strong> " + result['responseJSON']['msg']);
                $('#alerta').show("fade", { direction: "right" }, 100);
            }
            catch(err) {
                $('#message').html("<strong>ERROR:</strong> Não foi possível atualizar a tabela");
                $('#alerta').show("fade", { direction: "right" }, 100);
            }
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
            $("#addNome").val('');
            $("#addSobrenome").val('');
            $("#addEndereco").val('');
            $('#alerta').hide("fade", { direction: "right" }, 100);
        },
        error: function(result) {
            $('#message').html("<strong>ERROR:</strong> " + result['responseJSON']['msg']);
            $('#alerta').show("fade", { direction: "right" }, 100);
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
        success: function (response) {
            $('#alerta').hide("fade", { direction: "right" }, 100);
        },
        error: function(result) {
            $('#message').html("<strong>ERROR:</strong> " + result['responseJSON']['msg']);
            $('#alerta').show("fade", { direction: "right" }, 100);
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
            $('#updateField').show("fade", { direction: "right" }, 300);
            $('#alerta').hide("fade", { direction: "right" }, 100);
        },
        error: function(result) {
                $('#message').html("<strong>ERROR:</strong> Não foi possível mostrar os campos de edição");
                $('#alerta').show("fade", { direction: "right" }, 100);
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
        success: function (response) {
            $('#alerta').hide("fade", { direction: "right" }, 100);
        },
        error: function(result) {
            $('#message').html("<strong>ERROR:</strong> " + result['responseJSON']['msg']);
            $('#alerta').show("fade", { direction: "right" }, 100);
        }
    });
    $('#updateField').hide("fade", { direction: "right" }, 100);
return false;
}

function aboutPage(){
    $.ajax({
        type: 'GET',
        url: 'about',
        success: function (response) {
            $('#content').html(response);
        },
        error: function(result) {
                $('#message').html("<strong>ERROR:</strong> Não foi possível mostrar os campos de edição");
                $('#alerta').show("fade", { direction: "right" }, 100);
        }
    });
    
}
function homePage(){
    $.ajax({
        type: 'GET',
        url: 'index',
        success: function (response) {
            $('#content').html(response);
        },
        error: function(result) {
                $('#message').html("<strong>ERROR:</strong> Não foi possível mostrar os campos de edição");
                $('#alerta').show("fade", { direction: "right" }, 100);
        }
    });
    
}