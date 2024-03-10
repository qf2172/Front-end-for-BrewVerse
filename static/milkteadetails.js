function display_milk_tea_detail(detail_data,data) {
    $("#milkTeaDetailsContainer").empty();
    const scaledRating = detail_data.rate / 2;
    let stars = '';
    for (let i = 1; i <= 5; i++) {
        if (i <= Math.floor(scaledRating)) {
            stars += '<span class="star filled">&#9733;</span>';
        } else if (i === Math.ceil(scaledRating) && !Number.isInteger(scaledRating)) {
            stars += '<span class="star filled">&#9734;</span>';
        } else {
            stars += '<span class="star">&#9734;</span>';
        }
    }
    const imageAndBasicInfo = `
        <div class="row justify-content-center deletemarginrow">
            <div id="leftcontainer" class="col-md-9 deletepadding">
                <div class="row deletemarginrow">
                    <div class="col-md-3">
                    <img class="card-image-detail" src="${detail_data.image}" alt="${detail_data.name}">
                    </div>
                    <div class="col-md-9 addrightpadding">
                        <h2 class="title">${detail_data.name}</h2>
                        <p class="addbottom">
                            <span style="color: darkgray;">ingredients</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            ${detail_data.ingredients.map(ingredient => 
                                `<a href="/search?ingredient=${encodeURIComponent(ingredient)}" style="text-decoration: none; margin-right: 10px;" class="clickable-text">${ingredient}&nbsp;|</a>`
                            ).join('')}
                        </p>
                        <p class="addbottom"><span style="color: darkgray;">brand</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/search?brand=${encodeURIComponent(detail_data.brand)}"style="text-decoration: none; margin-right: 10px;" class="clickable-text">${detail_data.brand}</a></p>
                        <p class="addbottom"><span style="color: darkgray;">price</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${detail_data.price.join(' / ')}</p>
                        <p class="addbottom"><span style="color: darkgray;">publish time</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${detail_data['publish time']}</p>
                        <button type="button" class="btn btn-outline-dark edit-button" onclick="window.location.href='/edit/${detail_data.id}'">Edit</button>
                    </div>
                </div>
                <div id="star-rating">${stars}</div>
                <div id="description">
                <h3 class="text" style="margin-bottom:20px"><span style="color: darkgray; font-size: 25px; font-weight: bold;">Description</span></h3>
                    <p class="des">${detail_data.description}</p>
                </div>
                <div id="reviews">
                    <h3 class="text" style="margin-bottom:20px"><span style="color: darkgray; font-size: 25px;font-weight: bold;">Reviews</span></h3>
                    ${detail_data.reviews.map(review => `<div class="phar"><p>${review}</p></div>`).join('')}
                </div>
            </div>
            <div id="similar milk tea" class="col-md-3 similar">
                <h3 class="text">Similar</h3>
                <div class="similar-milk-tea-container">
                    ${detail_data["similar milk tea ids"].map(teaId => `
                    <a href="/view/${teaId}" style="text-decoration: none; color: inherit;">
                        <div class="milk-tea-card">
                            <img  class="milk-tea-image" src="${data[teaId].image}" alt="${data[teaId].name}">
                            <div class="milk-tea-name">
                                <p style="margin-bottom: 5px">${data[teaId].name}</p>
                            </div>
                        </div>
                        `).join('')}
                    </a>
                    
                </div>
            </div>
        </div>
    `;
    $("#milkTeaDetailsContainer").append(imageAndBasicInfo);
}

$(document).ready(function () {
    display_milk_tea_detail(detail_data,data)
})