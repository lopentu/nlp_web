import styled from 'styled-components';

const Image = styled.img`
  width: 120px;
`;

const Price = styled.p`
  font-weight: 700;
  text-align: right;
`;

export default function PokemonCardContent({pokemon}) {
  return (
    <>
      <h3>{pokemon.name.toUpperCase()}</h3>

      {/** https://pwo-wiki.info/index.php/Base_Experience */}
      <p>Base experience: {pokemon.base_experience}</p>
      <p>Abilities:
        {pokemon.abilities.map((ability, idx) => (
          <span 
            key={`${idx}_${ability.ability.name}`}
            style={{padding: '5px'}} 
          >
            {ability.ability.name}
          </span>
        ))}
      </p>
      
      <Image 
        src={pokemon.sprites.front_default} 
        alt="pokemon.sprites.front_default"
      />
      <Image
        src={pokemon.sprites.back_default} 
        alt="pokemon.sprites.back_default"
      />
      <Price>Price: ${pokemon.weight}</Price>
    </>
  )
}