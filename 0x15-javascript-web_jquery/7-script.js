$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json').done((data)=>{
    console.log(data.name)
})