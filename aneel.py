import requests 

def aneel_tensao(municipio):
    url = "https://www2.aneel.gov.br/aplicacoes/srd/dspConcessionaria.cfm?municipio={}".format(municipio)

    response = requests.request("POST", url)

    # Inicio fatiamento de resultados

    a = response.text.find('<label>')
    b = response.text.find('<br />')
    b = b - 12
    response_result = response.text[a:b]

    # Obtendo resultado A

    start_looking_for_a_end = response_result.find("</div>")
    result_not_final = response_result[:start_looking_for_a_end]
    result_final_A = result_not_final.replace('<label>', '').replace('</label> <span>', ': ').replace('</span>', '')

    # Obterndo resultado B

    start_looking_for_a_beginning = start_looking_for_a_end + 44
    taking_text = response_result[start_looking_for_a_beginning:]
    result_final_B = taking_text.replace('<label>', '').replace('</label> <span>', ': ').replace('</span></div>', '')

    print("==========================================================")
    print(result_final_A)
    print(result_final_B)
    print("==========================================================")

def aneel_municipio(UF, city="None", show_all=False):
    url = "https://www2.aneel.gov.br/aplicacoes/srd/dspMunicipios.cfm?municipio={}".format(UF)

    response = requests.request("POST", url)

    # Fatiamento de resultados

    end_all_html = response.text.find("</option>")

    end_all_end = response.text.find("</select>")

    end_html_result = response.text[end_all_html:end_all_end]

    # Procura e fatiamento da cidade

    if show_all == True:
        print(end_html_result)

    if city == "None":
        if show_all == False:
            print("[!] Nome de cidade não definido.")
        else:
            print(end_html_result)
    else:
        start_looking = end_html_result.find(city) - 10

        end_looking = end_html_result[start_looking:].find('</option>') + start_looking

        result = end_html_result[start_looking:end_looking].replace('"', '').replace(">", ": ")

        print(result)

# Primeiro pesquise a UF do seu estado e o nome da cidade para conseguir o número correspondente de identificação da cidade para a pesquisa.
aneel_municipio("PR", "Fazenda Rio Grande")

# Depois quando conseguir o número, chamar a outra função com o número correspondente. Lembrando que os números de cada cidade irão ser sempre de 7 dígitos.
aneel_tensao(4107652)