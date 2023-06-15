import inject
import json
import os

from infra.http_client.httpx.http_client import HttpClient
from settings.data.dataSettings import DataSettings

def write_json(new_data, filename='data.json'):
    if os.path.isfile(filename):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['records'].append(new_data)
            file.seek(0)
            # file.truncate()  # limpar o conteúdo do arquivo
            json.dump(file_data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump(new_data, file, indent=4)

class DataService:

    @staticmethod
    async def get_data():
        http_adapter: HttpClient = inject.instance(HttpClient)
        
        response = await http_adapter.get(
            DataSettings.URL,
            headers={
            }
        )
        # json_object = json.dumps(response.payload.records, indent=4)
        # with open("data.json", "w") as outfile:
        #     outfile.write(json_object)
        for i in response.payload["result"]["records"]:
            item = dict()
            item["_id"]= i["_id"],
            item["DatGeracaoConjuntoDados"]= i["DatGeracaoConjuntoDados"],
            item["AnmPeriodoReferencia"]= i["AnmPeriodoReferencia"],
            item["NumCNPJDistribuidora"]= i["NumCNPJDistribuidora"],
            item["SigAgente"]= i["SigAgente"],
            item["NomAgente"]= i["NomAgente"],
            item["CodClasseConsumo"]= i["CodClasseConsumo"],
            item["DscClasseConsumo"]= i["DscClasseConsumo"],
            item["CodSubGrupoTarifario"]= i["CodSubGrupoTarifario"],
            item["DscSubGrupoTarifario"]= i["DscSubGrupoTarifario"],
            item["codUFibge"]= i["codUFibge"],
            item["SigUF"]= i["SigUF"],
            item["codRegiao"]= i["codRegiao"],
            item["NomRegiao"]= i["NomRegiao"],
            item["CodMunicipioIbge"]= i["CodMunicipioIbge"],
            item["NomMunicipio"]= i["NomMunicipio"],
            item["CodCEP"]= i["CodCEP"],
            item["SigTipoConsumidor"]= i["SigTipoConsumidor"],
            item["NumCPFCNPJ"]= i["NumCPFCNPJ"],
            item["NomeTitularEmpreendimento"]= i["NomeTitularEmpreendimento"],
            item["CodEmpreendimento"]= i["CodEmpreendimento"],
            item["DthAtualizaCadastralEmpreend"]= i["DthAtualizaCadastralEmpreend"],
            item["SigModalidadeEmpreendimento"]= i["SigModalidadeEmpreendimento"],
            item["DscModalidadeHabilitado"]= i["DscModalidadeHabilitado"],
            item["QtdUCRecebeCredito"]= i["QtdUCRecebeCredito"],
            item["SigTipoGeracao"]= i["SigTipoGeracao"],
            item["DscFonteGeracao"]= i["DscFonteGeracao"],
            item["DscPorte"]= i["DscPorte"],
            item["MdaPotenciaInstaladaKW"]= i["MdaPotenciaInstaladaKW"],
            item["NumCoordNEmpreendimento"]= i["NumCoordNEmpreendimento"],
            item["NumCoordEEmpreendimento"]= i["NumCoordEEmpreendimento"],
            item["NomSubEstacao"]= i["NomSubEstacao"],
            item["NumCoordESub"]= i["NumCoordESub"],
            item["NumCoordNSub"]= i["NumCoordNSub"]
            write_json(item)
        
        return response