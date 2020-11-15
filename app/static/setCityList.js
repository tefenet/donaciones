let cityList = []

function getAjax(page) {
    return $.get({
        url: 'https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?page=' + page,
    })
}

function setOptions(jsonResponse) {
    let towns = jsonResponse.data.Town
    for (t in towns) {
        cityList.push(towns[t])
    }
    let page = jsonResponse.page
    if ((jsonResponse.total - page * jsonResponse.per_page) > 0) {
        getAjax(page + 1).done(setOptions)
    } else {
        select = document.getElementById('city_id')

        function appendOption(city) {
            newOption = document.createElement('option');
            newOption.value = parseInt(city.id, 10);
            newOption.text = city.name;
            select.appendChild(newOption);
        }

        cityList.sort((a, b) => a.name > b.name).forEach(appendOption)
    }
}

window.onload = () => {
    getAjax(1).done(setOptions)
}