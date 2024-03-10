function clearErrorMessages() {
    $('.text-danger').text(''); 
}
function validateImageURL(url, callback) {
    var img = new Image();
    img.onload = function() { callback(true); };
    img.onerror = function() { callback(false); };
    img.src = url;
}
function validateForm(formData, callback) {
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
    if (!formData.rate) {
        $('#error-rate').text('Rate is required.');
        isValid = false;
    }else {
        if(isNaN(parseFloat(formData.rate))){
            $('#error-rate').text('Rate is invalid');
        }
    }
    if (!formData.ingredients) {
        $('#error-ingredients').text('Ingredients are required.');
        isValid = false;
    }
    if (!formData.image) {
        $('#error-image').text('Image URL is required.');
        isValid = false;
        callback(isValid);
    } else {
        validateImageURL(formData.image, function(exists) {
            if (!exists) {
                $('#error-image').text('Image URL is invalid or inaccessible.');
                isValid = false;
            }
            callback(isValid);
        });
    }
}

function submitForm(formData) {
    formData.ingredients = formData.ingredients.split(',');
    formData.rate = formData.rate.toString();

    $.ajax({
        type: 'POST',
        url: '/add',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(response) {
            console.log(response.id);
            $('#message').html('<div class="alert alert-success">New item successfully created. <a href="/view/' + response.id + '">See it here</a></div>');
            $('#addMilkTeaForm')[0].reset();
            $('#name').focus();
        },
        error: function(xhr, status, error) {
            $('#message').html('<div class="alert alert-danger">Error: ' + xhr.responseText + '</div>');
        }
    });
}
$(document).ready(function () {
    $('#addMilkTeaForm').submit(function (event) {
        event.preventDefault();
        clearErrorMessages(); 

        const formData = {
            name: $('#name').val().trim(),
            brand: $('#brand').val().trim(),
            description: $('#description').val().trim(),
            rate: $('#rate').val().trim(),
            image: $('#image').val().trim(),
            ingredients: $('#ingredients').val().trim()
        };
        console.log(formData);
        validateForm(formData, function(formIsValid) {
            if (formIsValid) {
                submitForm(formData);
            }
        });
    });
});
