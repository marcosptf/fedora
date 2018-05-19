#query default example
query {
  peopleList {
    edges {
      node {
        id
        name
        height
        mass
        hairColor
        skinColor
        eyeColor
        birthYear
        gender
        created
        edited
        url
        planet {
          id
          name
          rotationPeriod
          diameter
          climate
          gravity
          terrain
          surfaceWater
          population
          created
          edited
          url
        }
      }
    }
  }
}


#query {
	planet(id:"UGVvcGxlOjI=") {
    id
    name
  }
}

#query simples
query{
    peopleList{
      edges{
        node{
          id
          name
      }
    }
  }
}

#query com variaveis peopleList
#dont work because peopleLIst dont have variable support
query{
  peopleList(id:"UGVvcGxlOjE="){
    id
    name
  }
}


#query com variaveis planet
query {
	planet(id:"UGxhbmV0OjE="){
		id
		name
	}      
}



#example create data with mutation query
mutation {
  createPerson (input: {
    name: "nova pessoa"
    height: "189"
    mass: "73"
    hairColor: "brown"
    skinColor: "white"
    eyeColor: "green"
    birthYear: "1983"
    gender: "male"
    planetId: "UGxhbmV0Ojk="
  }) {
    person {
      id
      name
      height
      mass
      hairColor
      skinColor
      eyeColor
      birthYear
      gender
      planet {
        id
        name
      }
      created
      edited
      url
    }
  }
}

#example of update data with MutationEvent()
mutation {
  updatePlanet (input:{
    id: "UGxhbmV0Ojk="
    name: "fiat-marea-hlx"
  }) {
    planet {
      id
      name
      rotationPeriod
      orbitalPeriod
      diameter
      climate
      terrain
      surfaceWater
      population
      created
      edited
      url
    }
  }
}

mutation{
    updatePlanet(input:{id:"UGxhbmV0Ojk=" name:"fiat-tipo-slx"}){
        planet{
            id
            name
        }
    }
}

query{
  planet(id:"UGxhbmV0Ojk="){
    id
    name
  }
}






