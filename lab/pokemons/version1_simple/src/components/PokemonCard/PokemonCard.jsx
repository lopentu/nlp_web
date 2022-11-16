import { useState, useEffect } from 'react';
import styled from 'styled-components';

import PokemonCardActions from './PokemonCardActions';
import PokemonCardContent from './PokemonCardContent';

const Card = styled.div`
  border: 2px dashed gray; 
  margin: 15px;
  padding: 10px;
  width: 400px;
`;

export default function PokemonCard({
  pokemonUrl,
  handleAddToCart
}) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [pokemon, setPokemon] = useState(null);
  const [count, setCount] = useState(0); 

  useEffect(() => {
    fetch(pokemonUrl)
      .then(response => {
        return response.json();
      })
      .then(data => {
        setPokemon(data);
      })
      .catch(error=> setError(error))
      .finally(()=> setLoading(false))
  }, [pokemonUrl])

  const handleAdd = () => setCount(count + 1);
  const handleSubtract = () => {
    if (count > 0){
      setCount(count - 1);
    }
  }


  if (loading || !pokemon) {
    return <p>loading</p>
  }

  if (error) {
    return <p>something wrong QQ</p>
  }

  return (
    <Card>
      <PokemonCardContent pokemon={pokemon} />  
      <PokemonCardActions
        handleAdd={handleAdd}
        handleSubtract={handleSubtract}
        handleAddToCart={handleAddToCart}
        pokemon={pokemon}
        count={count}
      />
    </Card>
  )
}