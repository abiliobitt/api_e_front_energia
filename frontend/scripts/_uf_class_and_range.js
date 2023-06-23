var global_ufs = [];
var global_AnmPeriodoReferencia = [];
var global_DscClasseConsumo = [];
var global_by_classe_consumo_and_range = [];
var table_data = [];
function onlyUnique(value, index, array) {
  return array.indexOf(value) === index;
}

$(document).ready(async function () {
  await $.ajax({
    type: "GET",
    url: "http://localhost:8000/potency_by_uf_and_class",
    cache: false,

    success: function (response) {
      table_data = new Array(...response);
      global_ufs = [...new Set(response.map((item) => item.SigUF))];
      global_AnmPeriodoReferencia = [
        ...new Set(response.map((item) => item.AnmPeriodoReferencia)),
      ];
      global_DscClasseConsumo = [
        ...new Set(response.map((item) => item.DscClasseConsumo)),
      ];
      global_DscClasseConsumo.map((type) => {
        global_AnmPeriodoReferencia.map(periodo => {
          var temp = new Object();
          temp.MdaPotenciaInstaladaKW = [];
          temp.DscClasseConsumo = type;
          temp.AnmPeriodoReferencia = [];
          response.map(item => {
            if(item.DscClasseConsumo === type && item.AnmPeriodoReferencia === periodo) {
              temp.AnmPeriodoReferencia.push(periodo)
              temp.data.push(parseInt(item.MdaPotenciaInstaladaKW))
            }
          })
          global_by_classe_consumo_and_range.push(temp)
        });
      });
    },
  });
});
