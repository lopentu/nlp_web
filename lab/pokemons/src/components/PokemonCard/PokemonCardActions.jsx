import PropTypes from 'prop-types';
import styled from 'styled-components';

import Button from '../Button';

const CardAction = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const AddToCartButton = styled(Button)`
  background-color: ${props => props.isDisabled ? "gray" : "blue"};
  color: white;
  font-size: 18px;
  border: none;
  cursor:  ${props => props.isDisabled ? "default": "pointer"};
`;

export default function PokemonCardActions({
  handleAdd, 
  handleSubtract, 
  handleAddToCart,
  pokemon, 
  count
}){
  return (
    <CardAction>
      <div>
        <Button onClick={handleAdd} label="+" />
        <span style={{padding: '5px'}}>{count}</span>
        <Button onClick={handleSubtract} label="-" />
      </div>

      <AddToCartButton
        onClick={() => handleAddToCart({
          pokemonName: pokemon.name, 
          id: pokemon.id,
          count,
          price: pokemon.weight,
        })}
        disabled={count <= 0}
        isDisabled={count <= 0}
        label="Add to cart"
      />
    </CardAction>
  )
}

PokemonCardActions.propTypes = {
  handleAdd: PropTypes.func.isRequired,
  handleSubtract: PropTypes.func.isRequired,
  handleAddToCart: PropTypes.func.isRequired,
  pokemon: PropTypes.object.isRequired,
  count: PropTypes.number.isRequired,
}