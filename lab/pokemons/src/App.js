import { useState } from 'react';
import styled from 'styled-components';

import Header from './components/Header';
import PokemonCard from './components/PokemonCard/PokemonCard';
import useFetch from "./hooks/useFetch";

// https://pokeapi.co/
const url = "https://pokeapi.co/api/v2/pokemon?limit=30";

const PokemonsWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 200px;
`;

function App() {
  const [notification,setNotification] = useState(null);
  const {loading, error, data: pokemons} = useFetch({
    url, 
    resolvedPath: 'results'
  });

  const handleAddToCart = ({pokemonName, count}) => {
    setNotification(()=> ({
      pokemonName,
      count,
    }))

    setTimeout(()=>{
      setNotification(null);
    }, 3000)
  }

  if (loading || !pokemons) {
    return <p>loading</p>;
  }

  if (error) {
    return <p>something wrong QQ</p>
  }

  return (
    <div>
      <Header notification={notification} />

      <PokemonsWrapper>
        {pokemons?.map(pokemon=> (
          <PokemonCard
            key={`${pokemon.id}_${pokemon.url}`} 
            pokemonUrl={pokemon.url} 
            handleAddToCart={handleAddToCart}
          />
        ))}
      </PokemonsWrapper>
      
    </div>
  );
}

export default App;
