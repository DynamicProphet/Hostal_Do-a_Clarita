$(document).ready(function () {
  var path = $("#path").val();
  id_marca_fn();
  id_tipo_fn();

  function id_marca_fn(){
    var url = '';
    var url2 = '';
    id_marca = $("#id_fk_id_marca").children("option:selected").val();
    if(id_marca == ''){
        url = '#'
        url2 = '#'
    }else{
        url = '/producto/id_fk_id_marca/editar/'+ id_marca+'?next='+path;
        url2 = '/producto/id_fk_id_marca/eliminar/'+ id_marca+'?next='+path;
    }
    $('#editarid_fk_id_marca').attr("href", url);
    $('#eliminarid_fk_id_marca').attr("href", url2);
  };
  function id_tipo_fn(){
    var url = '';
    var url2 = '';
    id_tipo = $("#id_fk_id_tipo").children("option:selected").val();
    if(id_tipo == ''){
        url = '#'
        url2 = '#'
    }else{
        url = '/producto/id_fk_id_tipo/editar/'+ id_tipo+'?next='+path;
        url2 = '/producto/id_fk_id_tipo/eliminar/'+ id_tipo+'?next='+path;
    }
    $('#editarid_fk_id_tipo').attr("href", url);
    $('#eliminarid_fk_id_tipo').attr("href", url2);
  };

  $("#id_fk_id_marca").on("change", function (e) {
    id_marca_fn();
  });

  $("#id_fk_id_tipo").on("change", function (e) {
    id_tipo_fn();
  });
});
