$(document).ready(function () {
    $('#searchForm').on('submit', function(event) {
        var searchValue = $('#searchInput').val().trim();
        console.log(searchValue);
        if (searchValue === '') {
            event.preventDefault();
            alert('Please enter a search term.');
            $('#searchInput').val('');
            $('#searchInput').focus();
        }
    });
});