$(document).ready(function () {
    url_agregar_fn();
    function url_agregar_fn(){
        rut_emp = $("#empleados_cmb").children("option:selected").val();
        $('#agregar_btn').attr("href", '/retiro-producto/agregar/'+rut_emp);
    }

    $("#empleados_cmb").on("change", function (e) {
        url_agregar_fn();
    });
});