# utils/extract.py

import re

def extract_data(text):
    extracted_data = {
        "name": "",
        "cpf": "",
        "rg": "",
        "naturalidade": "",
        "orgao_emissor": ""
    }
    
    # Exemplo básico de extração usando regex (ajuste conforme necessário)
    name_match = re.search(r'Nome:\s*(.*)', text)
    if name_match:
        extracted_data["name"] = name_match.group(1).strip()

    cpf_match = re.search(r'CPF:\s*([\d\.]+)', text)
    if cpf_match:
        extracted_data["cpf"] = cpf_match.group(1).strip()

    rg_match = re.search(r'RG:\s*([\d\.]+)', text)
    if rg_match:
        extracted_data["rg"] = rg_match.group(1).strip()

    naturalidade_match = re.search(r'Naturalidade:\s*(.*)', text)
    if naturalidade_match:
        extracted_data["naturalidade"] = naturalidade_match.group(1).strip()

    orgao_emissor_match = re.search(r'Orgão Emissor:\s*(.*)', text)
    if orgao_emissor_match:
        extracted_data["orgao_emissor"] = orgao_emissor_match.group(1).strip()

    return extracted_data


