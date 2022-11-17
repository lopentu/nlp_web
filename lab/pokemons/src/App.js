import { useState } from 'react';
import styled from 'styled-components';

import Header from './components/Header';
import PokemonCard from './components/PokemonCard/PokemonCard';
import CartInfo from './components/CartInfo';
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
  
  /**
   *  較好的方式是 cart 內只存 {id: id, count: count} ，不存多餘的資訊（e.g., price）
   *  因為 id 應該要是 unique，count 是使用者操作過後的值
   *  然後再回查資料來源： pokemons 列表 or pokemon data ，找到要呈現在 cart 裡對應的資訊
   *  但因為 pokemons 列表裡目前只有 name & url，
   *  所以這裡就先取巧，直接在 handleAddToCart 裡傳入 cart 呈現時需要的所有資料
   */
   const [cart, setCart] = useState([]);

   const {loading, error, data: pokemons} = useFetch({
    url, 
    resolvedPath: 'results'
  });

  const updateCart = ({pokemonName, count, price}) => {
    const hasPokemonAddedToCart = cart.find(pokemon => pokemon.name === pokemonName);
    if (!hasPokemonAddedToCart) {
      setCart([
        ...cart, 
        {name: pokemonName, count, price}
      ])
    } else {
      const updatedCart = cart.map(pokemon => (
        pokemon.name === pokemonName
          ?  {...pokemon, count}
          : pokemon
      ));
      setCart(updatedCart)
    }
  }

  const showAlert = ({pokemonName,count}) => {
    setNotification(()=> ({
      pokemonName,
      count,
    }))

    setTimeout(()=>{
      setNotification(null);
    }, 3000)
  }

  const handleAddToCart = ({pokemonName, count, price}) => {
    showAlert({pokemonName, count});
    updateCart({pokemonName, count, price});
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

      <CartInfo cart={cart} />
      
    </div>
  );
}

export default App;
