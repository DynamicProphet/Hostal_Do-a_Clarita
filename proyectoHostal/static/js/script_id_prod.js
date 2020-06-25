$(document).ready(function () {
  /// ID : 3 numeros random + 3 del id_proveedor + 3 del id_tipo + 8 de la fecha de venc
  /// 999 999 999 99999999

  //999 n° random
  var id_1 = getRndInteger(100, 999).toString();

  //999 id proveedor
  var id_2 = $("#id_fk_id_tipo").children("option:selected").val();
  id_2 = validarLength2(id_2);

  $("#id_fk_id_tipo").on("change", function (e) {
    id_2 = "";
    id_2 = $(this).children("option:selected").val();
    id_2 = validarLength2(id_2);
  });

  ///999 id tipo
  var id_3 = $("#id_fk_id_proveedor").children("option:selected").val();
  id_3 = validarLength2(id_3);

  $("#id_fk_id_proveedor").on("change", function (e) {
    id_3 = "";
    id_3 = $(this).children("option:selected").val();
    id_3 = validarLength2(id_3);
  });

  ///99999999 fecha venc
  
  var dd = $("#id_fecha_venc_day").children("option:selected").val();
  dd = validarLength1(dd);

  var mm = $("#id_fecha_venc_month").children("option:selected").val();
  mm = validarLength1(mm);

  var yyyy = $("#id_fecha_venc_year").children("option:selected").val();;

  $("#id_fecha_venc_day").on("change", function (e) {
    dd = "";
    dd = $(this).children("option:selected").val();
    dd = validarLength1(dd);
  });
  $("#id_fecha_venc_month").on("change", function (e) {
    mm = "";
    mm = $(this).children("option:selected").val();
    mm = validarLength1(mm);
  });
  $("#id_fecha_venc_year").on("change", function (e) {
    yyyy = "";
    yyyy = $(this).children("option:selected").val();
  });

  $("select").on("change", function (e) {
    var id_4 = '';
    id_4 = dd + mm + yyyy;
    if (id_4 == "") {
      id_4 = "0";
    }
    full_id = id_1 + id_2 + id_3 + id_4;
    $("#id_id").val(full_id);
  });

  function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function validarLength2(x) {
    if (x.length == 1) {
      x = "00" + x;
    } else if (x.length == 2) {
      x = "0" + x;
    }
    return x;
  }

  function validarLength1(x) {
    if (x.length == 1) {
      x = "0" + x;
    }
    return x;
  }
});
