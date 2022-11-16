import { useState, useEffect } from 'react';
import styled from 'styled-components';

import Header from './components/Header';
import PokemonCard from './components/PokemonCard/PokemonCard';

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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [pokemons, setPokemons] = useState(null);

  useEffect(() => {
    // https://javascript.info/fetch
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(data => {
        setPokemons(data.results);
      })
      .catch(error=> setError(error))
      .finally(()=> setLoading(false))
  }, [])

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
