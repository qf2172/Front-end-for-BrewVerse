$(document).ready(function() {
    $('#editMilkTeaForm').submit(function(event) {
        event.preventDefault();
        $('.text-danger').empty();

        const formData = {
            name: $('#name').val().trim(),
            brand: $('#brand').val().trim(),
            description: $('#description').val().trim(),
            rate: $('#rate').val().trim(),
            image: $('#image').val().trim(),
            ingredients: $('#ingredients').val().trim().split(',')
        };

        let isValid = validateForm(formData);
        if (isValid) {
            $.ajax({
                url: `/edit/${detail_data.id}`, 
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(formData),
                success: function(response) {
                    window.location.href = `/view/${response.id}`;
                },
                error: function(response) {
                    alert('There was an error updating the milk tea.');
                }
            });
        }
    });

    $('#discardChanges').click(function(event) {
        event.preventDefault();
        const isConfirmed = confirm('Are you sure you want to discard your changes?');
        if (isConfirmed) {
            const discardUrl = $(this).attr('href');
            window.location.href = discardUrl;
        }
    });
});

function validateForm(formData) {
    let isValid = true;

    if (!formData.name) {
        $('#error-name').text('Name is required.');
        isValid = false;
    }
    if (!formData.brand) {
        $('#error-brand').text('Brand is required.');
        isValid = false;
    }
    if (!formData.description) {
        $('#error-description').text('Description is required.');
        isValid = false;
    }
    if (!formData.rate || isNaN(parseFloat(formData.rate))) {
        $('#error-rate').text('A valid rate is required.');
        isValid = false;
    } else {
        const rateValue = parseFloat(formData.rate);
        if (rateValue < 0 || rateValue > 10) {
            $('#error-rate').text('Rate must be between 0 and 10.');
            isValid = false;
        }
    }
    if (!formData.image) {
        $('#error-image').text('Image URL is required.');
        isValid = false;
    } else {
        validateImageURL(formData.image, function(valid) {
            if (!valid) {
                $('#error-image').text('Image URL is invalid or inaccessible.');
                isValid = false;
            }
        });
    }
    if (!formData.ingredients || formData.ingredients.length === 0) {
        $('#error-ingredients').text('Ingredients are required.');
        isValid = false;
    }

    return isValid;
}
function validateImageURL(url, callback) {
    var img = new Image();
    img.onload = function() { callback(true); };
    img.onerror = function() { callback(false); };
    img.src = url;
}
