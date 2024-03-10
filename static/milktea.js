function display_milk_tea(data) {
    $("#milkTeaContainer").empty();
    Object.values(data).forEach((milkTea) => {
        console.log(milkTea);
        const ingredientsText = milkTea.ingredients ? milkTea.ingredients.join(', ') : 'No ingredients listed';
        const milkTeaCard = $(`
            <div class="col-md-3 col-sm-6 mb-4 one_card_container">
                <div class="card" id="milkTea-${milkTea.id}">
                    <img src="${milkTea.image}" class="card-img-top" alt="${milkTea.name}">
                    <div class="card-body">
                        <div class="card-title">${milkTea.name}<div/>
                        <p class="text-muted">Ingredients: ${ingredientsText}</p> <!-- 添加ingredients -->
                        <div class="text-muted">Brand: ${milkTea.brand}</div>
                    </div>
                </div>
            </div>
        `);
        milkTeaCard.on('click', function() {
            window.location.href = `/view/${milkTea.id}`;
        })
        $("#milkTeaContainer").append(milkTeaCard);
    })

}

$(document).ready(function () {
    console.log(data)
    display_milk_tea(data)
})