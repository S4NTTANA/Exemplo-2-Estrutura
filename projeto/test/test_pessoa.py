# Testes de cobertura
import pytest
from projeto.models.pessoa import Pessoa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 22)
    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    # Alterando o nome da pessoa de 'Marta' para 'Vitória'
    pessoa_valida.nome = "Vitória"
    assert pessoa_valida.nome == "Vitória"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 22

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Idade não pode ser negativa."):
        Pessoa("Marta", -1)
    