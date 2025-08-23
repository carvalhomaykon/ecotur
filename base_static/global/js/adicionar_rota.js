let pontosRota = JSON.parse(localStorage.getItem('pontosRota')) || [];
console.log("Pontos carregados do localStorage:", pontosRota);

function adicionarRota(pontoNome, pontoCoords, username, pontoId) {
    if (!username) {
        alert('Você precisa estar logado para adicionar pontos à rota!');
        return;
    }

    try {
        // Garante que pontoCoords seja JSON válido
        pontoCoords = typeof pontoCoords === 'string' ? JSON.parse(pontoCoords) : pontoCoords;
    } catch (error) {
        console.error("Erro ao parsear coordenadas:", pontoCoords);
        return;
    }

    var botao = event.target;
    var textoBotao = botao.innerHTML.trim();

    // Verifica se o ponto já está na lista
    const index = pontosRota.findIndex(p => p.nome === pontoNome && p.username === username);

    if (textoBotao === 'Adicionar à Rota' && index === -1) {
        pontosRota.push({ nome: pontoNome, coords: pontoCoords, username: username, id: pontoId });
        botao.innerHTML = 'Rota Adicionada';
        botao.style.backgroundColor = 'red';
        botao.style.color = 'white';

        alert(pontoNome + ' adicionado à Rota!');
        console.log('Ponto adicionado:', { nome: pontoNome, coords: pontoCoords });
    } else if (textoBotao === 'Rota Adicionada' && index !== -1) {
        const removido = pontosRota.splice(index, 1)[0];
        botao.innerHTML = 'Adicionar à Rota';
        botao.style.backgroundColor = '';
        botao.style.color = '';

        alert(pontoNome + ' removido da Rota!');
        console.log('Ponto removido:', removido);
    }

    // Atualiza o localStorage
    localStorage.setItem('pontosRota', JSON.stringify(pontosRota));
    console.log('Estado atual da lista:', pontosRota);

}
function limparPontosTuristicos() {
    // Limpa os pontos do localStorage
    localStorage.removeItem('pontosRota');

    // Atualiza a lista em memória
    pontosRota = [];

    // Exibe uma mensagem de confirmação
    alert('Todos os pontos turísticos foram removidos.');

    // Atualiza a interface (se necessário)
    location.reload(); // Recarrega a página para resetar o mapa e a interface
}

// Nova Função
// Função para aplicar estilos aos pontos já adicionados à rota
function marcarPontosSelecionados(username) {
    if (!username) return; // Verifica se o usuário está logado

    document.querySelectorAll('.adicionar-rota').forEach((botao) => {
        const pontoNome = botao.getAttribute('data-nome'); // Nome do ponto associado ao botão
        const pontoExiste = pontosRota.some(p => p.nome === pontoNome && p.username === username);

        if (pontoExiste) {
            botao.innerHTML = 'Rota Adicionada';
            botao.style.backgroundColor = 'red';
            botao.style.color = 'white';
        } else {
            botao.innerHTML = 'Adicionar à Rota';
            botao.style.backgroundColor = '';
            botao.style.color = '';
        }
    });
}

// Chame a função ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const username = document.body.getAttribute('data-username'); // Suponha que o username esteja disponível como atributo no <body>
    marcarPontosSelecionados(username);
});
