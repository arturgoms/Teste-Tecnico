$(document).ready(function () {

    // add a variable that remains through closure
    var lastTimeResponse = [];

    function getRealData() {
        $.get("api", function(dados, status){
            response = $.parseJSON(dados);
            //console.log(response)
            //var vehicleListData = '';
            var userList = '';
            $.each(response, function(key, value) {
                userList += '<tr id="rowVehicleStatus" class="">';
                userList += '<td>'+key+'</td>';
                userList += '<td>'+value["nome"]+'</td>';
                userList += '<td>'+value["sobrenome"]+'</td>';
                userList += '<td>'+value["endereco"]+'</td>';
                userList += '</tr>';     
            });
            $('#tabela').html(userList);

        });
    }

    //this refreshes data every 2seconds
    setInterval(getRealData, 1000);

    //call the function to display data
    getRealData();

});
