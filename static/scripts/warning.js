function warning(ID) {
    if (ID == 'delete') {
        if (confirm("Remove this item from basket?")) {
            document.getElementById(ID).submit();
        }
    }
    else if (ID == 'clear') {
        if (confirm("Remove all items from basket?")) {
            document.getElementById(ID).submit();
        }
    }
}