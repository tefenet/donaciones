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
  }
  else {
    let select = document.getElementById('city_id')
    const selected = select.selectedOptions[0].value
    while (select.childNodes.length >= 1) {
      select.removeChild(select.firstChild);
    }
    function appendOption(city) {
      newOption = document.createElement('option');
      newOption.value = city.id;
      newOption.text = city.name;
      select.appendChild(newOption);
    }
    cityList.sort((a, b) => a.name > b.name).forEach(appendOption)
    select.value = selected ? selected : 1
  }
}
window.onload = () => {
  getAjax(1).done(setOptions)
}
