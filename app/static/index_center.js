function getAjax(idMuni) {
    return $.get({
        url: 'https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios/' + idMuni,
    })
}
let esparta = (index,ev) => {        
    muni = document.getElementById('Municipio'+index)        
    key=muni.accessKey
    getAjax(key).done((jsonResponse)=>{        
    muni.innerText = 'Municipio: '+jsonResponse.data.Town[key].name    
    })
}

$(document).ready(function () {
        $('.toggle').click(function () {
            document.getElementById('form-' + this.childNodes[0].value).submit()
        })
        document.getElementsByName('show-center').forEach(n =>
            $(document).on('show.bs.modal', '#modalShowCenter' + n.attributes.content.value, esparta.bind(event, n.attributes.content.value)
            )
        )})