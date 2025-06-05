from fastapi import FastAPI
from pydantic import BaseModel
from unidecode import unidecode

app = FastAPI()

# Lista de cidades aprovadas
approved_cities = [unidecode(city).lower() for city in [
    "Abaetetuba", "Abreu e Lima", "Açailândia", "Acaraú", "Águas Lindas de Goiás", "Alagoinhas", "Alegrete", "Alenquer", "Alfenas", "Almirante Tamandaré", "Altamira", "Alvorada", "Americana", "Amparo", "Ananindeua", "Anápolis", "Angra dos Reis", "Aparecida de Goiânia", "Apucarana", "Aquiraz", "Aracaju", "Aracati", "Aracruz", "Araguaína", "Araguari", "Arapiraca", "Araranguá", "Araras", "Araripina", "Araruama", "Araucária", "Araxá", "Arcoverde", "Ariquemes", "Arujá", "Assis", "Atibaia", "Avaré",
    "Bacabal", "Bagé", "Balneário Camboriú", "Balsas", "Barbacena", "Barbalha", "Barcarena", "Barra do Corda", "Barra do Garças", "Barra do Piraí", "Barra Mansa", "Barreiras", "Barreirinhas", "Barretos", "Barueri", "Bauru", "Bayeux", "Bebedouro", "Belém", "Belford Roxo", "Belo Horizonte", "Belo Jardim", "Benevides", "Bento Gonçalves", "Bertioga", "Betim", "Bezerros", "Biguaçu", "Birigui", "Blumenau", "Boa Vista", "Boituva", "Bom Jesus da Lapa", "Botucatu", "Brasília", "Bragança", "Bragança Paulista", "Breves", "Brumado", "Brusque",
    "Cabedelo", "Cabo de Santo Agostinho", "Cabo Frio", "Caçador", "Caçapava", "Cáceres", "Cachoeira do Sul", "Cachoeirinha", "Cachoeiro de Itapemirim", "Cacoal", "Caicó", "Caieiras", "Cajamar", "Cajazeiras", "Caldas Novas", "Camaçari", "Camaquã", "Camaragibe", "Camboriú", "Cametá", "Camocim", "Campina Grande", "Campo Bom", "Campo Formoso", "Campo Largo", "Campo Limpo Paulista", "Campo Mourão", "Campos dos Goytacazes", "Canaã dos Carajás", "Candeias", "Canindé", "Canoas", "Capanema", "Capão da Canoa", "Caraguatatuba", "Carapicuíba", "Caratinga", "Carazinho", "Cariacica", "Carpina", "Caruaru", "Casa Nova", "Cascavel", "Castanhal", "Castro", "Cataguases", "Catalão", "Catanduva", "Caucaia", "Caxias", "Caxias do Sul", "Ceará-Mirim", "Chapadinha", "Cianorte", "Cidade Ocidental", "Coari", "Codó", "Colatina", "Colombo", "Conceição do Coité", "Concórdia", "Conselheiro Lafaiete", "Contagem", "Coronel Fabriciano", "Corumbá", "Cotia", "Crateús", "Crato", "Criciúma", "Cristalina", "Cruz das Almas", "Cruzeiro", "Cruzeiro do Sul", "Cubatão", "Curvelo",
    "Diadema", "Dias d'Ávila", "Divinópolis", "Dourados", "Duque de Caxias",
    "Embu das Artes", "Embu-Guaçu", "Erechim", "Esmeraldas", "Estância", "Esteio", "Euclides da Cunha", "Eunápolis", "Eusébio", "Extremoz",
    "Farroupilha", "Fazenda Rio Grande", "Feira de Santana", "Ferraz de Vasconcelos", "Floriano", "Florianópolis", "Formiga", "Fortaleza", "Francisco Beltrão", "Francisco Morato", "Franco da Rocha",
    "Garanhuns", "Gaspar", "Goiana", "Goianésia", "Goiânia", "Goianira", "Governador Valadares", "Grajaú", "Gravatá", "Gravataí", "Guaíba", "Guanambi", "Guarapari", "Guaratinguetá", "Guarujá", "Guarulhos", "Gurupi",
    "Horizonte", "Hortolândia",
    "Ibirité", "Ibitinga", "Ibiúna", "Icó", "Igarapé-Miri", "Igarassu", "Iguatu", "Ijuí", "Ilhéus", "Imperatriz", "Indaial", "Indaiatuba", "Ipatinga", "Ipojuca", "Iranduba", "Irecê", "Itabaiana", "Itaberaba", "Itabira", "Itaboraí", "Itabuna", "Itacoatiara", "Itaguaí", "Itaitinga", "Itaituba", "Itajaí", "Itajubá", "Itanhaém", "Itapecerica da Serra", "Itapecuru Mirim", "Itapema", "Itaperuna", "Itapetinga", "Itapetininga", "Itapeva", "Itapevi", "Itapipoca", "Itapira", "Itaquaquecetuba", "Itatiba", "Itaúna", "Itu", "Ituiutaba", "Itumbiara", "Itupeva",
    "Jaboatão dos Guararapes", "Jaboticabal", "Jacareí", "Jacobina", "Janaúba", "Jandira", "Januária", "Japeri", "Jaraguá do Sul", "Jataí", "Jaú", "Jequié", "Ji-Paraná", "João Monlevade", "João Pessoa", "Joinville", "Juazeiro", "Juazeiro do Norte", "Juiz de Fora", "Jundiaí",
    "Lagarto", "Lages", "Lagoa Santa", "Lajeado", "Lauro de Freitas", "Leme", "Lençóis Paulista", "Limeira", "Linhares", "Lins", "Lorena", "Lucas do Rio Verde", "Luís Eduardo Magalhães", "Luziânia",
    "Macaé", "Macaíba", "Macapá", "Maceió", "Magé", "Mairiporã", "Manacapuru", "Manaus", "Manhuaçu", "Marabá", "Maracanaú", "Maranguape", "Marechal Deodoro", "Mariana", "Maricá", "Marília", "Marituba", "Matão", "Mauá", "Maués", "Mesquita", "Mineiros", "Mirassol", "Mococa", "Mogi das Cruzes", "Mogi Guaçu", "Mogi Mirim", "Moju", "Mongaguá", "Monte Alegre", "Monte Mor", "Montenegro", "Montes Claros", "Morada Nova", "Mossoró", "Muriaé",
    "Natal", "Navegantes", "Nilópolis", "Niterói", "Nossa Senhora do Socorro", "Nova Friburgo", "Nova Iguaçu", "Nova Lima", "Nova Odessa", "Nova Serrana", "Novo Gama", "Novo Hamburgo", "Novo Repartimento",
    "Olinda", "Oriximiná", "Osasco", "Ouricuri", "Ourinhos", "Ouro Preto",
    "Pacajus", "Pacatuba", "Paço do Lumiar", "Palhoça", "Palmas", "Palmeira dos Índios", "Pará de Minas", "Paracatu", "Paragominas", "Paranaguá", "Paranavaí", "Parauapebas", "Parintins", "Parnaíba", "Parnamirim", "Passo Fundo", "Passos", "Pato Branco", "Patos", "Patos de Minas", "Patrocínio", "Paulínia", "Paulista", "Paulo Afonso", "Pedro Leopoldo", "Pelotas", "Penápolis", "Peruíbe", "Pesqueira", "Petrolina", "Petrópolis", "Picos", "Pindamonhangaba", "Pinhais", "Pinheiro", "Piraquara", "Pirassununga", "Piripiri", "Planaltina", "Poá", "Ponta Porã", "Portel", "Porto Nacional", "Porto Seguro", "Porto Velho", "Pouso Alegre", "Praia Grande", "Presidente Prudente",
    "Queimados", "Quixadá", "Quixeramobim",
    "Recife", "Redenção", "Resende", "Ribeirão das Neves", "Ribeirão Pires", "Rio Branco", "Rio Claro", "Rio das Ostras", "Rio de Janeiro", "Rio do Sul", "Rio Grande", "Rio Largo", "Rio Verde", "Rolândia", "Russas",
    "Sabará", "Salgueiro", "Salto", "Salvador", "Santa Bárbara d'Oeste", "Santa Cruz do Capibaribe", "Santa Cruz do Sul", "Santa Inês", "Santa Izabel do Pará", "Santa Luzia", "Santa Maria", "Santa Rita", "Santa Rosa", "Santana", "Santana de Parnaíba", "SantAna do Livramento", "Santarém", "Santo André", "Santo Ângelo", "Santo Antônio de Jesus", "Santo Antônio do Descoberto", "Santos", "São Bento do Sul", "São Bernardo do Campo", "São Caetano do Sul", "São Carlos", "São Cristóvão", "São Félix do Xingu", "São Gonçalo", "São Gonçalo do Amarante", "São João da Boa Vista", "São João de Meriti", "São João del Rei", "São José", "São José de Ribamar", "São José dos Pinhais", "São Leopoldo", "São Lourenço da Mata", "São Luís", "São Mateus", "São Paulo", "São Pedro da Aldeia", "São Roque", "São Sebastião", "São Sebastião do Paraíso", "São Vicente", "Sapiranga", "Sapucaia do Sul", "Saquarema", "Sarandi", "Senador Canedo", "Senhor do Bonfim", "Seropédica", "Serra", "Serra Talhada", "Serrinha", "Sertãozinho", "Sete Lagoas", "Simões Filho", "Sobral", "Sousa", "Sumaré", "Surubim", "Suzano", 
    "Tabatinga", "Taboão da Serra", "Tailândia", "Tangará da Serra", "Tatuí", "Tauá", "Tefé", "Teixeira de Freitas", "Telêmaco Borba", "Teófilo Otoni", "Teresina", "Teresópolis", "Tianguá", "Timon", "Timóteo", "Tomé-Açu", "Três Corações", "Três Lagoas", "Três Rios", "Trindade", "Tubarão", "Tucuruí", "Tupã",
    "Ubá", "Ubatuba", "Uberaba", "Unaí", "Uruguaiana",
    "Vacaria", "Valença", "Valença", "Valparaíso de Goiás", "Varginha", "Várzea Grande", "Várzea Paulista", "Venâncio Aires", "Vespasiano", "Viamão", "Viana", "Viçosa", "Vila Velha", "Vilhena", "Vitória", "Vitória da Conquista", "Vitória de Santo Antão", "Volta Redonda", "Votorantim", "Votuporanga"
]]

# Lista de cidades em operação
operating_cities = [unidecode(city).lower() for city in [
    "Lavras", "Rondonópolis", "Umuarama", "Guarapuava", "Londrina", "Cambé", "Maringá", "Foz de Iguaçu", "Chapecó", "Campinas", "São José do Rio Preto", "Vinhedo", "São José dos Campos"
]]

# Lista de cidades em implantação
deploying_cities = [unidecode(city).lower() for city in [
    "Formosa", "Aparecida de Goiânia", "Uberlandia", "Poços de Calda", "Campo Grande" "Corumbá", "Dourados", "Sinop", "Sorriso", "Cuiabá", "Primavera do Leste", "Toledo ", "Curitiba", "Ponta Grossa ", "Arapongas ", "São José Dos Pinhais", "Cidade do leste ", "Porto Alegre", "Sorocaba", "Piracicaba", "Araçatuba", "Bauru", "Ribeirão preto", "Araraquara ", "Franca", "Taubaté", "Limeira", "Presidente Prudente", "Americana"
]]

class MessageRequest(BaseModel):
    city: str

def check_city_status(city_name: str) -> str:
    normalized_city = unidecode(city_name).lower()

    if normalized_city in approved_cities:
        return "approved"
    elif normalized_city in operating_cities:
        return "operating"
    elif normalized_city in deploying_cities:
        return "deploying"
    else:
        return "not_found"

@app.post("/verify_city")
async def verify_city(message_request: MessageRequest):
    city_name = message_request.city
    status = check_city_status(city_name)

    if status == "approved":
        return {"status": "success", "message": f"A cidade {city_name} está aprovada!"}
    elif status == "operating":
        return {"status": "operating", "message": f"A cidade {city_name} está em operação!"}
    elif status == "deploying":
        return {"status": "deploying", "message": f"A cidade {city_name} está em implantação!"}
    else:
        return {"status": "failure", "message": f"A cidade {city_name} não está aprovada."}
