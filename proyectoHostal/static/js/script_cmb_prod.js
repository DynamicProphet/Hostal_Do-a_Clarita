$(document).ready(function () {
  $("#id_fk_id_marca").on("change", function (e) {
    var url = '';
    var url2 = '';
    id_marca = $(this).children("option:selected").val();
    if(id_marca == ''){
        url = '#'
        url2 = '#'
    }else{
        url = '/producto/id_fk_id_marca/editar/'+ id_marca;
        url2 = '/producto/id_fk_id_marca/eliminar/'+ id_marca;
    }
    $('#editarid_fk_id_marca').attr("href", url);
    $('#eliminarid_fk_id_marca').attr("href", url2);
  });

  $("#id_fk_id_tipo").on("change", function (e) {
    var url = '';
    var url2 = '';
    id_tipo = $(this).children("option:selected").val();
    if(id_tipo == ''){
        url = '#'
        url2 = '#'
    }else{
        url = '/producto/id_fk_id_tipo/editar/'+ id_tipo;
        url2 = '/producto/id_fk_id_tipo/eliminar/'+ id_tipo;
    }
    $('#editarid_fk_id_tipo').attr("href", url);
    $('#eliminarid_fk_id_tipo').attr("href", url2);

  });
});
