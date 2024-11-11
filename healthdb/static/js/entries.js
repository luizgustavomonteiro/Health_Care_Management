function updateEntries(){
    const entries = document.getElementById("entriesSelect").value;
    const url = new URL(window.location.href);
    url.searchParams.set('entries', entries);
    window.location.href = url;
}   