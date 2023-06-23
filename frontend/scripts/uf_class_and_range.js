var global_potency_by_uf_and_class = [];
var potency_by_uf_and_class = [];
var global_ufs = [];
var global_DscClasseConsumo = [];
var global_AnmPeriodoReferencia = [];
var table_data = [];
function onlyUnique(value, index, array) {
    return array.indexOf(value) === index;
  }

$( document ).ready(async function() {
    await $.ajax({
        type: "GET",
        url: "http://localhost:8000/potency_by_uf_and_class",
        cache: false,
        
        success: function(response){
        table_data = new Array(...response);
        global_ufs = [...new Set(response.map(item => item.SigUF))]
        global_DscClasseConsumo = [...new Set(response.map(item => item.DscClasseConsumo))]
        global_AnmPeriodoReferencia = [...new Set(response.map(item => item.AnmPeriodoReferencia))]
        global_DscClasseConsumo.map(type => {
            var data = new Object();
            data.DscClasseConsumo = type;
            data.MdaPotenciaInstaladaKW = [];
            data.AnmPeriodoReferencia = [];
            response.map(item => {
                if(item.DscClasseConsumo === type) {
                    data.MdaPotenciaInstaladaKW.push(parseInt(item.MdaPotenciaInstaladaKW))
                    data.AnmPeriodoReferencia.push(item.AnmPeriodoReferencia)
                }
            })
            potency_by_uf_and_class.push(data);
        })
        potency_by_uf_and_class.map(
            (item) => {
            var temp_data = new Object();
                temp_data.label = item.DscClasseConsumo;
                temp_data.x = [...item.AnmPeriodoReferencia];
                temp_data.data = [...item.MdaPotenciaInstaladaKW];
                global_potency_by_uf_and_class.push(temp_data)
            }
          );
        }
        });
        const ctx = document.getElementById("myChart");
        new Chart(ctx, {
          type: "line",
          data: {
            labels: global_AnmPeriodoReferencia ,
            datasets: global_potency_by_uf_and_class
          },
          options: {
            parsing: {
              xAxisKey: 'AnmPeriodoReferencia',
              yAxisKey: 'MdaPotenciaInstaladaKW'
            }
          }
        });
        console.log(global_potency_by_uf_and_class)
        new gridjs.Grid({
        columns: ["Classe de Consumo", "Periodo", "Potencia instalada"],
        data: table_data.map( item => {
          return [item.DscClasseConsumo, item.AnmPeriodoReferencia, item.MdaPotenciaInstaladaKW]
      })
      }).render(document.getElementById("table_wrapper"));
});