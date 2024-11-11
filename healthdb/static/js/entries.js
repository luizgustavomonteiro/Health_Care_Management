function updateEntries() {
    // Captura o valor do select
    var entries = document.getElementById('entries').value;

    // Obtém a URL atual e atualiza a query string
    var currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set('entries', entries);  // Atualiza o valor de entries na URL

    // Carrega a nova URL para que o servidor saiba qual valor de "entries" usar
    window.location.href = currentUrl.toString();
}
