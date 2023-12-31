var global_potency_by_state_and_time_range = [];
var potency_by_state_and_time_range = [];
var global_ufs = [];
var global_AnmPeriodoReferencia = [];
var table_data = [];
function onlyUnique(value, index, array) {
    return array.indexOf(value) === index;
  }

$( document ).ready(async function() {
    await $.ajax({
        type: "GET",
        url: "http://localhost:8000/potency_by_state_and_time_range",
        cache: false,
        
        success: function(response){
        table_data = new Array(...response);
        global_ufs = [...new Set(response.map(item => item.SigUF))]
        global_AnmPeriodoReferencia = [...new Set(response.map(item => item.AnmPeriodoReferencia))]
        global_ufs.map(uf => {
            var data = new Object();
            data.SigUF = uf;
            data.MdaPotenciaInstaladaKW = [];
            data.AnmPeriodoReferencia = [];
            response.map(item => {
                if(item.SigUF === uf) {
                    data.MdaPotenciaInstaladaKW.push(parseInt(item.MdaPotenciaInstaladaKW))
                    data.AnmPeriodoReferencia.push(item.AnmPeriodoReferencia)
                }
            })
            potency_by_state_and_time_range.push(data);
        })
        potency_by_state_and_time_range.map(
            (item) => {
            var temp_data = new Object();
                temp_data.label = item.SigUF;
                temp_data.x = [...item.AnmPeriodoReferencia];
                temp_data.data = [...item.MdaPotenciaInstaladaKW];
                global_potency_by_state_and_time_range.push(temp_data)
            }
          );
        }
        });
        const ctx = document.getElementById("myChart");
        new Chart(ctx, {
          type: "line",
          data: {
            labels: global_AnmPeriodoReferencia,
            datasets: global_potency_by_state_and_time_range
          },
          options: {
            parsing: {
              xAxisKey: 'AnmPeriodoReferencia',
              yAxisKey: 'MdaPotenciaInstaladaKW'
            }
          }
        });
        new gridjs.Grid({
        columns: ["Estado", "Periodo", "Potencia instalada"],
        data: table_data.map( item => {
          return [item.SigUF, item.AnmPeriodoReferencia, item.MdaPotenciaInstaladaKW]
      })
      }).render(document.getElementById("table_wrapper"));
});