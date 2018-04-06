$(document).ready(function () {

    // add a variable that remains through closure
    var lastTimeResponse = [];

    function getRealData() {
        $.get("api", function(data, status){
        $("#teste").html(data["REQUEST_METHOD"]);
    });
    }

    //this refreshes data every 2seconds
    setInterval(getRealData, 1000);

    //call the function to display data
    getRealData();

});